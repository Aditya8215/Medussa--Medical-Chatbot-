FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app
EXPOSE 8080
RUN pip install -r requirements.txt

CMD ["python3", "app.py"].
