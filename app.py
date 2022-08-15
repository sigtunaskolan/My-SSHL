from flask import Flask, render_template, request
from schedule import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", foura=foura, sixa=sixa, fiveb=fiveb)


@app.route("/testsub")
def testsub():
    return render_template("testsub.html")


if __name__ == "__main__":
    app.run()

# implement different route per class
# implement route for weekend
# remove seconds from time
