FROM python:3

COPY src/* src/
COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y redis-server
RUN service redis-server start
RUN pip install -r requirements.txt

EXPOSE 6379:6379


CMD [ "python3", "./src/test.py" ]