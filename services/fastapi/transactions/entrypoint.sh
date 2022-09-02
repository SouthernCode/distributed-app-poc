#!/bin/sh

echo "Waiting for postgres..."
echo "$POSTGRES_HOST"
echo "$POSTGRES_PORT"
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 0.1
done

if [ "$IS_CONSUMER" = "1" ]
then
  echo "Transactions service message broker consumer starting"
  exec python consumer.py
else
    echo "Using gunicorn"
    exec uvicorn main:app --proxy-headers --host 0.0.0.0 --port 9001 --reload
fi