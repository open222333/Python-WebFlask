FROM            python:3.6.15-buster
MAINTAINER      AVnight Inc. <powpi2000@gmail.com>

WORKDIR /usr/src/app
COPY . .

RUN apt-get update; exit 0
RUN update-ca-certificates
RUN apt-get install vim net-tools iftop -y
RUN apt-get install libmediainfo-dev -y

RUN pip install -r requirements.txt