# Execute a worker and gunicorn thread.
# https://stackoverflow.com/questions/3004811/how-do-you-run-multiple-programs-in-parallel-from-a-bash-script
. secrets.sh
cd $SERVER_LOCATION
source "env/bin/activate"
python manage.py collectstatic
gunicorn --workers=3 -b 127.0.0.1:9998 labwatch.wsgi:application


# gunicorn dashing.wsgi:application --workers=1 -b 127.0.0.1:9999 & celery -A dashing worker -l info && fg