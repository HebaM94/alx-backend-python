#!/usr/bin/env python3
""" Unit test for client
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock, MagicMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient class"""
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json', return_value={"login": "mocked_org"})
    def test_org(self, org_name, mock_get_json):
        """Test org method"""
        test_class = GithubOrgClient(org_name)
        org = test_class.org
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(org, {"login": "mocked_org"})

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that GithubOrgClient._public_repos_url
        returns the correct URL"""
        mock_org.return_value = {"repos_url":
                                 "https://api.github.com/orgs/google/repos"}
        client = GithubOrgClient("google")

        result = client._public_repos_url

        self.assertEqual(result, "https://api.github.com/orgs/google/repos")

    @patch('client.get_json', return_value=[
        {"name": "repo1"},
        {"name": "repo2"},
        {"name": "repo3"}
    ])
    def test_public_repos(self, mock_get_json):
        """Test that GithubOrgClient.public_repos
        returns the correct list of repos"""
        with patch('client.GithubOrgClient.repos_payload',
                   new_callable=PropertyMock, return_value=[
                    {"name": "repo1"},
                    {"name": "repo2"},
                    {"name": "repo3"}
                    ]) as mock_repos_payload:
            client = GithubOrgClient("google")

            result = client.public_repos()
            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_repos_payload.assert_called_once()
            mock_get_json.assert_not_called()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),  # Case where the repo has no license information
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the `has_license` method of `GithubOrgClient`
        with different inputs"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
