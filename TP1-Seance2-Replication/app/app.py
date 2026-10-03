import os
from flask import Flask, jsonify, request

app = Flask(__name__)

NODE_NAME = os.getenv("NODE_NAME", "unknown")
ROLE = os.getenv("ROLE", "unknown")
PORT = int(os.getenv("PORT", "8080"))

DATA = {}


@app.get("/")
def home():
    return jsonify({
        "service": "distributed-replication-tp",
        "node": NODE_NAME,
        "role": ROLE
    })


@app.get("/health")
def health():
    return jsonify({
        "node": NODE_NAME,
        "role": ROLE,
        "status": "UP"
    })


@app.get("/data")
def get_data():
    return jsonify({
        "node": NODE_NAME,
        "role": ROLE,
        "count": len(DATA),
        "data": DATA
    })


@app.post("/data")
def post_data():
    body = request.get_json(silent=True) or {}

    key = body.get("key")
    value = body.get("value")

    if not key or value is None:
        return jsonify({"error": "key and value are required"}), 400

    DATA[key] = value

    return jsonify({
        "message": "data stored",
        "node": NODE_NAME,
        "role": ROLE,
        "item": {
            "key": key,
            "value": value
        }
    })


@app.delete("/data")
def delete_data():
    DATA.clear()
    return jsonify({
        "message": "data cleared",
        "node": NODE_NAME
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
