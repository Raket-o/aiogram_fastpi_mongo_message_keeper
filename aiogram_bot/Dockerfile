FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip "poetry"
RUN poetry config virtualenvs.create false --local
COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY ./aiogram_bot ./aiogram_bot

WORKDIR /aiogram_bot
#WORKDIR .

#ENTRYPOINT ["python", "main.py"]
#ENTRYPOINT ["python3", "bot/main.py"]
#ENTRYPOINT ["python", "aiogram_bot/main.py"]
ENTRYPOINT ["./docker-entrypoint.sh"]
