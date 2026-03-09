from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Calculator API is running!"

@app.route("/add")
def add():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({"result": a + b})

@app.route("/subtract")
def subtract():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({"result": a - b})

@app.route("/multiply")
def multiply():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({"result": a * b})

@app.route("/divide")
def divide():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({"result": a / b})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5051)