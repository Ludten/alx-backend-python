#!/usr/bin/env python3
"""
Utils Test Module
"""

from typing import Dict, Tuple
from parameterized import parameterized
import unittest
from unittest.mock import MagicMock, patch
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


def mocked_requests_get(*args, **kwargs):
    """
    Mock requests
    """
    class MockResponse:
        """
        Mock Response class
        """

        def __init__(self, json_data):
            self.json_data = json_data

        def json(self):
            """
            Return mock json
            """
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
    def test_access_nested_map(
        self, map: Dict, path: Tuple[str], expected: int
    ):
        """
        test access nested map
        """
        self.assertEqual(access_nested_map(map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError, "'a'"),
        ({"a": 1}, ("a", "b"), KeyError, "'b'"),
    ])
    def test_access_nested_map_exception(
        self, map: Dict, path: Tuple[str],
        expected: Exception, mess: str
    ) -> None:
        """
        test access nested map
        """
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
    @patch('requests.get', side_effect=mocked_requests_get)
    def test_get_json(
        self, url: str, expected: Dict, mock_get: MagicMock
    ) -> None:
        """
        test get json
        """
        json_data = get_json(url)
        self.assertEqual(json_data, expected)
        mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """
    Defines test for memoize utility function
    """

    def test_memoize(self) -> None:
        """
        Test memoize function
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

        with patch.object(TestClass, 'a_method') as mockMethod:
            test = TestClass()
            self.assertEqual(test.a_property, mockMethod.return_value)
            self.assertEqual(test.a_property, mockMethod.return_value)
            mockMethod.assert_called_once()


if __name__ == '__main__':
    unittest.main()
