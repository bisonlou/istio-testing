FROM python:3.8.8-slim-buster

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5002

ENTRYPOINT [ "python", "app.py" ]
