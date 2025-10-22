import pytest

def _make_api_stub_module():
    types = __import__("types")
    mod = types.ModuleType("api_client")
    mod.get_pokemon_data = lambda identifier: {
        "name": "pikachu",
        "id": 25,
        "types": [{"type": {"name": "electric"}}],
        "height": 4,
        "weight": 60,
        "abilities": [{"ability": {"name": "static"}}],
    }
    mod.get_random_pokemon_id = lambda: 25
    mod.get_type_data = lambda type_name: {
        "name": type_name,
        "damage_relations": {"double_damage_to": [], "half_damage_to": [], "no_damage_to": []},
        "pokemon": [{"pokemon": {"name": "pikachu"}}],
    }
    return mod

def _make_dp_stub_module():
    types = __import__("types")
    mod = types.ModuleType("data_processor")
    mod.format_pokemon_details = lambda data: f"FORMATTED POKEMON: {data.get('name')}"
    mod.format_type_details = lambda data: f"FORMATTED TYPE: {data.get('name')}"
    return mod

def _load_main_with_mocks():
    sys = __import__("sys")
    importlib_util = __import__("importlib.util")
    pathlib = __import__("pathlib")

    PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[1]
    MAIN_PATH = PROJECT_ROOT / "src" / "main.py"

    # inject stubs so main.py imports resolve to mocks (no real API calls)
    sys.modules["api_client"] = _make_api_stub_module()
    sys.modules["data_processor"] = _make_dp_stub_module()

    spec = importlib_util.spec_from_file_location("main", str(MAIN_PATH))
    main_mod = importlib_util.module_from_spec(spec)
    sys.modules["main"] = main_mod
    spec.loader.exec_module(main_mod)
    return main_mod

def test_search_prints_formatted_pokemon(capsys):
    main = _load_main_with_mocks()
    rc = main.main(["search", "pikachu"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "FORMATTED POKEMON: pikachu" in out

def test_random_uses_api_stub(capsys):
    main = _load_main_with_mocks()
    rc = main.main(["random"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "FORMATTED POKEMON" in out

def test_type_prints_formatted_type(capsys):
    main = _load_main_with_mocks()
    rc = main.main(["type", "electric"])
    out = capsys.readouterr().out
    assert rc == 0
    assert "FORMATTED TYPE: electric" in out

def test_no_subcommand_shows_help(capsys):
    main = _load_main_with_mocks()
    rc = main.main([])
    captured = capsys.readouterr()
    out = captured.out + captured.err
    assert rc == 0
    assert ("usage" in out.lower()) or ("error" in out.lower())