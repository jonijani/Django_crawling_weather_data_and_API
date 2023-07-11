import requests
from bs4 import BeautifulSoup
import json
import json

# "https://www.theweatheroutlook.com/forecast/uk/london"
BASE_URL = "https://www.theweatheroutlook.com/forecast/uk/"


def get_resp(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res
    raise Exception("URL request is not successfull")


def get_td_tags(row: BeautifulSoup, class_name="") -> list:
    if class_name:
        td_list = row.find_all("td", class_=class_name)
    else:
        td_list = row.find_all("td")
    return td_list




def make_dict(row):
    d = {}
    # for row_no in range(1,row_len,3):
    td_tags = get_td_tags(row)
    td_text = td_tags[0].text
    date = td_text[:6]
    month = td_text[8:11]
    temperature = td_tags[2].text.strip()
    # print(date,month,temperature)

    d["date"] = date
    d["month"] = month
    d["temperature"] = temperature
    return d


def add_dict_to_list(url):
    res = get_resp(url)
    soup = BeautifulSoup(res.text, "html.parser")
    table = soup.find("table", class_="table table-condensed")
    rows = table.find_all("tr")
    lweather_list = []
    for row_no in range(1, 25, 3):
        row = rows[row_no]
        td_tags = make_dict(row)
        lweather_list.append(td_tags)
    return lweather_list

def make_url(city):
    #city = input("enter city name :")
    url = f'{BASE_URL}{city}'
    print(url)
    return url

def get_weather_for_city_searched(city):
    url = make_url(city)
    weather_data = add_dict_to_list(url)
    return weather_data

    
    


if __name__ == "__main__":
    #Base_url = f"{BASE_URL}"
    # res = get_resp(url)  # we request url and get responce
    # soup = BeautifulSoup(
    #     res.text, "html.parser"
    # )  # we get bs4 object from response text (html)
    # table = soup.find("table", class_="table table-condensed")

    # print(make_dict(table))
    #print(add_dict_to_list(url))
    #print(make_url('leeds'))
    print(get_weather_for_city_searched('london'))







