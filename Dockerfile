FROM "python:3.12"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install "poetry==2.4.1"
RUN poetry config virtualenvs.create false --local
COPY poetry.lock pyproject.toml ./

RUN poetry install --no-root

COPY mysite ./

RUN python manage.py collectstatic --clear --noinput

