#!/usr/bin/env python3
"""
Client Test Module
"""

from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import PropertyMock, patch


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
    def test_org(self, org, expected, mock_foo):
        mock_foo.return_value = expected
        test = GithubOrgClient(org)
        test.org
        mock_foo.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self):
        with patch.object(
            GithubOrgClient, '_public_repos_url', new_callable=PropertyMock
        ) as mock_off:
            mock_off.return_value = {"org": "abc"}
            test = GithubOrgClient("abc")
            self.assertEqual(test._public_repos_url, mock_off.return_value)

    @parameterized.expand([
        ("google", [{"name": "google"}], ["google"]),
        ("abc", [{"name": "abc"}], ["abc"])
    ])
    @patch("client.get_json")
    def test_public_repos(self, org, payload, expected, mock_json):
        mock_json.return_value = payload
        with patch.object(
            GithubOrgClient, '_public_repos_url', new_callable=PropertyMock
        ) as mock_off:
            mock_off.return_value = "https://api.github.com/orgs/{}".format(
                org)
            test = GithubOrgClient(org)
            self.assertEqual(test.public_repos(), expected)
            mock_json.assert_called_once()
            mock_off.assert_called_once()
