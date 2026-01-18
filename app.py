from flask import Flask, render_template, request
from calculator import calculate

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        operation = request.form["operation"]
        result = calculate(num1, num2, operation)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
