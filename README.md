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

## Running the Project (without Docker)

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

## Running the Project (WITH Docker)

With this approach you save more time as Docker containerizes the entire platform abstracting dependency issues away from developers.

1. Install Docker daemon

    1. Run project (with Dockerfile)
    2. Run project (with docker-compose, the easiest/fastest way)


## Install Docker daemon

Download the Docker desktop locally [from here](https://docs.docker.com/desktop/). Select your OS and download the agent. e.g. If you are using a Mac, please click "Mac" > "Install Docker Desktop on Mac" > click "Download from Docker Hub"

## Run project (with Dockerfile)

The easiest way to run this project is using the command line below:

```bash
docker build -t home-automation-app . && \
  docker run --env-file .env.home_automation_app -p 8000:8000 home-automation-app
```

This uses the `Dockerfile` to do the setup for us. After building the app, we tell the Docker agent to run using our `.env` file. This is only accesible by you and you must **not** share these details to anyone.

```bash
WEATHER_KEY=YOUR_API_KEY
WEATHER_CITY=YOUR_CITY
WEATHER_STATE=YOUR_STATE
CAL_ID=YOUR_CALENDAR_ID
```

## Run project (with docker-compose)

An even easier way to run the app is just configure your `.env` file (like above) but run the command below:

```bash
docker-compose up -d
```

Docker compose is just like Dockerfile, but it's more useful as an ochestration tool to launch multiple docker containers.

## API in keys.py

You will need to create your own keys.py file and include your API information.

* [Weather API](https://openweathermap.org/)
  * variables: weather_key = api key, city = your city, state = your state
* If you want to connect to a specific Google Calendar (other than your primary one) you will need to grab the calendar's ID from it's settings (click on the gear icon in the top right of your screen, select "Settings", and scroll down to 'Integrate calendar')

  * variable: cal_key = calendar id 
 
example keys.py
```
weather_key = "Api key"
city = "Your city"
state = "Your state"
cal_key = "Calender id"
```
## Weather API

Create an [OpenWeather](https://openweathermap.org/) account to get an API key. Add the key to your keys.py file. You can find the docs [here](https://openweathermap.org/forecast5) for the specific API connection being used.

## Google Calendar API

Complete step 1 from [Google's documentation](https://developers.google.com/calendar/quickstart/python?authuser=1). 
Make sure you are logged in with the Google account you want to use.

Download your credentials (file should be called credentials.json) and add the file to your directory and to your .gitignore file.

## Todos and Grocery List

Both the Todos and Grocery list are using [Peewee](http://docs.peewee-orm.com/en/latest/) to create  a SQLite database.
