class UrlCrawler:

    def __init__(self, http_client):
        self.__client = http_client
        self.OK = 200

    def is_url_reachable(self, url):
        return self.__client.request(url) == self.OK
