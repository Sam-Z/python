from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
class HtmlParser(object):
    def __init__(self):
        pass
    def get_new_data(self, page_url,  soup):
        res_data = {}
      
        #url
        res_data['url']   = page_url 
        
        title_node   = soup.find('dd',  class_ = 'lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()
	#lemma-summary
        summary_node         = soup.find('div', class_ = 'lemma-summary')
        res_data['summary']  = summary_node.get_text()
        return res_data

    def get_new_urls(self, page_url, soup):
        new_urls = set() 
        links = soup.find_all('a', href = re.compile(r'/item/.+'))
        for link in links:
            new_url = link['href']
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls


    def parse(self, page_url, html_cont):
        new_urls = set()
        res_data = set()
        
        if page_url is None or html_cont is None:
            return None

        soup = BeautifulSoup(html_cont, "html.parser")

        res_data = self.get_new_data(page_url, soup)
        
        new_urls = self.get_new_urls(page_url, soup)
     #   print (new_urls)
        return new_urls, res_data



        
