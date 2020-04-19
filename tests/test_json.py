import unittest
from base_model.json import loads, dumps


class TestJSON(unittest.TestCase):
    def setUp(self):
        self.json = '{"name":"Guionardo","id":1,"active":true}'
        self.obj = {"name": "Guionardo",
                    "id": 1,
                    "active": True}

    def test_loads(self):
        obj = loads(self.json)
        self.assertDictEqual(obj, self.obj)

    def test_dumps(self):
        json = dumps(self.obj)
        self.assertEqual(self.json, json)
