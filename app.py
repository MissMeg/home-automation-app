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

app = Flask(__name__)

@app.route('/')
def index():
    groceries = grocery.Glist.get_all()
    tasks = todos.Todos.get_all()
    print(groceries)
    for item in groceries:
        print(item.title)
    for task in tasks:
        print(task.title)
    return render_template('index.html', weather=get_weather, events=get_events, groceries=groceries, todos=tasks)

@app.route('/save-grocery-item', methods=['GET', 'POST'])
def save_grocery():
    data = request.form.to_dict()
    print(data)
    grocery.Glist.create_item(data['item'], data['description'])
    return redirect(url_for('index'))

@app.route('/save-todo-item', methods=['GET', 'POST'])
def save_todo():
    data = request.form.to_dict()
    print(data)
    todos.Todos.create_todo(data['title'], data['location'])
    return redirect(url_for('index'))


if __name__ == '__main__':
    grocery.initialize()
    todos.initialize()
    app.run(debug=True, host='127.0.0.1', port=8000)
