# syntax=docker/dockerfile:1.4
FROM python:3.11

WORKDIR /app

# Install OS dependencies
RUN apt-get update -y
RUN apt-get install -y gcc libpq-dev

# Install app dependencies
COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . /app

# Run migrations & start flask app
RUN chmod +x ./entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]