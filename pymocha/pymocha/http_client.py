import httplib


class HttpClient:

    def request(self, url):
        conn = httplib.HTTPConnection(url)
        conn.request("GET", "/")

        return conn.getresponse().status
