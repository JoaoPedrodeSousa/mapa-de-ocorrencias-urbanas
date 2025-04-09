FROM python:3.13-slim-bookworm

WORKDIR /app

COPY ./requirements.txt /app

RUN python -m pip install --upgrade pip && pip install -r ./requirements.txt

COPY . .

ENV FLASK_APP=app.py

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0"]