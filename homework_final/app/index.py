import random

from app.handler import load_rows, show_rows
from flask import Flask, json, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    data = show_rows()
    print(data)
    return render_template(
        "table_overview.html", title="Overview", rows=data, user=random.choice(data)
    )


@app.route("/suggestions")
def suggestions():
    text = request.args.get("jsdata")
    suggestions_list = [
        {
            "id": 19,
            "first_name": "Harley",
            "last_name": "Hall",
            "gender": "male",
            "phone": "(986)-042-8366",
            "email": "harley.hall@example.com",
            "state": "Waikato",
        },
        {
            "id": 18,
            "first_name": "Steven",
            "last_name": "Robin",
            "gender": "male",
            "phone": "077 081 04 40",
            "email": "steven.robin@example.com",
            "state": "Luzern",
        },
        {
            "id": 17,
            "first_name": "Ted",
            "last_name": "Watkins",
            "gender": "male",
            "phone": "011-557-8658",
            "email": "ted.watkins@example.com",
            "state": "Longford",
        },
        {
            "id": 16,
            "first_name": "Valdemar",
            "last_name": "Costa",
            "gender": "male",
            "phone": "(71) 4791-9361",
            "email": "valdemar.costa@example.com",
            "state": "Rio Grande do Sul",
        },
        {
            "id": 15,
            "first_name": "Rosa",
            "last_name": "Castillo",
            "gender": "female",
            "phone": "(777)-513-7893",
            "email": "rosa.castillo@example.com",
            "state": "Massachusetts",
        },
        {
            "id": 14,
            "first_name": "Eléna",
            "last_name": "Guillaume",
            "gender": "female",
            "phone": "02-00-07-35-23",
            "email": "elena.guillaume@example.com",
            "state": "Aude",
        },
        {
            "id": 13,
            "first_name": "Dana",
            "last_name": "Lewis",
            "gender": "female",
            "phone": "(046)-360-9987",
            "email": "dana.lewis@example.com",
            "state": "Connecticut",
        },
        {
            "id": 12,
            "first_name": "Andrea",
            "last_name": "Ruiz",
            "gender": "female",
            "phone": "941-851-851",
            "email": "andrea.ruiz@example.com",
            "state": "Cantabria",
        },
        {
            "id": 11,
            "first_name": "Matthew",
            "last_name": "Willis",
            "gender": "male",
            "phone": "01603 02234",
            "email": "matthew.willis@example.com",
            "state": "Powys",
        },
        {
            "id": 10,
            "first_name": "Louise",
            "last_name": "Reed",
            "gender": "female",
            "phone": "011-660-5179",
            "email": "louise.reed@example.com",
            "state": "Donegal",
        },
        {
            "id": 9,
            "first_name": "Frank",
            "last_name": "Mercier",
            "gender": "male",
            "phone": "078 917 40 20",
            "email": "frank.mercier@example.com",
            "state": "Zürich",
        },
        {
            "id": 8,
            "first_name": "Raymond",
            "last_name": "Thomas",
            "gender": "male",
            "phone": "09-7701-5568",
            "email": "raymond.thomas@example.com",
            "state": "Queensland",
        },
        {
            "id": 7,
            "first_name": "Kathy",
            "last_name": "Evans",
            "gender": "female",
            "phone": "061-522-4991",
            "email": "kathy.evans@example.com",
            "state": "Kilkenny",
        },
        {
            "id": 6,
            "first_name": "Maxine",
            "last_name": "Garrett",
            "gender": "female",
            "phone": "(980)-399-6558",
            "email": "maxine.garrett@example.com",
            "state": "Washington",
        },
        {
            "id": 5,
            "first_name": "Otfried",
            "last_name": "Pech",
            "gender": "male",
            "phone": "0899-9984567",
            "email": "otfried.pech@example.com",
            "state": "Bayern",
        },
        {
            "id": 4,
            "first_name": "Emmanuel",
            "last_name": "Moulin",
            "gender": "male",
            "phone": "078 737 47 49",
            "email": "emmanuel.moulin@example.com",
            "state": "Appenzell Innerrhoden",
        },
        {
            "id": 3,
            "first_name": "Felinta",
            "last_name": "Silveira",
            "gender": "female",
            "phone": "(47) 3893-5637",
            "email": "felinta.silveira@example.com",
            "state": "Rio de Janeiro",
        },
        {
            "id": 2,
            "first_name": "Carmen",
            "last_name": "Roos",
            "gender": "female",
            "phone": "68872322",
            "email": "carmen.roos@example.com",
            "state": "Hordaland",
        },
        {
            "id": 1,
            "first_name": "Dylan",
            "last_name": "Slawa",
            "gender": "male",
            "phone": "358-759-9950",
            "email": "dylan.slawa@example.com",
            "state": "Northwest Territories",
        },
    ]
    suggestions_list = suggestions_list[: int(text)]
    return render_template("suggestion.html", suggestions=suggestions_list)


if __name__ == "__main__":
    # load_rows()
    app.run()
    # delete bd, delete img
