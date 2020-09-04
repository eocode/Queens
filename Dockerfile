FROM python:3.8-alpine

WORKDIR /code

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers postgresql-dev bash
COPY app/requirements/prod.txt app/requirements/prod.txt

RUN pip install -r app/requirements/prod.txt

EXPOSE 5000
COPY . .
CMD ["flask", "run"]