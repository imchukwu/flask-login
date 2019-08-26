FROM python:3.6-slim

RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev

RUN mkdir /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install --editable .

LABEL maintainer="Ike Chukwu <imchukwu@gmail.com>"

CMD gunicorn -c "python:config.gunicorn" "ids.app:create_app()"
