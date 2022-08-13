FROM python:3.8-alpine

WORKDIR /code

# set working directory
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apk update \
    && apk --no-cache add gcc mysql-dev python3-dev musl-dev

RUN pip install --upgrade pip setuptools

COPY ./requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8001