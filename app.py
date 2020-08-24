from flask import Flask, render_template, redirect, url_for, request
from keys import weather_key, city, state
from gcalendar import Gcalendar
from weather import Weather
import grocery
import todos

app = Flask(__name__)

@app.route('/')
def index():
    groceries = grocery.Glist.get_all()
    for item in groceries:
        print(item.title)
    return render_template('index.html', groceries=groceries)

@app.route('/save-grocery-item', methods=['GET', 'POST'])
def save_grocery():
    data = request.form.to_dict()
    print(data)
    grocery.Glist.create_item(data['item'], data['description'])
    return redirect(url_for('index'))


if __name__ == '__main__':
    grocery.initialize()
    todos.initialize()
    app.run(debug=True, host='127.0.0.1', port=8000)