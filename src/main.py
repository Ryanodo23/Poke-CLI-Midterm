from typing import Optional
import argparse
import sys

def handle_search(args: argparse.Namespace) -> None:
    # Integration with api_client / data_processor has been removed.
    print(f"search called with identifier: {args.identifier}")
    print("Note: api_client and data_processor integrations were removed from this file.", file=sys.stderr)

def handle_random(args: argparse.Namespace) -> None:
    # Integration with api_client / data_processor has been removed.
    print("random called")
    print("Note: api_client and data_processor integrations were removed from this file.", file=sys.stderr)

def handle_type(args: argparse.Namespace) -> None:
    # Integration with api_client / data_processor has been removed.
    print(f"type called with type_name: {args.type_name}")
    print("Note: api_client and data_processor integrations were removed from this file.", file=sys.stderr)

def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="pokecli", description="PokeCLI - query Pokemon and types")
    subparsers = parser.add_subparsers(title="commands", dest="command")

    p_search = subparsers.add_parser("search", help="Retrieve details for a single Pokémon (name or ID)")
    p_search.add_argument("identifier", help="Pokemon name or ID")
    p_search.set_defaults(func=handle_search)

    p_random = subparsers.add_parser("random", help="Retrieve details for a random Pokémon")
    p_random.set_defaults(func=handle_random)

    p_type = subparsers.add_parser("type", help="Retrieve data for a Pokémon type")
    p_type.add_argument("type_name", help="Type name (e.g. fire, water)")
    p_type.set_defaults(func=handle_type)

    args = parser.parse_args(argv)
    if not hasattr(args, "func"):
        parser.print_help()
        return 0

    try:
        args.func(args)
        return 0
    except Exception as exc:
        print(f"An error occurred: {exc}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
