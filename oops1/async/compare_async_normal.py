import requests
import time

urls = [
    "https://httpbin.org/delay/1",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/3",
]


def fetch_url(url):
    response = requests.get(url)
    return response.text


start_time = time.time()

for url in urls:
    data = fetch_url(url)
    print(f"Fetched data from {url}")

end_time = time.time()
print(f"Total time taken: {end_time - start_time} seconds")
