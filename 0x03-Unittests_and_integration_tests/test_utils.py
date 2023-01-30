#!/usr/bin/env python3
"""
Utils Test Module
"""

from parameterized import parameterized
import unittest
from unittest import mock
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data):
            self.json_data = json_data

        def json(self):
            return self.json_data

    if args[0] == 'http://example.com':
        return MockResponse({"payload": True})
    elif args[0] == 'http://holberton.io':
        return MockResponse({"payload": False})

    return MockResponse(None)


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
        self.assertEqual(access_nested_map(map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError, "'a'"),
        ({"a": 1}, ("a", "b"), KeyError, "'b'"),
    ])
    def test_access_nested_map_exception(self, map, path, expected, mess):
        with self.assertRaises(expected) as cm:
            access_nested_map(map, path)

        self.assertEqual(str(cm.exception), mess)


class TestGetJson(unittest.TestCase):
    """
    A class for testing the get json of utils
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_json(self, url, expected, mock_get):
        json_data = get_json(url)
        self.assertEqual(json_data, expected)
        mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """
    A class for testing the memoize
    of utils
    """

    def test_memoize(self) -> None:
        """
        Test memoize
        """

        class TestClass:
            """
            Test class
            """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with mock.patch.object(TestClass, "a_method") as mock_foo:
            testclass = TestClass()
            self.assertEqual(testclass.a_property, mock_foo.return_value)
            self.assertEqual(testclass.a_property, mock_foo.return_value)
            mock_foo.assert_called_once()


if __name__ == '__main__':
    unittest.main()
