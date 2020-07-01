from flask import Flask, render_template, redirect, url_for, request
from gcalendar import Gcalendar
from grocery import Glist
from todos import Todos
from weather import Weather