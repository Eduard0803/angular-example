FROM python:3.11.4-slim-bullseye

RUN pip install poetry==1.4.2
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock /app/src/
WORKDIR /app/src

RUN poetry install
COPY . /app/src/

CMD ["python", "server.py"]
