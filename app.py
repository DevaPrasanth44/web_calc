from flask import Flask
import os
from calculator import calculate

app = Flask(__name__)

@app.route("/")
def home():
    n1 = os.getenv("NUMBER1", "0")
    n2 = os.getenv("NUMBER2", "0")
    op = os.getenv("OPERATION", "add")

    result = calculate(n1, n2, op)
    return f"Result: {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
