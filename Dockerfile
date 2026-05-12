FROM python:3.12-alpine 

COPY ./requirement.txt /tmp/requirement.txt

RUN pip install -r /tmp/requirement.txt 

COPY ./src /app

CMD python /app/app.py