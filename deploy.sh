#!/bin/bash
pip3 freeze > requirements.txt
python3 manage.py clear_cache
python3 manage.py collectstatic --noinput
gcloud app deploy

