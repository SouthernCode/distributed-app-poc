#!/bin/sh

echo "Waiting for postgres..."
echo "$POSTGRES_HOST"
echo "$POSTGRES_PORT"
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 0.1
done

echo "Running django makemigrations"
python manage.py makemigrations

echo "Running django migrate"
python manage.py migrate

echo "Loading default users"
python manage.py loaddata fixtures/default_users.json

exec "$@"
