FROM python:3.7-alpine

LABEL maintainer="Rüdiger Küpper <ruediger@kuepper.nrw"
LABEL com.example.version="1.0.0"
LABEL vendor1="9IT-Full-Service"
LABEL vendor2="Devops"
LABEL com.example.release-date="2020-11-09"
LABEL com.example.version.is-production="yes"

RUN apk add --no-cache gcc
RUN mkdir /app
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
