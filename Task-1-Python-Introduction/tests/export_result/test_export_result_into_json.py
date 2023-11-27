from unittest import TestCase, mock
from export_result import JsonConverter


class JsonConverterTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.json_converter = JsonConverter(
            [[[1, 2], [3, 4], [5, 6]]])

    @mock.patch("json.dump")
    def test__convert_to_format__success(self, mock_dump):
        mock_dump.return_value = None
        self.json_converter.convert_to_format()
        mock_dump.assert_called_once_with([{1: 2, 3: 4, 5: 6}], list(mock_dump.call_args.args)[1], ensure_ascii=False, indent=4)
        # self.assertEqual(test_data, '[{"1": 2, "3": 4, "5": 6}]')

