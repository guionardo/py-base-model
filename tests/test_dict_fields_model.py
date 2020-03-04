import unittest

from tests.models.dict_fields_model import DictFieldsModel


class TestListFieldsModel(unittest.TestCase):

    def setUp(self) -> None:
        self.mock = {
            'names': {'Guionardo': 'Marines'},
            'ages': {'a': 1, 'b': 30, 'c': 90},
            'enables': {'a': True, 'b': False, 'c': True}
        }

    def test_values_best_scenario(self):
        bm = DictFieldsModel(self.mock)
        self.assertIsInstance(bm, DictFieldsModel)

    # def test_values_all_string(self):
    #     bm = ListFieldsModel(self.mock_str)
    #     self.assertIsInstance(bm, ListFieldsModel)
    #
    # def test_values_bad_scenario(self):
    #     with self.assertRaises(Exception):
    #         ListFieldsModel(self.mock_error)
