from kafka import KafkaProducer
from faker import Faker
import json
import time
import os

BOOTSTRAP_SERVER = os.environ.get('BOOTSTRAP_SERVER')
KAFKA_TOPIC = os.environ.get('KAFKA_TOPIC')

fake = Faker()

def get_user():
    return {
        'name': fake.name(),
        'address': fake.address()
    }

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

def main():
    print(f'Server {BOOTSTRAP_SERVER} | Topic {KAFKA_TOPIC}')
    producer = KafkaProducer(bootstrap_servers=[BOOTSTRAP_SERVER], value_serializer=json_serializer)
    while True:
        user = get_user()
        print(user)
        producer.send(KAFKA_TOPIC, user)
        time.sleep(5)


if __name__ == "__main__":
    main()