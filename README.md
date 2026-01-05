# DataForge

CLI tool for automating data cleaning, validation, and reporting.

## Features (v0.1 - Day 1)

✅ CSV row validation
- Column count validation
- Empty cell detection
- Configurable empty cell handling

## Installation
```bash
pip install -e .
```

## Usage
```python
from dataforge.validator import validate_csv_row

# Validate a CSV row
row = ["Alice", "28", "Engineer"]
is_valid, message = validate_csv_row(row, expected_cols=3)

if is_valid:
    print("✅ Row is valid!")
else:
    print(f"❌ Error: {message}")
```

## Testing
```bash
pytest tests/ -v
```

