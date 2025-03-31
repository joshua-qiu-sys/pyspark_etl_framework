from confluent_kafka import Producer
from random import choice
import time
import logging
from read_kafka_producer_cfg import KafkaProducerCfgReader

logger = logging.getLogger(f'random_data_generator')

def produce_message():

    producer_cfg_reader = KafkaProducerCfgReader()
    producer_props_cfg = producer_cfg_reader.read_producer_props_cfg()
    print(f'Producer properties: {producer_props_cfg}')

    producer = Producer(producer_props_cfg)

    def delivery_callback(err, msg):
        if err:
            print(f'ERROR: Message delivery failed: {err}')
        else:
            topic = msg.topic()
            key = msg.key().decode('utf-8')
            value = msg.value().decode('utf-8')
            print(f'SUCCESS: Message delivery succeeded: {{"topic": {topic}, "key": {key}, "value": {value}}}')

    topic = 'uncatg_landing_zone'
    products = ['computer', 'television', 'smartphone', 'book', 'clothing', 'alarm clock', 'batteries', 'headphones',
                'toothpaste', 'shampoo', 'laundry detergent', 'paper towels', 'charger', 'sunscreen', 'instant noodles',
                'packaged snacks', 'light bulb', 'bottled water', 'air freshener', 'cooking oil', 'canned soup']

    poll_interval = 3
    flush_interval = 15
    curr_time = time.time()
    last_poll_time = curr_time
    last_flush_time = curr_time

    count = 0
    while True:
        try:
            key = str(products.index(choice(products)))
            value = choice(products)
            producer.produce(topic, value, key, callback=delivery_callback)
            print(f'Sent data to buffer: {{"topic": {topic}, "key": {key}, "value": {value}}}')
            print(f'Count: {count}')
            count += 1
        except BufferError:
            print(f'Buffer is full. Pausing for 2 seconds to allow messages to be sent from buffer before resuming.')
            time.sleep(2)

        curr_time = time.time()
        if curr_time >= last_poll_time + poll_interval:
            print('Producer is polling. Handling delivery callback responses from brokers...')
            producer.poll(poll_interval)
            last_poll_time = curr_time
        if curr_time >= last_flush_time + flush_interval:
            print('Producer is flushing records to brokers. Blocking current thread until completion...')
            producer.flush()
            last_flush_time = curr_time

        time.sleep(1)

if __name__ == '__main__':
    produce_message()