from datetime import datetime
from flask import render_template
from forms import RegisterForm
from app import app




@app.route('/')
@app.route('/index')
def index():
    day = datetime.now().weekday()
    weekdays = [
        "Понеділок",
        "Вівторок",
        "Середа",
        "Четвер",
        "П'ятниця",
        "Субота",
        "Неділя",
    ]
    if day >= 5 :
        type_day = "Вихідний день"
    else:
        type_day = "Будній день"
    return render_template('index.html', day = weekdays[day], type_day = type_day)


@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html', form=RegisterForm())


@app.route('/log_in')
def log_in():
    return render_template('log_in.html')


@app.route('/notes')
def notes():
    return render_template('breadcrumb.html')