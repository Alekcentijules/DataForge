import csv
from pathlib import Path
from typing import Iterator

def read_csv_file(filepath: str | Path, skip_header: bool = True) -> Iterator[list[str]]:
    with open(filepath, 'r', encoding='utf-8') as file:
        rows = csv.reader(file)

        for row in rows:
            yield row

