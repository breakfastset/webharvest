import time

import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "en-US,en;q=0.9",
    "DNT": "1"
}

url = "https://www.sgcarmart.com/new-cars"

try:

    while True:
        session = requests.Session()
        response = session.get(url, headers=headers)
        print("Can connect")
        time.sleep(10)


except Exception as e:
    print("Error")
    print(e)