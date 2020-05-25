from keys import weather_key, state, city
import requests

resp = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q={city},{state}&units=imperial&appid={weather_key}')

print(resp.json()["list"][1]["main"]["temp"]) # temp
print(resp.json()["list"][1]["weather"][0]["main"]) # clouds
print(resp.json()["list"][1]["wind"]["speed"]) # wind

for data_point in resp.json()["list"]:
    print(data_point["main"]["temp"]) # temp
    print(data_point["weather"][0]["main"]) # clouds
    print(data_point["wind"]["speed"]) # wind