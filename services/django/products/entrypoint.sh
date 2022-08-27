#!/bin/sh

echo "Running django migrate"
python manage.py migrate

exec "$@"
