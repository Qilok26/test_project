from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)


@app.route("/")
def home():
    res = requests.get("https://dog.ceo/api/breeds/image/random")
    data = res.json()
    return f"<h1>Here’s a random dog!</h1><img src='{data['message']}' width='400'>"

# dog images by breed 
@app.route("/breed")
def breed():
    breed = request.args.get("breed", "beagle")  # default breed = beagle
    res = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
    if res.status_code == 200:
        data = res.json()
        return f"<h1>{breed.title()}</h1><img src='{data['message']}' width='400'>"
    return f"<h1>Breed {breed} not found!</h1>"

# form page
@app.route("/form")
def form():
    return '''
        <form action="/showbreed" method="post">
            <label for="breed">Enter a dog breed:</label>
            <input type="text" name="breed">

            <label for="size">Enter the size you want to see the image:</label>
            <input type="range" id="size" name="size" min="1" max="600" value="300" 
                oninput="this.nextElementSibling.value = this.value">
            <output>300</output><br><br>
            
            <input type="submit" value="Show Dog">
        </form>
    '''

# handle form submission
@app.route("/showbreed", methods=["POST"])
def showbreed():
    breed = request.form.get("breed")
    size = request.form.get("size", 300)  # default = 300 px
    res = requests.get(f"https://dog.ceo/api/breed/{breed}/images/random")
    if res.status_code == 200:
        #200 means we chilling
        data = res.json()
        return f"<h1>{breed.title()}</h1><img src='{data['message']}' width='{size}'>"
    return f"<h1>Breed {breed} not found!</h1>"

if __name__ == "__main__":
    app.run(debug=True)