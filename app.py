from flask import Flask, render_template, request

from Text import Text

# from main import load
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def predict():
    f = open('corpus.txt', encoding='utf-8')
    text = Text(f.read())
    txt = request.form.get("userInput")
    out = text.predict(txt)
    print(out)
    return render_template("index.html", out=[i[0][0] + " " + i[0][1] + " " + i[0][2] for i in out])


if __name__ == "__main__":
    app.run()
