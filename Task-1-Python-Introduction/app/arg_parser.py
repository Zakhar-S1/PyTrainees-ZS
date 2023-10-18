# import logging
from typing import Dict, Any
import argparse


class ArgumentParser:

    @staticmethod
    def parse_args() -> Dict[str, Any]:

        parser = ErrorCatchingArgumentParser()
        parser.add_argument(
            '--path_for_rooms_file',
            help='path for rooms file',
            type=str
        )
        parser = ErrorCatchingArgumentParser()
        parser.add_argument(
            '--path_for_students_file',
            help='path for students file',
            type=str
        )
        parser.add_argument(
            '--format_of_export_file',
            help='format for exporting file in output dir',
            type=str
        )

        return vars(parser.parse_args())


class ArgParserError(Exception):

    def __init__(self, message):
        self.message = message


class ErrorCatchingArgumentParser(argparse.ArgumentParser):

    def error(self, message) -> None:

        raise ArgParserError('Error')
