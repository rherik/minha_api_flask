FROM python:3.10-slim

WORKDIR /penTweepy

COPY . .

RUN pip install tweepy pandas

CMD ["python", "main.py"]