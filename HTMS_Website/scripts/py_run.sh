#!/bin/sh


set -e

python manage.py collectstatic --noinput\

uwsgi --ini /htms_website/uwsgi/uwsgi.ini
