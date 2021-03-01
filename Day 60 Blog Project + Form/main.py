from flask import Flask, render_template
import requests

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


@app.route('/contact')
def contact_page():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
