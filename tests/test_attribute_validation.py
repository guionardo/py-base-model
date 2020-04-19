from unittest import TestCase
from base_model.attribute_validation import AttributeValidation


class TestAttributeValidation(TestCase):

    def setUp(self) -> None:
        self.att_val = AttributeValidation(None, None, None)

    def test_repr(self):
        self.assertIsNotNone(repr(self.att_val))

    def test_init(self):
        self.assertIsInstance(self.att_val, AttributeValidation)

    def test_set_extra_validation(self):
        self.att_val.set_extra_validations("default=None")
        self.assertIsInstance(self.att_val, AttributeValidation)

    def test_set_default(self):
        self.att_val.set_default(None)
        self.assertIsInstance(self.att_val, AttributeValidation)

    def test_get_default(self):
        self.assertIsNone(self.att_val.get_default(None))
