import grpc
from concurrent import futures
import time
import my_grpc_pb2
import my_grpc_pb2_grpc


class MyService(my_grpc_pb2_grpc.MyServiceServicer):
    def MyMethod(self, request, context):
        print(f"Получен запрос с именем: {request.name}")
        response = my_grpc_pb2.MyResponse()
        response.message = f"Привет, {request.name}!"
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    my_grpc_pb2_grpc.add_MyServiceServicer_to_server(MyService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Сервер запущен на порту 50051...")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
