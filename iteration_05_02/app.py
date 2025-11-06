from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    author = "Georgii Panasenko"
    interests = ["Web Development", "Machine Learning", "UI Design"]
    is_student = True
    return render_template("about.html", author=author, interests=interests, is_student=is_student)

@app.route("/contact")
def contact():
    contacts = {
        "email": "gpanasenko26@nmhschool.org",
        "github": "https://github.com/qilok26",
        "twitter": None  
    }
    return render_template("contact.html", contacts=contacts)

if __name__ == "__main__":
    app.run(debug=True)
