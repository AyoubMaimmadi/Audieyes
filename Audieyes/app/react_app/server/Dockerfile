FROM python:3.8-slim

WORKDIR /server

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV NAME ImageCaptioning

CMD ["python", "app.py"]
