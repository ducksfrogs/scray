import re
import time
from typing import Iterator
import requests
import lxml.html

from pymongo import MongoClient

def main():
    client = MongoClient('localhost', 27017)
    collection = client.scraping.ebooks
    collection.create_index('key', unique=True)

    session = requests.Session()
    response = session.get('hppts://gihyo.jp/dp')



def scrape_list_page(response, requests.Response) -> Iterator[str]:
    html = lxml.html.fromstring(response.text)
    html.make_links_absolute(response.url)

    for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
        url = a.get('href')
        yield url

def scrape_detail_page(response: requests.Response) -> dict:
    html = lxml.html.fromstring(response.text)
    ebook = {
        'url': response.url,
        'key': extract_key(response.url)

        'title': html.cssselect('#bookTitle')[0],
        'price':
    }
