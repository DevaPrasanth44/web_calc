from flask import Flask, render_template, request
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        a = int(request.form["number1"])
        b = int(request.form["number2"])
        operation = request.form["operation"]

        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
