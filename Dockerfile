FROM python:3.9-slim

WORKDIR /penTweepy

COPY . .

RUN pip install Flask

CMD ["python", "run.py"]