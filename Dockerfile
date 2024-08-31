FROM python:3.10.12-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input

# RUN python manage.py migrate

# RUN python seed.py