import json
import os

import logging
from kafka import KafkaConsumer

event = os.environ.get('EVENT_KEY', '')

assert event, 'Event key must be specified as environment variable'

tokens = os.environ.get('TOKENS', '').split(',')
bootstrap_servers = os.environ.get('KAFKA_SERVERS', 'localhost:9092').split(',')


def main():
    consumer = KafkaConsumer('raw_topics', group_id=event, value_deserializer=lambda m: json.loads(m.decode('ascii')))

    for tweet in consumer:
        logging.info('Tweet: %s' % tweet)


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )
    main()