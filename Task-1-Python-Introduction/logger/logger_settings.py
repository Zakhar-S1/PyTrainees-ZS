import os
import logging


class AppLogging:
    @staticmethod
    def setup_logs(file_path) -> None:
        logging.basicConfig(
            filename=file_path,
            filemode="a",
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.DEBUG
        )

    @staticmethod
    def log_setup() -> None:
        file_path = "app_logging.log"

        with open("app_logging.log", "w") as wf:
            AppLogging.setup_logs(file_path)

    @staticmethod
    def show_logs() -> str:
        with open("app_logging.log", "r") as rf:
            logging.info("Show logs")
            return "Logs:\n" + "".join([line for line in rf])
