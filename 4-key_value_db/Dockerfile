FROM redis

COPY src/* src/
COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install python3
RUN pip install -r requirements.txt

RUN redis-server &

EXPOSE 6379:6379


CMD [ "python3", "./src/test.py" ]