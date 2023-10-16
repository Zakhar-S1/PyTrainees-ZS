import logging

from db import MySQLManager
from export_result.export_result_into_json import JsonConverter
from export_result.export_result_into_xml import XmlConverter
from logger.logger_settings import AppLogging
from my_queries.queries import QUERIES
from settings import my_host, my_user, my_password

# def main() -> None:
#     try:
#         AppLogging.setup_logs()
#         app = Application()
#         app.run_app()
#     except Exception as ex:
#         logging.error(f'Error {ex}. Close application.', exc_info=False)


def run_app() -> None:
    mydb = MySQLManager(host=my_host, user=my_user, password=my_password)

    data_from_db = mydb.execute_select_query(QUERIES)
    # JsonConverter(data_from_db).convert_to_format()
    # XmlConverter(data_from_db).convert_to_format()

    mydb.close_connection()


if __name__ == '__main__':
    run_app()

