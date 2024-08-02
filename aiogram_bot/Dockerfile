FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip "poetry"
RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY ./config_data ./aiogram_bot/config_data
COPY .env .env
COPY ./aiogram_bot ./aiogram_bot

CMD ["python3", "aiogram_bot/main.py"]