FROM python:alpine

LABEL AUTHOR="Supun Viraj"
LABEL AUTHOR_EMAIL="rathnavira@gmail.com"

RUN pip install kafka-python

RUN mkdir /usr/share/app

WORKDIR /usr/share/app

COPY consumer.py consumer.py

ENTRYPOINT ["python3","-u","consumer.py"]