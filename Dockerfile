FROM python:3.12-slim as builder

WORKDIR /app

COPY . .

RUN pip install -r requirements-webapp.txt

EXPOSE 5000

CMD [ "python3", "webapp.py" ]

