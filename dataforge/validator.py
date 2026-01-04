def validate_csv_row(row: list[str], expected_cols: int, allow_empty: bool = False) -> tuple[bool, str]:
    if len(row) != expected_cols:
        return (False, f"Expected {expected_cols} columns, got {len(row)}")
    if not allow_empty:
        for idx, cell in enumerate(row):
            if cell.strip() == "":
                return (False, f"Row contains empty cell at position {idx+1}")
    
    return (True, 'ok')
