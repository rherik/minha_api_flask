FROM python:3.10-slim

EXPOSE 5000

WORKDIR /app

COPY . .

RUN pip install Flask

CMD ["flask", "run", "--host", "0.0.0.0"]