from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# Включение CORS для всего приложения
CORS(app)


@app.route("/api/v2", methods=["GET"])
def api_v2():
    return jsonify({"message": "Hello from Python (API v2)!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
