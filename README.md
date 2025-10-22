# Poke-CLI

[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](https://github.com/Ryanodo23/Poke-CLI-Midterm/tree/main/tests)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple command-line interface (CLI) for fetching and displaying information about Pokémon from the [PokeAPI](https://pokeapi.co/).

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Ryanodo23/Poke-CLI-Midterm.git
    cd Poke-CLI-Midterm
    ```

2.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

The Poke-CLI has three main commands: `search`, `random`, and `type`.

### Search

Retrieve detailed information for a single Pokémon by name or ID.

```bash
python src/main.py search [name or ID]
```

**Example:**

```bash
python src/main.py search pikachu
```

### Random

Retrieve details for a randomly selected Pokémon.

```bash
python src/main.py random
```

### Type

Retrieve data on a specific Pokémon type, including its damage relations and a list of Pokémon of that type.

```bash
python src/main.py type [type_name]
```

**Example:**

```bash
python src/main.py type fire
```

## Development

The project is divided into three main modules:

*   `src/api.py`: Handles all network calls to the PokeAPI.
*   `src/data_processor.py`: Transforms raw JSON data into human-readable output.
*   `src/main.py`: Defines the CLI and orchestrates the application.

For more details on the architecture and coding standards, please see `AGENTS.md`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
