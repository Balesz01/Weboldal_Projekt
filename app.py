# app.py
from flask import Flask, render_template, request
from profit import Segito

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        anyag = request.form["anyag"]
        hossz = request.form["hossz"]
        szelesseg = request.form["szelesseg"]
        melyseg = request.form["melyseg"]
        tobbi = request.form["tobbi"]

        segit = Segito(anyag, hossz, szelesseg, melyseg, tobbi)
        result = segit.medence_koltseg()

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

