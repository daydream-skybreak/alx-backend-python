#!/usr/bin/env python3
"""tests the method utils.access_nested_map"""

import unittest
from typing import Mapping, Sequence, Any

from parameterized import parameterized

get_json = __import__("utils").get_json
access_nested_map = __import__("utils").access_nested_map


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


if __name__ == "__main__":
    unittest.main()
