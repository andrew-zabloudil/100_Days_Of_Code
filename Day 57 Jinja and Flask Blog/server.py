from flask import Flask, render_template
from dotenv import load_dotenv
import random
from datetime import datetime
import requests

load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index1.html", random_number=random_number, current_year=current_year)


@app.route("/guess/<string:name>")
def guess(name):
    agify_url = "https://api.agify.io"
    genderize_url = "https://api.genderize.io"
    params = {
        "name": name,
    }

    age_response = requests.get(url=agify_url, params=params)
    age_data = age_response.json()
    age = age_data["age"]

    gender_response = requests.get(url=genderize_url, params=params)
    gender_data = gender_response.json()
    gender = gender_data["gender"]

    return render_template("guess.html", name=name, age=age, gender=gender)


@app.route("/blog")
def get_blog():
    blog_json_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(url=blog_json_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
