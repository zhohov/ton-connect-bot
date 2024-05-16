FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /bot

COPY pyproject.toml poetry.lock /bot/
RUN pip install --upgrade pip && pip install poetry
RUN poetry install --no-root

COPY . /bot/

RUN poetry run python src/main.py