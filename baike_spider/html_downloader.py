import urllib

class HtmlDownloader(object):
    def __init__(self):
        pass
    def download(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)
        len = response.getcode()
        if response.getcode() != 200:
            return None

        return response.read()
