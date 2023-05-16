#!/bin/sh

set -e


python manage.py collectstatic --noinput

touch /htms_website/logs/cron.log

touch /etc/cron.d/htms_cronjob

# Define the cron job command
CRON_COMMAND="/py/bin/python3 /htms_website/manage.py shell -c 'from HTMS_App.task import automated_techinicans_report; automated_techinicans_report()'"

# Define the timing for the cron job (runs every minute)
CRON_TIMING="0 0 * * *"

# Define the cron job file name
CRON_FILE="/etc/cron.d/htms_cronjob"

# Define the error log file name and location
LOG_FILE="/htms_website/logs/cron.log"

# Write the cron job command and timing to the cron job file, and redirect the standard error output to the log file
echo "$CRON_TIMING root $CRON_COMMAND 2>$LOG_FILE" > $CRON_FILE

cron

uwsgi --ini /htms_website/uwsgi/uwsgi.ini
