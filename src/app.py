import psycopg, json
from psycopg.rows import dict_row

from .utils import values_names_to_insert, compare_item_type_conditionals, read_json, path_creator

def insert_json_db(file_name: str, file_dir: str, dir_path:str):
    # Feature, add a function to check if table exist in db, if not exit create a db
    file_path: str = f"{dir_path}/{file_dir}/{file_name}.json"
    print(f"Path successfully created: {file_path}")
    try:
        file: list = read_json(file_path)
    except Exception as e:
        print("Error leyendo el archivo como texto:", e)
        return

    file_columns: list = list(set(file[0].keys()))
    column_names: str = values_names_to_insert(file_columns)
    placeholders: str = ", ".join(["%s"] * len(file_columns))
    insert_into_table_columns: str = f"INSERT INTO {file_name} {column_names} VALUES ({placeholders})"
    for item in file:
        table_values: tuple = compare_item_type_conditionals(item, file_columns)
        with psycopg.connect("dbname=postgres host=localhost password=1234 user=postgres") as conn:
            with conn.cursor() as cur:
                cur.execute(insert_into_table_columns, table_values)

    print(f"Insert data into table {file_name} finished.")

    return


def select_db_data(dir_path: str, file_dir: str, file_name_to_create: str, select_query: str):
    with psycopg.connect("dbname=postgres host=localhost password=1234 user=postgres") as conn:
        with conn.cursor(row_factory = dict_row) as cur:
            cur.execute(select_query)
            data = cur.fetchall()
    with open(f"{dir_path}/{file_dir}/{file_name_to_create}.json", "x") as my_file:
        my_file.write(json.dumps(data,indent=4, default=str))
    return
