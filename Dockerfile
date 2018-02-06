FROM python:3.4-alpine

WORKDIR /app

ADD /src /app

RUN pip3 install tweepy

CMD ["python", "app.py"]