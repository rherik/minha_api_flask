FROM python:3.9-slim

WORKDIR /penTweepy

COPY . .

RUN pip install tweepy pandas

CMD ["python", "main.py"]