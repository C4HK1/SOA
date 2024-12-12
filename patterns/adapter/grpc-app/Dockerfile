FROM python:3.9-slim
WORKDIR /app
RUN pip install flask
RUN pip install flask-cors
RUN pip install grpcio
RUN pip install grpcio-tools
COPY . .
EXPOSE 50051
CMD ["python", "grpc-app.py"]