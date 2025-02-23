# syntax=docker/dockerfile:1.4
FROM python:3.11

WORKDIR /app

COPY requirements.txt /app
RUN apt-get update -y
RUN apt install gcc
RUN apt-get install -y libpq-dev
RUN pip3 install -r requirements.txt

# COPY . /app

ENV FLASK_APP=src.app:create_app
ENV FLASK_ENV=development

ENTRYPOINT ["sh", "-c", "flask db upgrade && python3 run.py"]
