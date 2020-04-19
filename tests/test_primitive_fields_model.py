import unittest

from tests.models.primitive_fields_model import PrimitiveFieldsModel


class TestPrimitiveFieldsModel(unittest.TestCase):

    def setUp(self) -> None:
        self.mock = {
            "id": 1,
            "name": "Guionardo",
            "active": True,
            "size": 3.1415
        }
        self.mock_str = {
            "id": "1",
            "name": "Guionardo",
            "active": "True",
            "size": "3.1415"
        }
        self.mock_error = {
            "id": "a1",
            "name": "Guionardo",
            "active": "True",
            "size": "3,1415"
        }

    def test_values_best_scenario(self):
        bm = PrimitiveFieldsModel(self.mock)
        self.assertIsInstance(bm, PrimitiveFieldsModel)

    def test_values_all_string(self):
        bm = PrimitiveFieldsModel(self.mock_str)
        self.assertIsInstance(bm, PrimitiveFieldsModel)

    def test_values_bad_scenario(self):
        with self.assertRaises(Exception):
            PrimitiveFieldsModel(self.mock_error)
