FROM python:3.11.2-slim-buster

ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install -y -V vim curl gcc dnsutils iputils-ping
RUN apt-get install --fix-broken
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN curl -sSL https://install.python-poetry.org/ | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false
COPY . /app
EXPOSE 8000