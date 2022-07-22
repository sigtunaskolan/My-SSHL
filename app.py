from flask import Flask, render_template, request
from schedule import *

app = Flask(__name__)


@app.route("/")
def index():
    foura = finish_today(class_4a)
    fiveb = finish_today(class_5b)
    sixa = finish_today(class_6a)
    return render_template("index.html", foura=foura, sixa=sixa, fiveb=fiveb)


if __name__ == "__main__":
    app.run()
