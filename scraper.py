import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://discourse.onlinedegree.iitm.ac.in/c/courses/tds-kb/34"

def get_all_threads():
    threads = []
    for page in range(1, 10):  # Adjust if needed
        print(f"Scraping page {page}...")
        url = f"{BASE_URL}?page={page}"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        for link in soup.find_all('a', class_='title raw-link raw-topic-link'):
            href = link.get('href')
            title = link.text.strip()
            full_url = f"https://discourse.onlinedegree.iitm.ac.in{href}"
            threads.append({
                "title": title,
                "url": full_url
            })
    return threads

def save_threads(threads):
    with open("data.json", "w") as f:
        json.dump(threads, f, indent=2)

if __name__ == "__main__":
    threads = get_all_threads()
    save_threads(threads)
