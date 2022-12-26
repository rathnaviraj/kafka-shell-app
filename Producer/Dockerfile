FROM python:alpine

LABEL AUTHOR="Supun Viraj"
LABEL AUTHOR_EMAIL="rathnavira@gmail.com"

RUN pip install kafka-python Faker

RUN mkdir /usr/share/app

WORKDIR /usr/share/app

COPY producer.py producer.py

ENTRYPOINT ["python3","-u","producer.py"]