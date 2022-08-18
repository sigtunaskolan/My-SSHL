from flask import Flask, render_template, redirect, url_for
import datetime
from schedule import *

app = Flask(__name__)


@app.route("/")
def index():
    dayofweek = datetime.datetime.today().weekday()
    if dayofweek > 5:
        return redirect(url_for("helg"))
    else:
        return render_template("index.html")


@app.route("/helg")
def helg():
    return render_template("helg.html")


@app.route("/bm23")
def bm23():
    bm23 = finish_today(b23)
    return render_template("Bm23.html", bm23=bm23)


@app.route("/bm24")
def bm24():
    bm24 = finish_today(b24)
    return render_template("Bm24.html", bm24=bm24)


@app.route("/bm25")
def bm25():
    bm25 = finish_today(b25)
    return render_template("Bm25.html", bm25=bm25)


@app.route("/ek23")
def ek23():
    ek23 = finish_today(e23)
    return render_template("Ek23.html", ek23=ek23)


@app.route("/ek24")
def ek24():
    ek24 = finish_today(e24)
    return render_template("Ek24.html", ek24=ek24)


@app.route("/ek25")
def ek25():
    ek25 = finish_today(e25)
    return render_template("Ek25.html", ek25=ek25)


@app.route("/na23")
def na23():
    na23 = finish_today(n23)
    return render_template("Na23.html", na23=na23)


@app.route("/na24")
def na24():
    na24 = finish_today(n24)
    return render_template("Na24.html", na24=na24)


@app.route("/na25")
def na25():
    na25 = finish_today(n25)
    return render_template("Na25.html", na25=na25)


@app.route("/sa23")
def sa23():
    sa23 = finish_today(s23)
    return render_template("Sa23.html", sa23=sa23)


@app.route("/sa24")
def sa24():
    sa24 = finish_today(s24)
    return render_template("Sa24.html", sa24=sa24)


@app.route("/sa25")
def sa25():
    sa25 = finish_today(s25)
    return render_template("Sa25.html", sa25=sa25)


if __name__ == "__main__":
    app.run(debug=True)
