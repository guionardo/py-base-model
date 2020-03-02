import unittest

from tests.models.test_model_parent import ParentModel, ChildModel


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
            }
        }

        pm = ParentModel(mock)

        self.assertIsNotNone(pm)

    def test_child(self):
        mock = {"id": 1, "name": "child"}
        cm = ChildModel()

        self.assertIsNotNone(cm)
