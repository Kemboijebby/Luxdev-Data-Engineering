import threading
import requests

def download_page(link):
    response = requests.get(link)
    if response.status_code == 200:
        print(f"Downloaded: {link} (Size: {len(response.text)} chars)")
    else:
        print(f"Failed to download: {link} (Status: {response.status_code})")

links = [
    "https://example.com",
    "https://www.python.org",
    "https://httpbin.org/get"
]

threads = []

for link in links:
    thread = threading.Thread(target=download_page, args=(link,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
