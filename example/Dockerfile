FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y netcat

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Adds our application code to the image
COPY . code
WORKDIR code

EXPOSE 8000
