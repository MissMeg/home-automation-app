# Home Automation App

The goal of this app is to make information more accessible and to have a single place to hold information valuable to a family. The project is made as a website interface so everyone can follow along.

Table of Contents
=================

   * [Skills Practiced](#skills-practiced)
   * [Current Features](#current-features)
   * [Running the Project](#running-the-project)
   * [API in keys.py](#api-in-keyspy)
   * [Weather API](#weather-api)
   * [Google Calendar API](#google-calendar-api)
   * [Todos and Grocery List](#todos-and-grocery-list)

## Skills Practiced

* Api connections
* Database Models
* Creating a Database
* CRUD with Database items
* Routes and "live" site with Flask

## Current Features

Current features are in the works. They will consist of:

* Daily weather forecast + next 3 days
* Grocery list
* ToDo list
* Calendar events for the day

## Running the Project

You will need Python version 3. This project utilizes [pipenv](https://realpython.com/pipenv-guide/) to run:

1. Download the project
2. Make sure you have pipenv installed - `python -m pip install pipenv` or `pip install pipenv`
3. Create the environment with `python -m pipenv shell`
4. Install the dependencies - `pipenv install --ignore-pipfile`
5. Run with `pipenv run python app.py`

To run this project in development mode:

1. Download the project
2. Make sure you have pipenv installed - `python -m pip install pipenv` or `pip install pipenv`
3. Create the environment with `python -m pipenv shell`
4. Install the dependencies - `pipenv install --dev`
5. Run with `pipenv run python app.py`

## API in keys.py

You will need to create your own keys.py file and include your API information.

* [Weather API](https://openweathermap.org/)
  * variables: weather_key = api key, city = your city, state = your state
* If you want to connect to a specific Google Calendar (other than your primary one) you will need to grab the calendar's ID from it's settings.
  * variable: cal_key = calendar id 
 
example keys.py
```
weather_key = "Api key"
city = "Your city"
state = "Your state"
cal_key = "Calender id"
```
## Weather API

Create an account at [Open Weathermap](https://openweathermap.org/) to get an API key. Add the key to your keys.py file. You can find the docs [here](https://openweathermap.org/forecast5) for the specific API connection being used.

## Google Calendar API

Complete step 1 from [Google's documentation](https://developers.google.com/calendar/quickstart/python?authuser=1). 
Make sure you are logged in with the Google account you want to use.

Download your credentials (file should be called credentials.json) and add the file to your directory and to your .gitignore file.

## Todos and Grocery List

Both the Todos and Grocery list are using [Peewee](http://docs.peewee-orm.com/en/latest/) to create  a SQLite database.
