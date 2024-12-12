from flask import Flask, request, jsonify
import grpc
import my_grpc_pb2
import my_grpc_pb2_grpc
from flask_cors import CORS
import os
import sys

app = Flask(__name__)
CORS(app)

GRPC_SERVICE_URL = os.getenv("GRPC_SERVICE_URL")


@app.route("/sayhello", methods=["POST"])
def say_hello():
    try:
        # Извлечение данных из REST-запроса
        data = request.get_json()
        name = data.get("name", "")

        channel = grpc.insecure_channel(GRPC_SERVICE_URL)
        stub = my_grpc_pb2_grpc.MyServiceStub(channel)

        # Создаем запрос с указанным именем
        r = my_grpc_pb2.MyRequest(name=name)

        # Отправляем запрос и получаем ответ
        r = stub.MyMethod(r)

        return jsonify({"message": r.message})
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
