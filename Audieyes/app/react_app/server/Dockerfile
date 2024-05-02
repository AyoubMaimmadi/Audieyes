FROM python:3.9-slim

WORKDIR /app

COPY . /app
COPY ./best_model.h5 /app/best_model.h5

RUN pip install --no-cache-dir flask flask-cors Pillow transformers

EXPOSE 5000

ENV NAME World

CMD ["flask", "run", "--host=0.0.0.0"]
