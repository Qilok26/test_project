from flask import Flask, request, render_template
import requests

# Creates Simple Flask App
app = Flask(__name__)

# Home Route shows options in HTML using buttons
@app.route("/")
def home():
    return render_template("home.html")

# First Route gets random joke
@app.route("/joke")
def joke():
    url = "https://official-joke-api.appspot.com/random_joke" # API for random joke
    response = requests.get(url)
    data = response.json()
    joke = f"{data['setup']} ... {data['punchline']}"
    html_content = f"<h1>Random Joke</h1><p>{joke}</p>"
    return html_content

# Second Route utilizes Query Parameter 'count' with the Random Joke API
@app.route("/jokes")
def jokes():
    count = int(request.args.get("joke_count", 1))
    jokes = []
    for _ in range(count):
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url)
        data = response.json()
        jokes.append(f"{data['setup']} ... {data['punchline']}")
    joke_html = "<br><br>".join(jokes)
    html_content = f"<h1>Here are {count} joke(s):</h1><p>{joke_html}</p>"
    return html_content

# Third Route utilizes GET method with Cat Fact API
@app.route("/catfact")
def cat_fact():
    url = "https://catfact.ninja/fact" # API for cat fact
    response = requests.get(url)
    data = response.json()
    html_content = (f"""
        <h1>Cat Fact</h1>
        <p>Random Cat Fact: {data['fact']}</p>
        """)
    return html_content

# Fourth Route utilizes Query Parameter 'limit' with Cat Breeds API
@app.route("/catbreeds")
def cat_breeds():
    limit = int(request.args.get("cat_breeds_count", 1))
    url = f"https://catfact.ninja/breeds?limit={limit}" # API for cat fact
    response = requests.get(url)
    response = response.json()
    breeds_list = []
    for breed in response['data']:
        breeds_list.append(f"Breed: {breed['breed']} Country: {breed['country']}")
    html_content = (f"""
        <h1>Cat Breeds</h1>
        <p>{"<br></br>".join(breeds_list)}</p>
    """)
    return html_content

if __name__ == "__main__":
    app.run()