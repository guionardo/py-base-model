import unittest
from tests.models.list_fields_model import ListFieldsModel


class TestListFieldsModel(unittest.TestCase):

    def setUp(self) -> None:
        self.mock = {
            'names': ['Guionardo', 'Marines'],
            'ages': [1, 30, '90'],
            'enables': [True, False, True]
        }

    def test_values_best_scenario(self):
        bm = ListFieldsModel(self.mock)
        self.assertIsInstance(bm, ListFieldsModel)

    # def test_values_all_string(self):
    #     bm = ListFieldsModel(self.mock_str)
    #     self.assertIsInstance(bm, ListFieldsModel)
    #
    # def test_values_bad_scenario(self):
    #     with self.assertRaises(Exception):
    #         ListFieldsModel(self.mock_error)
