FROM python:3.9-slim
WORKDIR /app
RUN pip install flask
RUN pip install flask-cors
RUN pip install grpcio
RUN pip install grpcio-tools
COPY . .

RUN python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. my_grpc.proto

EXPOSE 8080
CMD ["python", "adapter-app.py"]