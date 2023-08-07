FROM            python:3.11.2-buster

WORKDIR /usr/src/app
COPY . .

RUN apt-get update; exit 0
RUN apt-get install vim net-tools iftop -y

# RUN update-ca-certificates
# RUN apt-get install libmediainfo-dev -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt