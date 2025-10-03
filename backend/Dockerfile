FROM python:3.11-slim-bullseye

WORKDIR /code

COPY ./requirements /code/requirements

RUN apt-get update \
    # dependencies for building Python packages
    && apt-get install -y build-essential \
    # mariadb dependencies
    && apt-get install -y default-libmysqlclient-dev \
    # Additional dependencies
    && apt-get install -y telnet netcat-traditional libcairo2-dev \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade -r /code/requirements/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]