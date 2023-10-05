import json
from typing import List

from export_result import ExportResult


class JsonConverter(ExportResult):

    def __init__(self, data_from_queries):
        self.data_for_convert = data_from_queries  # ==[[(),...,()], [(),...,()], [(),...,()], [(),...,()]]

    def convert_to_format(self) -> str:
        result_list = []
        for list_element in self.data_for_convert:
            result_list.append({tt[0]: tt[1] if len(tt) == 2 else None for tt in list_element})

        json_str = json.dumps(result_list)

        return json_str
