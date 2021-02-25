from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}<b>"
    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}<em>"
    return wrapper_function


def make_underline(function):
    def wrapper_function():
        return f"<u>{function()}<u>"
    return wrapper_function


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/user/<username>')
def user(username):
    return f"Hello, {username}"


@app.route('/bye')
@make_bold
@make_underline
@make_emphasis
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)
