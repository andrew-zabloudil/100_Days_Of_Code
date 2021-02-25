from flask import Flask
from dotenv import load_dotenv
import random

load_dotenv()

app = Flask(__name__)

NUMBERS = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
TOO_LOW = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
TOO_HIGH = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
CORRECT = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"

RANDOM_NUMBER = random.randint(1, 10)


@app.route('/')
def hello_world():
    html_render = (
        f"<h1>Guess a number between 0 and 9</h1>"
        f"<img src={NUMBERS} width=300/>"
    )
    return html_render


@app.route('/<int:number>')
def number_guess(number):
    if number > RANDOM_NUMBER:
        html_render = (
            f"<h1 style='color:purple'>Too high, try again!</h1>"
            f"<img src={TOO_HIGH} width=300/>"
        )
    elif number < RANDOM_NUMBER:
        html_render = (
            f"<h1 style='color:red'>Too low, try again!</h1>"
            f"<img src={TOO_LOW} width=300/>"
        )
    else:
        html_render = (
            f"<h1 style='color:green'>You found me!</h1>"
            f"<img src={CORRECT} width=300/>"
        )
    return html_render


if __name__ == "__main__":
    app.run(debug=True)
