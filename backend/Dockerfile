FROM python:3.7-alpine

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

ENV FLASK_RUN_HOST 0.0.0.0

CMD ["flask", "run"]
