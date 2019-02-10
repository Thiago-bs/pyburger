#!/bin/bash
exec gunicorn pyburger.wsgi:application \
    --name django_server \
    --bind 0.0.0.0:80 \
    --workers 3 \