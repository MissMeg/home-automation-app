from flask import Flask, render_template, redirect, url_for, request
from gcalendar import Gcalendar
from grocery import Glist
from todos import Todos
from weather import Weather


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)