import xml.etree.ElementTree as Et
import logging

from export_result import ExportResult


class XmlConverter(ExportResult):
    def __init__(self, data_from_queries):
        self.data_for_convert = data_from_queries

    def convert_to_format(self) -> None:
        logging.info('Convert data to xml and return it')

        root = Et.Element('Results')
        for item in self.data_for_convert:
            for i in item:
                result_of_query = Et.SubElement(root, 'Result_of_query')
                result_of_query.text = str(i)

        tree = Et.ElementTree(root)
        tree.write("data/output/Output.xml", encoding='utf-8', xml_declaration=True)


