# Home Automation App

The goal of this app is to make information more accessible and to have a single place to hold information valuable to a family. The app will be made to go with a RaspberryPi touch screen combo so the app can be interacted with and displayed in the home.

## Current Features

Current features are in the works. They will consist of:

* Daily weather forecast + next 3 days
* Grocery list
* ToDo list
* Calendar events for the day

## Running the Project

You will need Python version 3. This project utilizes pipenv. To run:

1. Download the project
2. Make sure you have pipenv installed - `python -m pip install pipenv` or `pip install pipenv`
3. Install the dependencies - `pipenv install --ignore-pipfile`
4. Run with `pipenv python run app.py`

To run this project in development mode:

1. Download the project
2. Make sure you have pipenv installed - `python -m pip install pipenv` or `pip install pipenv`
3. Install the dependencies - `pipenv install --dev`
4. Run with `pipenv python run app.py`

## API in keys.py

You will need to create your own keys.py file and include your API information.

* [Weather API](https://openweathermap.org/)
  * [Docs](https://openweathermap.org/forecast5)
  * variables: weather_key = api key, city = your city, state = your state
* If you want to connect to a specific Google Calendar (other than your primary one) you will need to grab the calendar's ID from it's settings.
  * variable: cal_key = calendar id

## Google Calendar API

Complete step 1 from [Google's documentation](https://developers.google.com/calendar/quickstart/python?authuser=1). Make sure you are logged in with the Google account you want to use.

Download your credentials (file should be called credentials.json) and add the file to your directory and to your .gitignore file.
  