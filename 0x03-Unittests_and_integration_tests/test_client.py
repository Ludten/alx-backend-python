#!/usr/bin/env python3
"""
Client Test Module
"""

import json
from urllib.error import HTTPError
from fixtures import TEST_PAYLOAD
from typing import Dict
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import MagicMock, Mock, PropertyMock, patch


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, lic, key, expected):
        """
        test has_license method
        """
        test = GithubOrgClient("google")
        self.assertEqual(test.has_license(lic, key), expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(TEST_PAYLOAD[0][0],
      TEST_PAYLOAD[0][1],
      TEST_PAYLOAD[0][2],
      TEST_PAYLOAD[0][3])]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    A class for testing the integration GithubOrgClient
    of clients
    """

    @classmethod
    def setUp(cls) -> None:
        """
        setup test
        """
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def mocked_requests_get(url: str):
            """
            Mock request
            """
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch(
            'requests.get', side_effect=mocked_requests_get)
        cls.mock_object = cls.get_patcher.start()

    def test_public_repos(self):
        """
        test public repos
        """
        test = GithubOrgClient("google")
        self.assertEqual(
            test.public_repos(),
            self.expected_repos
        )

    def test_public_repos_with_license(self):
        """
        test public repos with license
        """
        test = GithubOrgClient("google")
        self.assertEqual(
            test.public_repos(license="apache-2.0"),
            self.apache2_repos
        )

    @classmethod
    def tearDown(cls) -> None:
        """
        teardown test
        """
        cls.get_patcher.stop()
