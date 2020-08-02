#!/bin/sh
echo "Running gunicorn"
gunicorn -c 'gunicorn.py' 'app:create_app()'
