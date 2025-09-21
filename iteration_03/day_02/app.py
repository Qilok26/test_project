from flask import Flask, request, jsonify, render_template_string
import random
import json
from user import User

app = Flask(__name__)

# Sample data
NAMES = ["Ben", "Liam", "Charlie", "Henry", "Eve"]
AGES = list(range(0, 60))
HOBBIES = ["painting", "cycling", "gaming", "cooking", "reading"]
FAV_ANIMAL = ["pig", "horse", "cat", "dog"]

USER_FILE = "user.json"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            count = int(request.form.get("count", 1))
        except ValueError:
            count = 1

        users = []
        for _ in range(count):
            name = random.choice(NAMES)
            age = random.choice(AGES)
            hobby = random.choice(HOBBIES)
            fav_animal = random.choice(FAV_ANIMAL)

            user = User(name, age, hobby, fav_animal)
            users.append(user.to_dict())

        # Save list of users into JSON
        with open(USER_FILE, "w") as f:
            json.dump(users, f)

        return jsonify(users)

    # Simple HTML form
    html_form = """
    <h1>Random User Generator</h1>
    <form method="POST">
        <label for="count">How many random users do you want?</label>
        <input type="number" name="count" min="1" max="1000" required>
        <button type="submit">Generate</button>
    </form>
    <p>After generating, visit <a href="/show">/show</a> to see the users.</p>
    """
    return render_template_string(html_form)


@app.route("/show")
def show_users():
    try:
        with open(USER_FILE, "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        return "No users generated yet. Please go to the home page and generate some."

    html_template = """
    <h1>Generated Users</h1>
    <ul>
    {% for user in users %}
        <li>
            <b>Name:</b> {{ user.name }},
            <b>Age:</b> {{ user.age }},
            <b>Hobby:</b> {{ user.hobby }},
            <b>Favorite Animal:</b> {{ user.fav_animal }}
        </li>
    {% endfor %}
    </ul>
    <p><a href="/">Back to Home</a></p>
    """
    return render_template_string(html_template, users=users)


if __name__ == "__main__":
    app.run(debug=True)