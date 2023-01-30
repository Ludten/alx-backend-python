#!/usr/bin/env python3
"""
Utils Test Module
"""

import unittest
import utils
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    A class for testing the access nested map
    of utils
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, map, path, expected):
        self.assertEqual(utils.access_nested_map(map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError, "'a'"),
        ({"a": 1}, ("a", "b"), KeyError, "'b'"),
    ])
    def test_access_nested_map_exception(self, map, path, expected, mess):
        with self.assertRaises(expected) as cm:
            utils.access_nested_map(map, path)

        self.assertEqual(str(cm.exception), mess)


if __name__ == '__main__':
    unittest.main()
