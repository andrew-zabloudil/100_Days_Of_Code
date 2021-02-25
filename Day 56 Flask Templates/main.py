from flask import Flask
from flask import render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/")
def home_page(name=None):
    return render_template("index.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)
