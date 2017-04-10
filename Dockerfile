FROM python:3

COPY src/* src/
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD [ "python", "./src/test.py" ]