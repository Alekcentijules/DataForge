import csv
from pathlib import Path
from typing import Iterator

def read_csv_file(filepath: str | Path, skip_header: bool = False, delimiter: str = ',', encoding: str = 'utf-8') -> Iterator[list[str]]:
    filepath = Path(filepath)

    if not filepath.exists():
        raise FileNotFoundError(f"File not found: {filepath}")

    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=delimiter, skipinitialspace=True)

        if skip_header:
            next(reader, None)

        for row in reader:
            yield row


def detected_delimiter(filepath: str | Path, sample_size: int = 5) -> str:
    filepath = Path(filepath)

    with open(filepath, 'r', encoding='utf-8', newline='') as file:
        sample = ''.join([file.readline() for _ in range(sample_size)])

    try:
        sniffer = csv.Sniffer()
        delimiter = sniffer.sniff(sample).delimiter
        return delimiter
    except csv.Error:
        delimiters = [',', ';', '\t', '|']
        counts = {d: sample.count(d) for d in delimiters}
        return max(counts, key=counts.get)
    
def count_csv_rows(filepath: str | Path, skip_header: bool = False) -> int:
    count = sum(1 for _ in read_csv_file(filepath, skip_header=skip_header))
    return count

def read_csv_with_validation(filepath: str | Path, expected_cols: int, skip_header: bool = False, allow_empty: bool = False) -> tuple[list[list[str]], list[tuple[int, str]]]:
    from dataforge.validator import validate_csv_row

    valid_rows = []
    errors = []

    rows = list(read_csv_file(filepath, skip_header=skip_header))

    for row_num, row in enumerate(rows, start=1):
        is_valid, error_msg = validate_csv_row(row, expected_cols, allow_empty)

        if not is_valid:
            errors.append((row, error_msg))
        else:
            valid_rows.append(row)
        
    if errors:
        if allow_empty:
            valid_rows = [
                row for row in valid_rows
                if any(cell.strip() == '' for cell in row)
            ]
        else:
            valid_rows = []
    
    return valid_rows, errors