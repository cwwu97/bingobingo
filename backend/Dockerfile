FROM python:3.7-alpine

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

ENV FLASK_RUN_HOST 0.0.0.0

ENV GOOGLE_APPLICATION_CREDENTIALS="db/bingodis-7466969cd012.json"

CMD ["flask", "run"]
