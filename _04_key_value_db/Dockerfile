FROM redis

COPY src/* src/
COPY requirements.txt requirements.txt

RUN apt-get update
RUN apt-get install -y python3
RUN pip install -r requirements.txt

CMD [ "python3", "./src/test.py" ]