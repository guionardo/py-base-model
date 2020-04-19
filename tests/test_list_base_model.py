import unittest
from base_model.list_base_model import ListBaseModel
from tests.models.list_fields_model import ListSubModelModel
from tests.models.primitive_fields_model import PrimitiveFieldsModel


class TestListBaseModel(unittest.TestCase):

    def test_list(self):
        test_case = '''[
{"id":1,"name":"name 1","active":true,"size":0.0},
{"id":2,"name":"name 2","active":false,"size":1.5},
{"id":3,"name":"name 3","active":true,"size":-10.0}
]'''
        lbm = ListBaseModel(PrimitiveFieldsModel, test_case)
        self.assertEqual(len(lbm), 3)

    def test_sub_model_list(self):
        test_case = '''{
    "id":1,
    "submodels": [
{"id":1,"name":"name 1","active":true,"size":0.0},
{"id":2,"name":"name 2","active":false,"size":1.5},
{"id":3,"name":"name 3","active":true,"size":-10.0}
]
}'''
        lsm = ListSubModelModel(test_case)
        self.assertEqual(len(lsm.submodels), 3)
