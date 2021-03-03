from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
db = sqlite3.connect(
    "Day 63 Virtual Bookshelf with SQLite/books-collection.db")

all_books = []


@app.route('/')
def home():
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        data = request.form.to_dict()
        all_books.append(data)
        print(all_books)
        return redirect(url_for('home'))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
