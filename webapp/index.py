from flask import Flask, escape, render_template, request

app = Flask(__name__)

data = [
    {
        "id": 9,
        "first_name": "Esther",
        "last_name": "Gerard",
        "gender": "female",
        "phone": "078 833 60 86",
        "email": "esther.gerard@example.com",
        "state": "Obwalden",
    },
    {
        "id": 8,
        "first_name": "Milan",
        "last_name": "Roussel",
        "gender": "male",
        "phone": "05-49-63-84-21",
        "email": "milan.roussel@example.com",
        "state": "Paris",
    },
    {
        "id": 7,
        "first_name": "Oskari",
        "last_name": "Pollari",
        "gender": "male",
        "phone": "08-292-193",
        "email": "oskari.pollari@example.com",
        "state": "Southern Ostrobothnia",
    },
    {
        "id": 6,
        "first_name": "Harper",
        "last_name": "Wade",
        "gender": "female",
        "phone": "09-1940-8653",
        "email": "harper.wade@example.com",
        "state": "Victoria",
    },
    {
        "id": 5,
        "first_name": "Gabrielle",
        "last_name": "Nguyen",
        "gender": "female",
        "phone": "079 148 52 04",
        "email": "gabrielle.nguyen@example.com",
        "state": "Schaffhausen",
    },
]


@app.route("/")
def index():
    rows = data
    return render_template("table_overview.html", title="Overview", rows=rows)


if __name__ == "__main__":
    app.run()
