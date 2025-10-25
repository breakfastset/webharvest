from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup
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
    session = requests.Session()
    response = session.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    temp_list = soup.find_all("div", attrs={"class": "styles_textCarDetail__VwrQ2"})
    print(temp_list)

    cars_list = []
    for car in temp_list:
        cars_list.append(car.text)   # saving the text only into the cars_list

    cars_list.sort()    # sort in ascending order
    for i in range(len(cars_list)):
        print(f"{i+1}. {cars_list[i]}")

except Exception as e:
    print("Error")
    print(e)