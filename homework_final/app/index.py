import random

from app.handler import load_rows, show_rows
from flask import Flask, json, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    data = show_rows()
    return render_template(
        "table_overview.html",
        title="Random user by K",
        rows=data,
        user=random.choice(data),
    )


@app.route("/suggestions")
def suggestions():
    text = request.args.get("jsdata")
    suggestions = show_rows()
    suggestions_list = suggestions[: int(text)]
    return render_template("suggestion.html", suggestions=suggestions_list)


@app.route("/user_update")
def user_update():
    data = show_rows()
    return render_template("user.html", user=random.choice(data))


if __name__ == "__main__":
    # load_rows()
    app.run()
    # delete bd, delete img
