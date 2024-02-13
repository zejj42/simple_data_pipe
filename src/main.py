import csv
import os
import configparser
import logging
from .db.db_factory import connect_to_database
from .storage.storage_factory import get_storage_service


DB_TYPE = "mysql"
STORAGE_TYPE = "S3"
OUTPUT_FILE_DIR = "data"
OUTPUT_FILE_NAME = "orders_extract.csv"
CONFIG_DIR = "config"
CONFIG_FILE_NAME = "pipeline.conf"

logging.basicConfig(level=logging.INFO)


def read_config(config_directory, filename):
    parser = configparser.ConfigParser()
    config_path = os.path.join(config_directory, filename)
    parser.read(config_path)
    return parser


def write_to_csv(data, output_directory, file_name, delimiter="|"):
    os.makedirs(output_directory, exist_ok=True)
    file_path = os.path.join(output_directory, file_name)
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerows(data)
    logging.info(f"Data written to {file_path}")


if __name__ == "__main__":
    config = read_config(CONFIG_DIR, CONFIG_FILE_NAME)

    db_config = {
        key: config.get("db_config", key)
        for key in ["hostname", "port", "username", "database", "password"]
    }

    storage_config = {
        key: config.get("storage_credentials", key)
        for key in ["access_key", "secret_key", "bucket"]
    }

    try:
        db = connect_to_database(DB_TYPE, db_config)
        data = db.get_all_orders()
        write_to_csv(data, OUTPUT_FILE_DIR, OUTPUT_FILE_NAME)

        storage = get_storage_service(STORAGE_TYPE, storage_config)
        full_file_path = os.path.join(OUTPUT_FILE_DIR, OUTPUT_FILE_NAME)
        storage.upload_file(full_file_path, storage_config["bucket"])

    except Exception as e:
        logging.error(f"An error occurred: {e}")
