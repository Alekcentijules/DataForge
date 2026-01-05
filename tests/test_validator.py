import pytest
from dataforge.validator import validate_csv_row

def test_valid_row_passes():
    row = ['Alice', '22', 'Engineer']
    expected_cols = 3

    is_valid, message = validate_csv_row(row, expected_cols)

    assert is_valid is True, 'Valid row should pass validation'
    assert message == 'OK', f"Expected 'OK', got '{message}'"

def test_wrong_column_count_fails():
    row = ['Bob', '31']
    expected_cols = 3

    is_valid, message = validate_csv_row(row, expected_cols)

    assert is_valid is False, 'Row with wrong column count should fail'
    assert '3' in message, 'Error message should mention expented columns'
    assert '2' in message, 'Error message should mention actual columns'

def test_empty_cell_fails_when_not_allowed():
    row = ['Roberto', '', 'Designer']
    expected_cols = 3

    is_valid, message = validate_csv_row(row, expected_cols)

    assert is_valid is False, 'Empty cell should fail when not allowed'
    assert 'empty' in message.lower(), 'Error should mention empty cell'

def test_empty_cell_passes_when_allowed():
    row = ['Joker', '', 'Manager']
    expected_cols = 3

    is_valid, message = validate_csv_row(row, expected_cols, allow_empty=True)

    assert is_valid is True, 'Empty cell should pass when allowed'
    assert message == 'OK'

def test_all_empty_row_fails():
    row = ['', '', '']
    expected_cols = 3

    is_valid, message = validate_csv_row(row, expected_cols)

    assert is_valid is False, 'All-empty row should fail'
    assert 'empty' in message.lower()

def test_row_with_spaces_only():
    row = ['Neo', '    ', 'ChosenOne']
    expected_cols = 3

    is_valid, message = validate_csv_row(row, expected_cols)

    assert is_valid is False
    assert 'empty' in message.lower()

def test_zero_columns():
    row = []
    expected_cols = 0

    is_valid, message = validate_csv_row(row, expected_cols)

    assert is_valid is True

def test_validator_with_unicode():
    row = ['Johny', '👨‍💻', 'Developer']
    expected_cols = 3

    is_valid, message = validate_csv_row(row, expected_cols)

    assert is_valid is True

def test_validator_with_very_long_string():
    long_text = 'A' * 1000
    row = [long_text, 'test', 'data']
    expected_cols = 3

    is_valid, message = validate_csv_row(row, expected_cols)

    assert is_valid is True