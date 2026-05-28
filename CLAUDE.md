## Development Setup

```bash
# Create a virtual environment if one doesn't exist
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install the package with dev dependencies into the local virtual environment
pip install -e ".[dev]"

# Install pre-commit hooks (runs black on commit)
pre-commit install
```

All commands below assume the virtual environment is activated. Use
`.venv/bin/pytest`, `.venv/bin/mypy`, etc. if running without activating.

## Common Commands

```bash
# Run all tests
.venv/bin/pytest

# Run a single test function
.venv/bin/pytest tests/test_fsize_init.py::test_byte

# Run tests with coverage
.venv/bin/pytest --cov=fsize

# Type checking
.venv/bin/mypy .

# Linting
.venv/bin/pylint .

# Format code (max line length: 80)
.venv/bin/black .
```

## Architecture

The entire library lives in `src/fsize/__init__.py`. There are no submodules.

**`FSize(value, units="B")`** — The constructor (`__new__`) converts the input
to bytes and stores the base-10 or base-2 conversion factor (`__convert__` —
either 1000 or 1024) on the instance. The internal representation is always
bytes.

- Accepts a numeric value or a string like `"1.5 GiB"`.
- `units` determines whether the `__convert__` factor is 1024 (binary: `KiB`,
  `MiB`…, or plain `B`) or 1000 (decimal: `KB`, `MB`…).
- Once constructed, the conversion direction (binary vs. decimal) is fixed by
  `__convert__`.

**`__format__(format_spec)`** — Implements the custom format mini-language:
```
[fill][align][width][grouping][unit][i][B]
```
where `unit` is one of `K M G T P E`. The `i` and trailing `B` are accepted but
ignored — the actual binary/decimal choice comes from `__convert__` set at
construction time.

**Conversion methods**: `to_bytes()`, `to_k()`, `to_m()`, `to_g()`, `to_t()`,
`to_p()`, `to_e()` — each divides `self.real` by the appropriate power of
`__convert__`.

## Code Style

- Line length: 80 characters (enforced by `black` and `pylint`).
- Follows Google Python Style Guide (`.pylintrc` is based on Google's canonical
  config).
- All public methods require docstrings (minimum 12 characters for
  functions/classes).
- Naming: `snake_case` for functions/variables/arguments, `PascalCase` for
  classes.

## Pre-Commit Requirements

**All of the following must pass before committing any change:**

```bash
.venv/bin/pytest        # all tests must pass
.venv/bin/mypy .        # no type errors
.venv/bin/pylint .      # no lint errors
```

These mirror the three GitHub Actions CI workflows (`.github/workflows/pytest.yml`,
`mypy.yml`, `pylint.yml`) that run on every push against Python 3.11, 3.12, and
3.13. A commit that breaks any of these checks must not be pushed.

## Testing

Tests live in `tests/test_fsize_init.py`. The package is installed in
`importlib` mode with `src/` on the Python path (configured in `pyproject.toml`
under `[tool.pytest.ini_options]`).

CI runs pytest, mypy, and pylint against Python 3.11, 3.12, and 3.13 on every
push.

## Package Configuration

- Version is sourced dynamically from `fsize.__version__` (currently `"0.1.0"`).
- Build system: `setuptools`.
- Requires Python ≥ 3.11 (uses `typing.Self`).
