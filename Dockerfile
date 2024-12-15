FROM python:3.12-slim-bullseye

ENV PYTHONUNBUFFERED 1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

RUN pip install poetry

WORKDIR /app
COPY pyproject.toml poetry.lock /app/

RUN poetry install --no-dev

COPY . /app/