# Dockerfile

# pull the official docker image
FROM python:3.9.6-buster

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get -y update \
    && apt -y upgrade \
    && apt-get -y install netcat gcc \
    && apt -y install gnupg2 wget vim \
    && apt-get -y install libgeos-dev \
    && apt -y update 

# install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN touch /app/dev.log
# copy project
COPY . .