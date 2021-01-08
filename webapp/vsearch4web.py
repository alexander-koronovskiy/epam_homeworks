from flask import Flask, escape, render_template, request
from vsearch import search4letters

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


def log_request(req: "flask_request", res: str) -> None:
    with open("vsearch.log", "a") as log:
        print(req.form, file=log, end="|")
        print(req.remote_addr, file=log, end="|")
        print(req.user_agent, file=log, end="|")
        print(res, file=log, end="|")


@app.route("/search4", methods=["POST"])
def do_search() -> "html":
    phrase = request.form["phrase"]
    letters = request.form["letters"]
    title = "Here are your results:"
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template(
        "results.html",
        the_title=title,
        the_phrase=phrase,
        the_letters=letters,
        the_results=results,
    )


@app.route("/")
@app.route("/entry")
def entry_page() -> "html":
    return render_template(
        "entry.html", the_title="Welcome to search4letters on the web!"
    )


@app.route("/viewlog")
def view_the_log() -> str:
    with open("vsearch.log") as log:
        contents = log.read()
    return escape(contents)


if __name__ == "__main__":
    app.run(debug=True)
