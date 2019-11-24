from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = '4ecd1da2c26abd5fdb366d9c94a95fff'

from timerapp import timer
