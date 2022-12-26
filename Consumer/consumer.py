import time
import json
import os

from kafka import KafkaConsumer


BOOTSTRAP_SERVER = os.environ.get('BOOTSTRAP_SERVER')
KAFKA_TOPIC = os.environ.get('KAFKA_TOPIC')


def main():
    print(f'Consuming from Server {BOOTSTRAP_SERVER} | Topic {KAFKA_TOPIC}')
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers=[BOOTSTRAP_SERVER],
        auto_offset_reset='earliest', 
        group_id='C1'
    )

    for message in  consumer:
        print(f'User - {json.loads(message.value)}')


if __name__ == "__main__":
    main()