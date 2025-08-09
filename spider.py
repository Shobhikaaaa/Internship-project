import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://www.fairmont.com"

to_visit = set([base_url])
visited = set()

def get_all_link(url):
    print(url)
    links = set()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/115.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    for a_tag in soup.find_all('a', href=True):
        full_url = urljoin(url, a_tag['href'])
        if full_url.startswith(base_url): 
            links.add(full_url)    
    return links


if __name__ == "__main__":
    while to_visit:
        popped_url = to_visit.pop()
        if popped_url in visited:
            continue
        links = get_all_link(popped_url)
        visited.add(popped_url)
        to_visit.update(links - visited)
        time.sleep(1)   
    
    print("Crawled endpoints:")
    for i in visited:
        print(i)
    print("\ntotal endpoint crawled: ", len(visited))