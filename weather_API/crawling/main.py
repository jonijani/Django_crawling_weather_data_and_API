
import requests
from bs4 import BeautifulSoup
import json
from typing import List, Optional
from pydantic import BaseModel



# "https://www.theweatheroutlook.com/forecast/uk/london"
BASE_URL = "https://www.theweatheroutlook.com/forecast/uk/"

# need to to import pydantic and Optional
class WeatherData(BaseModel):  # pydantic model
    date: str=''
    month: str=''
    temperature: str=''
    winds : str=''
    humidity : str=''
    rain : str=''


class WeatherDataList(BaseModel):
    td_list : List[WeatherData]=[]

    

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


# made pydantic class 
def make_data_dict(row):
    WeatherData_pydantic = WeatherData() 

    td_tags = get_td_tags(row)
    td_text = td_tags[0].text
    date = td_text[:6]
    month = td_text[8:11]
    temperature = td_tags[2].text.strip()
    winds = td_tags[4].text.strip()
    humidity = td_tags[6].text.strip()
    rain = td_tags[8].text.strip()

    WeatherData_pydantic.date =  date
    WeatherData_pydantic.month =  month
    WeatherData_pydantic.temperature =  temperature
    WeatherData_pydantic.winds =  winds
    WeatherData_pydantic.humidity =  humidity
    WeatherData_pydantic.rain =  rain

    #return WeatherData_pydantic 
    return WeatherData_pydantic

# def make_data_dict(row):
    
#     d = {}
#     # for row_no in range(1,row_len,3):
#     td_tags = get_td_tags(row)
#     td_text = td_tags[0].text
#     date = td_text[:6]
#     month = td_text[8:11]
#     temperature = td_tags[2].text.strip()
#     winds = td_tags[4].text.strip()
#     humidity = td_tags[6].text.strip()
#     rain = td_tags[8].text.strip()
#     # print(date,month,temperature)  6 , 8

#     d["date"] = date
#     d["month"] = month
#     d["temperature"] = temperature
#     d['winds'] = winds
#     d['humidity'] = humidity
#     d['rain'] = rain

#     return d


def add_dict_to_list(url):
    res = get_resp(url)
    soup = BeautifulSoup(res.text, "html.parser")
    table = soup.find("table", class_="table table-condensed")
    rows = table.find_all("tr")
    weather_pydantic_list = WeatherDataList()
    for tr_tag in rows:
        tag_id = tr_tag.get('id')
        if (not tag_id) or 'trd' in tag_id :

            continue


        pydantic_td_tags = make_data_dict(tr_tag)
        weather_pydantic_list.td_list.append(pydantic_td_tags)
    return weather_pydantic_list.json()
    

    
    # for row_no in range(1, 25, 3):
    #     td_tags = make_dict(rows[row_no])
    #     lweather_list.append(td_tags)
    # return lweather_list

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
   
    print(get_weather_for_city_searched('dublin'))



''' 'day':monday , 'temp':25, 'date':'12july2023','description':'abcxzsds', 
'day':monday , 'temp':25, 'date':'12july2023','description':'abcxzsds', '''




