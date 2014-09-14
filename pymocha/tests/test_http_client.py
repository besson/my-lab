from mock import MagicMock
from pymocha.http_client import HttpClient
from pymocha.url_crawler import UrlCrawler


class TestUrlCrawler:

    def test_invoke_request_with_my_url(self):
        mock_client = HttpClient()
        mock_client.request = MagicMock()
        url = "http://fbesson.wordpress.com"
        UrlCrawler(mock_client).run(url)
        mock_client.request.assert_called_with(url)