from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("WTFORMS_SECRET_KEY")


class MyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    login_form = MyForm()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
