import random

from app.handler import load_rows, show_rows
from flask import Flask, json, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    data = show_rows()
    return render_template(
        "table_overview.html", title="Overview", rows=data, user=random.choice(data)
    )


@app.route("/get_value", methods=["GET", "POST"])
def get_value():
    name = request.form["name"]
    print(name)
    return json.dumps({"value": name})


if __name__ == "__main__":
    # load_rows()
    app.run()
    # delete bd, delete img
