import json

def read_json(file_path) -> list:
    with open(file_path, 'r') as file:
        data = json.load(file)

    return data


def values_names_to_insert(column_names)-> str:
    values: str = "(" + ", ".join(column_names) + ")"
    return values


def compare_item_type_conditionals(item: list, file_columns: list)-> tuple:
    table_values: list = []
    for col in file_columns:
        value  = item[col]
        if col == "rejection" or col == "reading_electricity" or col == "reading_gas":
            table_values.append(json.dumps(value))
        else:
            table_values.append(value)
    return tuple(table_values)
