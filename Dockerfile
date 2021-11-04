FROM python:3.8

WORKDIR /usr/src
COPY . ./app
RUN cd /usr/src/app && pip install --no-cache-dir -r requirements.txt
WORKDIR /usr/src/app/dash