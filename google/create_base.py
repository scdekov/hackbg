from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from connection import *
from Page import Page
scanned_urls = []


def is_outer_url(url, base_url):
    if url.startswith("https://"+base_url) or url.startswith("http://"+base_url) or url.startswith(base_url):
        return False
    return True


def prepare_link(url, href):
    return urljoin(url, href)


def scan_page(url, base_url):

    if url in scanned_urls:
        return

    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html)
    for link in soup.find_all("a"):
        new_link = prepare_link(url, link.get("href"))
        if not is_outer_url(new_link, base_url):
            if soup.title:
                crr_page_title = soup.title.text
            crr_page_url = url
            session.add(Page(url=crr_page_url))
            #crr_page_desc = soup.find("meta", {"name": "description"})['content']
            print(new_link)
            scanned_urls.append(new_link)
            scan_page(new_link, base_url)
    return scanned_urls


scan_page("http://skanev.com/", "skanev.com")
session.commit()
