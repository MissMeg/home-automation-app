FROM python:3.8

ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0.0

RUN pip3 install pipenv

WORKDIR /usr/src/app

COPY Pipfile ./
COPY Pipfile.lock ./

RUN set -ex && pipenv install --deploy --system

COPY . /usr/src/app

EXPOSE 5000

CMD ["flask", "run"]