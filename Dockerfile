FROM python:latest

WORKDIR /usr/src/app/

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY ./entrypoint.sh .

COPY . .
