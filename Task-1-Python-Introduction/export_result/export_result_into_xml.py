import xml.etree.ElementTree as ET
import logging

from export_result import ExportResult


class XmlConverter(ExportResult):
    def __init__(self, data_from_queries):
        self.data_for_convert = data_from_queries

    def convert_to_format(self) -> None:
        logging.info('Convert data to xml and return it')

        root = ET.Element('Results')
        for item in self.data_for_convert:
            for i in item:
                result_of_query = ET.SubElement(root, 'Result_of_query')
                result_of_query.text = str(i)

        tree = ET.ElementTree(root)
        tree.write("data/output/Output.xml", encoding='utf-8', xml_declaration=True)


