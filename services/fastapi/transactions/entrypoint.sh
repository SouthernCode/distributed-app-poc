#!/bin/sh

if [ "$IS_CONSUMER" = "1" ]
then
  echo "Transactions service message broker consumer starting"
  exec python consumer.py
else
    echo "Using gunicorn"
    exec uvicorn main:app --proxy-headers --host 0.0.0.0 --port 9001 --reload
fi