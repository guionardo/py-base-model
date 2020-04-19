import unittest

from tests.models.test_model_parent import ChildModel, ParentModel


class TestParentModel(unittest.TestCase):

    def test_parent_child(self):
        mock = {
            "id": 1,
            "name": "PARENT",
            "child": {
                "id": 2,
                "name": "CHILD",
                "children": [
                    {"id": 3, "age": 4.5}
                ]
            },
            "date_creation": "2020-03-02 00:00:00"
        }

        pm = ParentModel(mock)

        self.assertIsNotNone(pm)

    def test_child(self):
        cm = ChildModel()

        self.assertIsNotNone(cm)
