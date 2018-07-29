import urllib


class Downloader():
    '''
    Class to retrieve HTML code
    and binary files from a
    specified website
    '''

    def __init__(self, url):
        self.url = url
        self.contents = ''

    def download(self):
        browser = urllib.urlopen(self.url)
        response = browser.getcode()
        if response == 200:
            self.contents = browser.read()
