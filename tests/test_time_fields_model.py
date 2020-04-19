import unittest

from tests.models.time_fields_model import TimeFieldsModel
from datetime import date,datetime,time

class TestTimeFieldsModel(unittest.TestCase):

    def setUp(self) -> None:
        self.mock = {
            "birthday": datetime.now().date(),
            "register": datetime.now(),
            "alarm": datetime.now().time()
        }
        self.mock_str = {
            "birthday": str(datetime.now().date()),
            "register": str(datetime.now()),
            "alarm": str(datetime.now().time())
        }

    def test_values_best_scenario(self):
        bm = TimeFieldsModel(self.mock)
        self.assertIsInstance(bm, TimeFieldsModel)

    def test_values_all_string(self):
        bm = TimeFieldsModel(self.mock_str)
        self.assertIsInstance(bm, TimeFieldsModel)