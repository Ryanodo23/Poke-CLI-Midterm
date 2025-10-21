1. Project Overview

The PokeCLI is a simple command-line interface (CLI) application built in Python. Its primary function is to fetch and display structured information about Pokémon and Pokémon types from the PokeAPI (https://pokeapi.co/).

Technology Stack: Python 3.9+, the requests library for networking, and argparse for the CLI.

Goal: Provide quick, readable access to key Pokémon data without requiring the user to navigate a browser.

2. Architecture Breakdown

The project follows a modular design pattern with a strict separation of concerns into three main files. All three files must reside in the same directory.

api_client.py

Responsibility: Data Access Layer. Handles all external network calls to the PokeAPI.

Dependencies: requests, random.

Key Functions: get_pokemon_data(identifier), get_type_data(type_name), get_random_pokemon_id().

Error Handling: Responsible for network and HTTP error handling (4xx/5xx errors, timeouts). Returns raw JSON dictionaries or None on failure.

data_processor.py

Responsibility: Business Logic/Presentation Layer. Responsible for transforming raw JSON data into human-readable, formatted strings suitable for CLI output.

Dependencies: None (N/A).

Key Functions: format_pokemon_details(data), format_type_details(data).

cli.py

Responsibility: Presentation/Orchestration Layer. Defines the command-line interface using argparse. Parses user input, delegates tasks, and prints the final output to the console.

Dependencies: argparse, api_client, data_processor.

Key Functions: handle_search(), handle_random(), handle_type(), main().

3. CLI Command Structure

The main entry point is cli.py, which uses sub-commands defined via argparse.

search

Usage Example: python cli.py search [name or ID]

Purpose: Retrieves detailed information for a single Pokémon.

Expected Output: Name, ID, Types, Height (in meters), Weight (in kilograms), and Abilities.

random

Usage Example: python cli.py random

Purpose: Retrieves details for a Pokémon selected randomly from the total available count.

Expected Output: Same details as the search command.

type

Usage Example: python cli.py type [type_name]

Purpose: Retrieves data on a specific Pokémon type.

Expected Output: Type name, damage relations (double damage to, half damage to, no damage to), and a list of sample Pokémon of that type.

4. Coding Standards and Guidelines

Type Hinting: All functions must use Python type hints for clarity (e.g., -> Optional[Dict[str, Any]]).

External Libraries: The use of requests is mandatory for all network operations in api_client.py.

Data Units: In data_processor.py, all raw API units (decimetres for height, hectograms for weight) must be converted to metric units (meters, kilograms) for user display.

Error Handling (API): Network and HTTP errors (4xx, 5xx) must be handled within api_client.py using response.raise_for_status() and try/except blocks. None should be returned upon failure.

Error Handling (CLI): Any generic exceptions should be caught in the main function of cli.py to prevent abrupt tool crashes.

Formatting: The presentation logic in data_processor.py should ensure output is clearly formatted with headers and easy-to-read lists.