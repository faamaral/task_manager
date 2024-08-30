#!/usr/bin/env bash
# Sair caso erro
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate