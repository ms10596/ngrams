from flask import Flask, render_template, request
from Text import Text
#from main import load
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/com", methods=["GET", "POST"])
def predict():
    f = open('corpus.txt', encoding='utf-8')
    text = Text(f.read())
    txt = request.form.get("userInput")
    out = text.predict(txt)
    return render_template("index.html", out=out)

if __name__ == "__main__":
    app.run()
