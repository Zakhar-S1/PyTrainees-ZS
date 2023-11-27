import logging

from db import MySQLManager
from export_result.export_result_into_json import JsonConverter
from export_result.export_result_into_xml import XmlConverter
# from logger.logger_settings import AppLogging
from my_queries.queries import QUERIES
from settings import my_host, my_user, my_password, my_db_name, my_port


class Application:

    def __init__(self, dict_args):
        self.dict_args = dict_args

    def run_app(self) -> None:
        logging.info(f'args{self.dict_args}')

        mydb = MySQLManager(
            host=my_host,
            port=my_port,
            user=my_user,
            password=my_password,
            namedb=my_db_name,
            path_for_rooms_file=self.dict_args["path_for_rooms_file"],
            path_for_students_file=self.dict_args["path_for_students_file"]
        )

        # mydb.create_schema()
        # mydb.create_tables()
        # mydb.insert_data_into_rooms_tb()
        # mydb.insert_data_into_students_tb()
        data_from_queries = mydb.execute_select_query(QUERIES)
        # mydb.close_connection()

        if self.dict_args["format_of_export_file"] == "json":
            JsonConverter(data_from_queries=data_from_queries).convert_to_format()
        else:
            XmlConverter(data_from_queries).convert_to_format()
