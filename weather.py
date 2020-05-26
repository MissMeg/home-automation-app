from keys import weather_key, state, city
from datetime import date, datetime, timedelta, time
import requests


class Weather():
    def __init__(self):
        self.today = {}
        self.tomorrow = {}
        self.day_p2 = {}
        self.day_p3 = {}
        self.date = date.today()
        self.time = time(15, 0, 0, 0)

    def get_data(self, key, city, state):
        resp = requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q={city},{state}&units=imperial&appid={key}')
        return self.organize_data(resp.json()["list"])

    def organize_data(self, data):
        for data_point in data:
            converted = datetime.strptime(data_point['dt_txt'], '%Y-%m-%d %H:%M:%S')
            date = converted.date()
            time = converted.time()
            if time == self.time:
                if date == self.date:
                    self.today['temp'] = data_point['main']['temp']
                    self.today['weather'] = data_point["weather"][0]["main"]
                    self.today['wind'] = data_point['wind']['speed']
                if date == (self.date + timedelta(days=1)):
                    self.tomorrow['temp'] = data_point['main']['temp']
                    self.tomorrow['weather'] = data_point["weather"][0]["main"]
                if date == (self.date + timedelta(days=2)):
                    self.day_p2['temp'] = data_point['main']['temp']
                    self.day_p2['weather'] = data_point["weather"][0]["main"]
                if date == (self.date + timedelta(days=3)):
                    self.day_p3['temp'] = data_point['main']['temp']
                    self.day_p3['weather'] = data_point["weather"][0]["main"]
        return self.today, self.tomorrow, self.day_p2, self.day_p3


if __name__ == "__main__":
    weather = Weather()
    print(weather.get_data(weather_key, city, state))