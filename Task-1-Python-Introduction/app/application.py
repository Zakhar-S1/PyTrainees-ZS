import logging

from db import MySQLManager
from export_result.export_result_into_json import JsonConverter
from export_result.export_result_into_xml import XmlConverter
# from logger.logger_settings import AppLogging
from my_queries.queries import QUERIES
from settings import my_host, my_user, my_password


class Application:

    def __init__(self, dict_args):
        self.dict_args = dict_args

    def run_app(self) -> None:
        logging.info(f'args{self.dict_args}')

        mydb = MySQLManager(
            host=my_host,
            user=my_user,
            password=my_password,
            path_for_rooms_file=self.dict_args["path_for_rooms_file"],
            path_for_students_file=self.dict_args["path_for_students_file"]
        )

        data_from_db = mydb.execute_select_query(QUERIES)
        mydb.close_connection()

        if self.dict_args["format_of_export_file"] == "json":
            JsonConverter(data_from_db).convert_to_format()
        else:
            XmlConverter(data_from_db).convert_to_format()
