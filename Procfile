web: sh -c 'cd project && exec gunicorn project.wsgi:application --bind 0.0.0.0:$PORT --workers 1'

# Toggle next line to start Celery in a worker process
worker: sh -c 'cd project && exec celery -A project worker --beat -l info'
