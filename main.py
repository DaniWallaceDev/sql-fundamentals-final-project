from src.app import insert_json_db, select_db_data

if __name__ == "__main__":

    files: dict = {
        "meter_readings": "meter",
        "mandate_data": "customer",
        "meter_data": "meter"
    }

    insert_json_db("meter_readings", files["meter_readings"], "src")
    insert_json_db("mandate_data", files["mandate_data"], "data/dump")
    insert_json_db("meter_data", files["meter_data"], "data/dump")

    select_db_data("data/dump", files["meter_readings"], "meter_reading_energy_gas", "SELECT * FROM meter_readings WHERE energy_type = 'GAS'")
