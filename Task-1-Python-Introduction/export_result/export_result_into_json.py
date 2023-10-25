import json
import logging

from export_result import ExportResult


class JsonConverter(ExportResult):

    def __init__(self, data_from_queries):
        self.data_for_convert = data_from_queries

    def convert_to_format(self) -> None:
        logging.info('Convert data to json and return it')

        result_list = []
        for list_element in self.data_for_convert:
            result_list.append({tt[0]: tt[1] if len(tt) == 2 else None for tt in list_element})

        # json_str = json.dumps(result_list)
        with open('data/output/Output.json', 'w', encoding='utf-8') as f:
            json.dump(result_list, f, ensure_ascii=False, indent=4)

        # return json_str
