FROM python:3
RUN mkdir /app
WORKDIR /app
# Installing OS Dependencies
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev
RUN pip install -U pip setuptools
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
ADD . /app/
# Django service
EXPOSE 8000