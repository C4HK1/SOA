from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# Включение CORS для всего приложения
CORS(app)


@app.route("/", methods=["GET"])
def get_resource():
    param = request.args.get("param", None)

    if param == "error":
        return jsonify({}), 503
    else:
        return jsonify({"status": "Haha Good response!"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
