from flask import Flask, render_template, request
from schedule import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", foura=foura, sixa=sixa, fiveb=fiveb)


@app.route("/Ek23")
def ek23():
    return render_template("Ek23.html")

@app.route("/Na23")
def na23():
    return render_template("Na23.html")

@app.route("/Sa23")
def sa23():
    return render_template("Sa23.html")

@app.route("/Bm24")
def bm24():
    return render_template("Bm24.html")

@app.route("/Ek24")
def ek24():
    return render_template("Ek24.html")

@app.route("/Na24")
def na24():
    return render_template("Na24.html")

@app.route("/Sa24")
def sa24():
    return render_template("Sa24.html")

@app.route("/Bm25")
def bm25():
    return render_template("Bm25.html")

@app.route("/Ek25")
def ek25():
    return render_template("Ek25.html")

@app.route("/Na25")
def na25():
    return render_template("Na25.html")

@app.route("/Sa25")
def sa25():
    return render_template("Sa25.html")

@app.route("/Bm23")
def bm23():
    return render_template("Bm23.html")


if __name__ == "__main__":
    app.run()

# implement different route per class
# implement route for weekend
# remove seconds from time
