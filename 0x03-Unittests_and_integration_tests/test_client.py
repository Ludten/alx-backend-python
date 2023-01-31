#!/usr/bin/env python3
"""
Client Test Module
"""

from typing import Dict
from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import MagicMock, PropertyMock, patch


class TestGithubOrgClient(unittest.TestCase):
    """
    A class for testing the GithubOrgClient
    of clients
    """

    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False})
    ])
    @patch("client.get_json")
    def test_org(self, org: str, expected: Dict, mock_foo: MagicMock):
        """
        test org
        """
        mock_foo.return_value = expected
        test = GithubOrgClient(org)
        test.org
        mock_foo.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self):
        """
        test public_repos_url
        """
        with patch.object(
            GithubOrgClient, '_public_repos_url', new_callable=PropertyMock
        ) as mock_off:
            mock_off.return_value = {"org": "abc"}
            test = GithubOrgClient("abc")
            self.assertEqual(test._public_repos_url, mock_off.return_value)

    @patch("client.get_json")
    def test_public_repos(self, mock_json: MagicMock):
        """
        test public_repos method
        """
        mock_json.return_value = [{"name": "google"}, {"name": "abc"}]
        with patch.object(
            GithubOrgClient, '_public_repos_url', new_callable=PropertyMock
        ) as mock_off:
            mock_off.return_value = "https://api.github.com/orgs/{}".format(
                "google")
            test = GithubOrgClient("google")
            self.assertEqual(test.public_repos(), ["google", "abc"])
            mock_off.assert_called_once()
        mock_json.assert_called_once()
