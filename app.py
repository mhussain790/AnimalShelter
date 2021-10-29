from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
from flask_bootstrap import Bootstrap
import os

# Configuration

app = Flask(__name__, template_folder='templates')
Bootstrap(app)

app.config['MYSQL_HOST'] = 'flip1.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_hussamas'
app.config['MYSQL_PASSWORD'] = 'PASSWORD'
app.config['MYSQL_DB'] = 'cs340_hussamas'
app.config['MSQL_CURSORCLASS'] = "DictCursor"

mysql = MySQL(app)

# Routes


@app.route('/http://web.engr.oregonstate.edu/~hussamas/templates/index.html')
def root():
    return render_template('index.html')


@app.route('/animals')
def animals():
    return render_template('animals.html')


@app.route('/volunteers')
def volunteers():
    return render_template('volunteers.html')


@app.route('/mentors')
def mentors():
    return render_template('mentors.html')


@app.route('/locations')
def locations():
    return render_template('locations.html')


# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9113))
    #                                 ^^^^
    #              You can replace this number with any valid port

    app.run(port=port, debug=True)
