import pymysql
from pymysql import MySQLError
import logging
from .db_wrapper import DatabaseWrapper


class MySQLWrapper(DatabaseWrapper):
    def connect(self):
        try:
            connection = pymysql.connect(
                host=self.config["hostname"],
                user=self.config["username"],
                password=self.config["password"],
                db=self.config["database"],
                port=int(self.config["port"]),
            )
            logging.info("MySQL connection established!")
            return connection
        except MySQLError as e:
            logging.error(f"Error connecting to the MySQL database: {e}")
            raise e

    def fetch_data(self, query):
        try:
            with self.connect() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(query)
                    return cursor.fetchall()
        except MySQLError as e:
            logging.error(f"Error fetching data: {e}")
            raise e

    def get_all_orders(self):
        query = "SELECT * FROM Orders;"
        return self.fetch_data(query)
