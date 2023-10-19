import logging

from app.arg_parser import ArgumentParser
from db import MySQLManager
from export_result.export_result_into_json import JsonConverter
from export_result.export_result_into_xml import XmlConverter
from logger.logger_settings import AppLogging
from my_queries.queries import QUERIES
from settings import my_host, my_user, my_password
from app.application import Application


def main() -> None:
    try:
        AppLogging.setup_logs("app_logging.log")
        dict_args = ArgumentParser.parse_args()
        app = Application(dict_args)
        app.run_app()
    except Exception as ex:
        print(ex)
        logging.error(f'Error {ex}. Close application.', exc_info=False)


if __name__ == '__main__':
    main()
