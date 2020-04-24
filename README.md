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
3. Install the dependencies - `pipenv install` or (to use the lock file only) `pipenv install --ignore-pipfile`
4. Run with `pipenv python run app.py`

To run this project in development mode:

1. Download the project
2. Make sure you have pipenv installed - `python -m pip install pipenv` or `pip install pipenv`
3. Install the dependencies - `pipenv install --dev` or (to use the lock file only) `pipenv install --ignore-pipfile --dev`
4. Run with `pipenv python run app.py`
