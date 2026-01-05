import pytest
from pathlib import Path
from dataforge.csv_reader import (
    read_csv_file,
    detected_delimiter,
    count_csv_rows,
    read_csv_with_validation
)

FIXTURES_DIR = Path(__file__).parent / 'fixtures'

class TestReadCsvFile:
    def test_read_valid_csv(self):
        filepath = FIXTURES_DIR / 'valid_data.csv'
        rows = list(read_csv_file(filepath))

        assert len(rows) == 4
        assert rows[0] == ['name', 'age', 'job']
        assert rows[1] == ['Alice', '28', 'Engineer']
    
    def test_read_csv_skip_header(self):
        filepath = FIXTURES_DIR / 'valid_data.csv'
        rows = list(read_csv_file(filepath))

        assert len(rows) == 3
        assert rows[0] == ['Alice', '28', 'Engineer']
        assert 'name' not in rows[0]

    def test_read_nonexistent_file(self):
        with pytest.raises(FileNotFoundError):
            list(read_csv_file('nonexistent.csv'))

    def test_read_empty_file(self):
        filepath = FIXTURES_DIR / 'empty_file.csv'
        rows = list(read_csv_file(filepath))

        assert rows == []

    def test_read_with_custom_delimiter(self):
        filepath = FIXTURES_DIR / 'semicolon_data.csv'
        rows = list(read_csv_file(filepath))

        assert len(rows) == 3
        assert rows[1] == ['Alice', '28', 'Engineer']

class TestDetectDelimiter:
    def test_detect_comma_delimiter(self):
        filepath = FIXTURES_DIR / 'valid_data.csv'
        delimiter = detected_delimiter(filepath)

        assert delimiter == ','

    def test_detect_semicolon_delimiter(self):
        filepath = FIXTURES_DIR / 'semicolon_data.csv'
        delimiter = detected_delimiter(filepath)

        assert delimiter == ';'

class TestCountCsvRows:
    def test_count_rows_with_header(self):
        filepath = FIXTURES_DIR / 'valid_data.csv'
        count = count_csv_rows(filepath, skip_header=False)

        assert count == 4

    def test_count_rows_without_header(self):
        filepath = FIXTURES_DIR / 'valid_data.csv'
        count = count_csv_rows(filepath, skip_header=True)

        assert count == 3

    def test_count_empty_file(self):
        filepath = FIXTURES_DIR / 'empty_file.csv'
        count = count_csv_rows(filepath)

        assert count == 0

class TestReadCsvWithValidation:
    def test_validation_with_valid_file(self):
        filepath = FIXTURES_DIR / 'valid_data.csv'
        valid_rows, errors = read_csv_with_validation(filepath, expected_cols=3, skip_header=True)

        assert len(valid_rows) == 3
        assert len(errors) == 0

    def test_validation_with_invalid_file(self):
        filepath = FIXTURES_DIR / 'invalid_data.csv'
        valid_rows, errors = read_csv_with_validation(filepath, expected_cols=3, skip_header=True)

        assert len(valid_rows) == 0
        assert len(errors) == 3

        row_nums = [err[0] for err in errors]
        assert 1 in row_nums
        assert 2 in row_nums
        assert 3 in row_nums

    def test_validation_allows_empty_when_configured(self):
        filepath = FIXTURES_DIR / 'invalid_data.csv'
        valid_rows, errors = read_csv_with_validation(filepath, expected_cols=3, skip_header=True, allow_empty=True)

        assert len(valid_rows) == 1
        assert valid_rows[0] == ['Bob', '', 'Designer']