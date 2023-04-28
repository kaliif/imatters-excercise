FROM python:3.11-alpine3.17
ENV PYTHONBUFFERED 1

# install poetry system-wide, fine in small demo projects
RUN python -m pip install poetry


WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# install deps, don't bother creating virtualenv
RUN POETRY_VIRTUALENVS_CREATE=false poetry install --no-root --without dev

COPY . /code