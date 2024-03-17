FROM python:3.10-bookworm

RUN mkdir /usr/src/app/
WORKDIR /usr/src/app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
