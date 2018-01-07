#!/usr/bin/python
#coding:utf8
import urllib.request
import html_downloader, html_outputer, html_parser, spider_main, url_manager

from bs4 import BeautifulSoup

class SpiderMain(object):
    def __init__(self):
        self.urls       = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser     = html_parser.HtmlParser()
        self.outputer   = html_outputer.HtmlOutputer()
        
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url             = self.urls.get_new_url()
                print("%d %s"%(count, new_url))
                html_cont           = self.downloader.download(new_url)
                new_urls, new_data  = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 10:
                    break 
                count = count + 1
            except:
                print ("carw failed %s"%new_url)

        self.outputer.html_output()
        
if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313?fr=aladdin"
    spider_main = SpiderMain()
    spider_main.craw(root_url)
'''
    response = urllib.request.urlopen(root_url)
    root_page = response.read()
    print (root_page.decode('utf-8'))
    soup = BeautifulSoup(root_page)
    print(soup.prettify())
'''   
