#!/bin/sh

python manage.py migrate --noinput
python manage.py compilemessages
python manage.py initdb
exec "$@"
