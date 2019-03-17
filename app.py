from flask import Flask, render_template, request
from Text import Text
from main import load
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/complete", methods=['GET'])
def predict():
    txt = request.form['userInput']
    out = load(txt)
    return render_template("index.html", out=out)

if __name__ == "__main__":
    app.run()
