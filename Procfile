release: sh -c 'cd ./src/ && exec python manage.py migrate'
web: sh -c 'cd ./src/ && exec gunicorn servie.wsgi'