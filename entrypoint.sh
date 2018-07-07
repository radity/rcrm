#!/bin/sh

wait-for-it db:5432 -- python manage.py migrate --noinput
#python manage.py compilemessages
python manage.py initdb
exec "$@"
