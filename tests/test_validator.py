import pytest
from dataforge.validator import validate_csv_row

def test_valid_row_passes():
    

def test_wrong_column_count_fails():

def test_empty_cell_fails_when_not_allowed():

def test_empty_cell_passes_when_allowed():

def test_all_empty_row_fails():
