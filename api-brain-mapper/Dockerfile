# syntax=docker/dockerfile:1.4
FROM python:3.11

WORKDIR /app

COPY requirements.txt /app
RUN apt-get update -y
RUN apt install gcc
RUN apt-get install -y libmariadb-dev
RUN pip3 install -r requirements.txt

# COPY . /app

ENTRYPOINT ["python3"]
CMD ["run.py"]


