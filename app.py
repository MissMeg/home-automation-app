from flask import Flask, render_template, redirect, url_for, request
from gcalendar import Gcalendar
from weather import Weather
import forms
import keys
import grocery
import todos


PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = keys.app_key

groc = grocery.Glist.select()
todo = todos.Todos.select()
weather = Weather().get_data(keys.weather_key, keys.city, keys.state)
cal = Gcalendar().gcal_connect()

@app.route('/')
def index():
    return render_template('index.html', grocery=groc, todos=todo, weather=weather, cal=cal)

@app.route('/grocery', methods=('GET', 'POST'))
def add_grocery():
    form = forms.GroceryForm()
    if form.validate_on_submit():
        grocery.Glist.create_item(
            title=form.title.data,
            description=form.description.data
        )
        return redirect(url_for('index'))
    return render_template('index.html', grocery=groc, todos=todo, weather=weather, cal=cal, gform=gform, tform=tform)

@app.route('/todo', methods=('GET', 'POST'))
def add_todo():
    form = forms.TodoForm()
    if form.validate_on_submit():
        todos.Todos.create_todo(
            title=form.title.data,
            location=form.location.data
        )
        return redirect(url_for('index'))
    return render_template('index.html', grocery=groc, todos=todo, weather=weather, cal=cal, gform=gform, tform=tform)


if __name__ == '__main__':
    grocery.initialize()
    todos.initialize()
    app.run(host=HOST, port=PORT)