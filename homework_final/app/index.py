import random

from app.handler import show_rows
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    data = show_rows()
    return render_template(
        "table_overview.html", title="Overview", rows=data, user=random.choice(data)
    )


if __name__ == "__main__":
    app.run()
