import unittest

from base_model.tools import get_class_name, parse_quotes


class TestTools(unittest.TestCase):

    def test_parse_quotes(self):
        test = 'default="WITH SPACES" another_argument'
        test_list = parse_quotes(test)
        self.assertEqual(len(test_list), 2)

    def test_get_class_name(self):
        class_name = get_class_name(self.__class__)
        self.assertTrue(class_name.endswith('test_tools.TestTools'))
