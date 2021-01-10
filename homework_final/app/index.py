import random

from app.handler import data
from flask import Flask, escape, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "table_overview.html", title="Overview", rows=data, user=random.choice(data)
    )


if __name__ == "__main__":
    app.run()
