import unittest
from datetime import datetime

from base_model.base_model import BaseModel
from tests.models.test_model import TestModel


class TestBaseModel(unittest.TestCase):

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

    def test_load(self):
        bm = TestModel()
        mock = {
            "id": 0,
            "name": "Guionardo",
            "date": "2020-03-01",
            "date_time": datetime.now()
        }
        self.assertTrue(bm.load_from_object(mock))

    def test_dict(self):
        mock = {
            "id": 0,
            "name": "Guionardo",
            "date": "2020-03-01",
            "date_time": datetime.now(),
            "names": "abcd"
        }
        bm = TestModel(mock)

        mock['date'] = bm.date
        mock['names'] = bm.names
        mock['guid'] = bm.guid
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
