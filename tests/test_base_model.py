import unittest
from datetime import datetime

from base_model.base_model import BaseModel
from tests.models.test_model import TestModel

from json import dumps

class TestBaseModel(unittest.TestCase):

    def setUp(self) -> None:
        self.mock = mock = {
            "id": 0,
            "name": "Guionardo",
            "date": "2020-03-01",
            "guid":"12345678",
            "date_time": datetime.now(),
            "names": ["abcd"],
            "alarm": "10:20:30"
        }

    def test_attr(self):
        bm = TestModel()
        print(bm._validations)

        self.assertIsInstance(bm, TestModel)

    def test_empty_model(self):
        with self.assertRaises(Exception):
            BaseModel()

    def test_clear(self):
        bm = TestModel()
        bm.clear()

    def test_from_json(self):
        mock = dumps(self.mock,default=str)
        bm = TestModel(mock)
        bm_dict = bm.to_dict()
        mock_dict = self.mock.copy()
        mock_dict['date']=bm.date
        mock_dict['alarm']=bm.alarm
        self.assertDictEqual(mock_dict, bm_dict)

    def test_dict(self):
        mock=self.mock.copy()

        bm = TestModel(mock)

        mock['date'] = bm.date
        mock['names'] = bm.names
        mock['guid'] = bm.guid
        mock["alarm"] = bm.alarm
        bm_dict = bm.to_dict()
        self.assertDictEqual(mock, bm_dict)

    def test_fail_load(self):
        bm = TestModel()
        mock = {
            "name": "Guionardo",
            "date": "2020-02-30",
            "date_time": datetime.now()
        }
        with self.assertRaises(Exception):
            bm.load_from_object(mock)

