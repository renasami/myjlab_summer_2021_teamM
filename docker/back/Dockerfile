FROM python:3.8.2-buster

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

# pip installs
COPY ./docker/back/requirements.txt requirements.txt
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libgl1-mesa-dev
RUN pip install -r requirements.txt

WORKDIR /app