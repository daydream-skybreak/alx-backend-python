#!/usr/bin/env python3
"""tests the method utils.access_nested_map"""

import unittest
from typing import Mapping, Sequence, Any, Dict
from unittest.mock import patch, Mock

from parameterized import parameterized
get_json = __import__("utils").get_json
access_nested_map = __import__("utils").access_nested_map
memoize = __import__("utils").memoize


class TestAccessNestedMap(unittest.TestCase):
    """class for testing access_nested_map method"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               key: Sequence, expected: Any) -> None:
        """checks if the function gives the desired output"""
        self.assertEqual(access_nested_map(nested_map, key), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         key: Sequence) -> None:
        """checks whether the function gives the correct errors"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, key)


class TestGetJson(unittest.TestCase):
    """Tests the `get_json` function."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        """Tests `get_json`'s output."""
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests the `memoize` function."""
    def test_memoize(self) -> None:
        """Tests `memoize`'s output."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()


if __name__ == "__main__":
    unittest.main()
