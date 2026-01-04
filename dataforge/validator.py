def validate_csv_row(row: list[str], expected_cols: int, allow_empty: bool = False) -> tuple[bool, str]:
    if len(row) != expected_cols:
        return (False, 'The number of columns does not match the required value.')
    if allow_empty != False:
        return (False, 'There are empty cells in the columns.')
    
    return (True, 'ok')