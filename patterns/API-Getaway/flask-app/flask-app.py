from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# Включение CORS для всего приложения
CORS(app)


@app.route("/api/v1", methods=["GET"])
def api_v1():
    return jsonify({"message": "Hello from Flask (API v1)!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
