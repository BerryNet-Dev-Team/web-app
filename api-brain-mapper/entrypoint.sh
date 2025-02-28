#!/bin/sh

# Exports FLASK_APP to make flask var work
export FLASK_APP=src.app:create_app

# Apply migrations
echo "Running migrations..."
flask db upgrade

# Start
echo "Starting production server..."
gunicorn -w 2 -k gevent -b 0.0.0.0:5000 wsgi_run:app
