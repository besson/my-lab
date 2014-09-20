from mock import MagicMock
from mock import Mock
from pymocha.http_client import HttpClient
from pymocha.url_crawler import UrlCrawler
from unittest import TestCase


class TestUrlCrawler(TestCase):

    def test_invoke_request_with_my_url(self):
        mock_client = HttpClient()
        mock_client.request = MagicMock()
        url = "http://fbesson.wordpress.com"
        # import pdb; pdb.set_trace()
        UrlCrawler(mock_client).is_url_reachable(url)
        mock_client.request.assert_called_with(url)

    def test_url_is_reachable_when_200_ok(self):
        mock_client = HttpClient()
        mock_client.request = Mock(return_value=200)
        status = UrlCrawler(mock_client).is_url_reachable("any url")

        self.assertTrue(status)