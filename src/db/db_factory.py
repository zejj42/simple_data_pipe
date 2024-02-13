from .mysql_wrapper import MySQLWrapper


def connect_to_database(db_type, config):
    if db_type == "mysql":
        return MySQLWrapper(config)
    else:
        raise ValueError(f"Unsupported database type: {db_type}")
