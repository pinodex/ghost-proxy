FROM python:3.7-alpine3.9

RUN apk add gcc musl-dev

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
