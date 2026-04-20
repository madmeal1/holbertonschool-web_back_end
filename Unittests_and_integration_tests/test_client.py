#!/usr/bin/env python3
"""Unit tests for client module"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that org returns the correct value"""
        mock_get_json.return_value = {"login": org_name}

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )
        self.assertEqual(result, {"login": org_name})

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the expected URL"""
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}

        with patch.object(
            GithubOrgClient, "org", new_callable=unittest.mock.PropertyMock
        ) as mock_org:
            mock_org.return_value = payload
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the expected list of repos"""
        test_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = test_payload

        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock,
            return_value="https://api.github.com/orgs/google/repos"
        ) as mock_url:
            client = GithubOrgClient("google")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2"])
            mock_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license returns the expected boolean"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)
