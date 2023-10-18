import logging

from app.arg_parser import ArgumentParser
from db import MySQLManager
from export_result.export_result_into_json import JsonConverter
from export_result.export_result_into_xml import XmlConverter
from logger.logger_settings import AppLogging
from my_queries.queries import QUERIES
from settings import my_host, my_user, my_password


class Application:
    # def __init__(self):
    #     # self.format_file = ArgumentParser.parse_args()
    #     pass
    def __init__(self, dict_args):
        self.dict_args = dict_args


    def run_app(self) -> None:
        # logging.info(f'args{self.dict_args}')

        mydb = MySQLManager(host=my_host, user=my_user, password=my_password)

        data_from_db = mydb.execute_select_query(QUERIES)
        # JsonConverter(data_from_db).convert_to_format()
        XmlConverter(data_from_db).convert_to_format()

        mydb.close_connection()

        # if file_format is not None:
        #     if self.format_file == "json":
        #         export_result_into_json()
        #     if self.format_file = "xml":
        #         export_result_into_xml()
