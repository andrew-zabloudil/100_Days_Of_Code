from flask import Flask, render_template, request
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

my_gmail = os.getenv("my_gmail")
gmail_password = os.getenv("gmail_password")

blog_json_url = "https://api.npoint.io/43644ec4f0013682fc0d"
response = requests.get(url=blog_json_url)
all_posts = response.json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:post_id>")
def get_post(post_id):
    post = [post for post in all_posts if post["id"] == post_id][0]
    return render_template("post.html", blog_post=post)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact_page():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        send_email(data)
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(data):
    message = f"Subject:New Message From Your Website\n\nName: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage: {data['message']}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=gmail_password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs=my_gmail,
            msg=message
        )


if __name__ == "__main__":
    app.run(debug=True)
