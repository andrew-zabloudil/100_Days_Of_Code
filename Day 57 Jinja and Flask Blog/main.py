from flask import Flask, render_template
import requests

blog_json_url = "https://api.npoint.io/5abcca6f4e39b4955965"
response = requests.get(url=blog_json_url)
all_posts = response.json()


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:post_id>")
def get_post(post_id):
    post = [post for post in all_posts if post["id"] == post_id][0]
    return render_template("post.html", blog_post=post)


if __name__ == "__main__":
    app.run(debug=True)
