# import logging
# from typing import Dict, Any
# import argparse


# class ArgumentParser:
#
#     @staticmethod
#     def parse_args() -> Dict[str, Any]:
#
#         parser = ErrorCatchingArgumentParser()
#         parser.add_argument()
#
# class ArgParserError(Exception):
#
#     def __init__(self, message):
#         self.message = message
#
#
# class ErrorCatchingArgumentParser(argparse.ArgumentParser):
#
#     def error(self, message) -> None:
#
#         raise ArgParserError('Error')
