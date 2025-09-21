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

# # Second Route gets cat fact
# @app.route("/catfact")
# def cat_fact():
#     pass

# # Third Route Utilizes Query params for limit of number of cat breed info
# @app.route("/catbreeds")
# def cat_breeds():
#     return pass

# # Third Route utilizes Query Parameters for total joke count
# @app.route("/joke")
#     return pass

if __name__ == "__main__":
    app.run()