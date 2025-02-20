from typing import List, Dict, Any

# The tests for this file already pass. Your task is to
# rephrease these functions to instead use list/genrator comprehensions.

# run the tests as follows:
#   $ poetry run pytest tests/test_tabular_data.py -x 

# If you do not want to delete the current implementation, just "shadow" the
# functions with new functions with the same name below

# You can run this module (see __main__.py) as follow:
#   $ poetry run python -m techtown2023.tabular_data



# TASK: rephrase this function as a single list expression
# HINT: you have to check every row, as they may vary in size
# HINT: there is a nice builtin function
def determine_n_columns(table) -> int:
    n_columns = 0
    for row in table:
        if len(row) > n_columns:
            n_columns = len(row)
    return n_columns

# TASK: rephrase this function to use list comprehensions
# HINT: start by converting the table to a table of cell sizes
# HINT: Try flattening the table of cell sizes. What if the flattened cells stored both column index and str size?
# HINT: the hints does not hint at a optimal solutoin w.r.t. runtime, but they do hint into some interesting problems to solve ;)
def determine_column_widths(table: List[List[Any]]) -> List[int]:
    column_widths = [-1] * determine_n_columns(table)

    for row in table:
        for i, value in enumerate(row):
            width = len(str(value))
            if width > column_widths[i]:
                column_widths[i] = width

    return column_widths

# TASK: rephrase this function as single list comprehension
# HINT: you may use a "inline if" inside the list comprehension
def format_row(row, column_widths, sep=" "):
    output = []
    for i, (value, col_width) in enumerate(zip(row, column_widths)):
        if i != 0:
            output.append(sep)
        if isinstance(value, int):
            output.append(str(value).rjust(col_width))
        elif isinstance(value, float):
            output.append(str(value).rjust(col_width))
        else:
            output.append(str(value or "").ljust(col_width))
    return "".join(output)



def add_header_separator(table, fillchar="-"):
    "injects a separator row between the table header and body"
    for i, row in enumerate(table):
        if i == 1:
            yield [fillchar * col_width for col_width in determine_column_widths(table)]
        yield row

# TASK: replace the loop with a slicing operation
# HINT: it features a start, stop and step
def reverse_table(table, has_header=False):
    if has_header:
        header, *table = table
    output = []
    for i in range(len(table)-1, -1, -1):
        output.append(table[i])
    if has_header:
        return [header, *output]
    else:
        return output

# TASK: rephrase the for loop in this function as single list comprehension
def format_table(
        table           : List[List[Any]],
        reverse         : bool = False,
        has_header      : bool = False,
        header_fillchar : str  = "-",
        row_start       : str  = "| ",
        row_sep         : str  = " | ",
        row_end         : str  = " |",
        ) -> str:
    column_widths = determine_column_widths(table)
    if reverse:
        table = reverse_table(table, has_header=has_header)
    if has_header:
        table = add_header_separator(table)
    output = []
    for i, row in enumerate(table):
        if i != 0:
            output.append("\n")
        output.append(row_start)
        output.append(format_row(row, column_widths, row_sep))
        output.append(row_end)
    return "".join(output)


# TASK: rephare this using set and dictionary comprehensions
def convert_dicts_to_table(data: List[Dict[str, Any]]) -> List[List[Any]]:
    # SUBTASK: rephrase this into a set comprehension
    keys = set()
    for item in data:
        for key in item.keys():
            keys.add(key)

    #import rich.pretty; rich.pretty.pprint(keys) # uncomment this to debug with printing

    # SUBTASK: rephrase this into a dict comprehension, nesting a list comprehension
    combined = {}
    for key in sorted(keys):
        combined[key] = []
        for item in data:
            combined[key].append( item.get(key, None) )

    #import rich.pretty; rich.pretty.pprint(combined) # uncomment this to debug with printing

    # SUBTASK: rephrase this into a single list literal, using unpacking syntax
    output = []
    output.append(list(combined.keys()))
    for row in zip(*combined.values()):
        output.append(row)

    return output
