from flask import Flask, request
import requests

# Creates Simple Flask App
app = Flask(__name__)

# Home Route gets random joke
@app.route("/")
def home():
    url = "https://official-joke-api.appspot.com/random_joke" # API url for random joke

    response = requests.get(url) # GET Request is made to url, response is return value
    data = response.json() # Parse the JSON into a dictionary which we can use

    joke = f"{data['setup']} ... {data['punchline']}" # Get what we want from response data
    html_content = f"<h1>Random Joke</h1><p>{joke}</p>" # organize into HTML for web page.

    return html_content # What you return is what you see in the page. Should always be some HTML content

# Second Route gets cat fact
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

# Third Route Utilizes Query params for limit of number of cat breed info
@app.route("/catbreeds")
def cat_breeds():
    limit = int(request.args.get("limit", 1))
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

# Third Route utilizes Query Parameters for total joke count
@app.route("/joke")
def jokes():
    count = int(request.args.get("count", 1))
    jokes = []
    for _ in range(count):
        url = f"https://official-joke-api.appspot.com/random_joke?count={count}"
        response = requests.get(url)
        data = response.json()
        jokes.append(f"{data['setup']} ... {data['punchline']}")
    joke_html = "<br><br>".join(jokes)
    html_content = f"<h1>Here are {count} joke(s):</h1><p>{joke_html}</p>"
    return html_content

if __name__ == "__main__":
    app.run()