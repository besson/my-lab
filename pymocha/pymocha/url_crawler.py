class UrlCrawler:

    def __init__(self, http_client):
        self.__client = http_client

    def run(self, url):
        self.__client.request(url)
