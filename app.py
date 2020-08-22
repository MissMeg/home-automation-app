from flask import Flask, render_template, redirect, url_for, request
from keys import weather_key, city, state
from gcalendar import Gcalendar
from weather import Weather
import grocery
import todos

# Weather
my_weather = Weather()
get_weather = my_weather.get_data(weather_key, city, state)

# Events
my_cal = Gcalendar()
get_events = my_cal.gcal_connect()

# Groceries
# groceries = grocery.Glist.select()

# Tasks
tasks = todos.Todos.select()


app = Flask(__name__)

@app.route('/')
def index():
    groceries = grocery.Glist.get_all()
    print(groceries[0])
    for item in groceries:
        print(item)
    print(tasks)
    return render_template('index.html', weather=get_weather, events=get_events, groceries=groceries, todos=tasks)

@app.route('/save-grocery-item', methods=['GET', 'POST'])
def save_grocery():
    data = request.form.to_dict()
    print(data['item'])
    grocery.Glist.create_item(data['item'], data['description'])
    return redirect(url_for('index'))


if __name__ == '__main__':
    grocery.initialize()
    todos.initialize()
    app.run(debug=True, host='0.0.0.0', port=8000)