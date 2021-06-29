from time import sleep
import json
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))


new_list = ["temperature",":"]

for e in range(2):
    object = str(e)
    new_list.append(object)
    print(new_list)
    producer.send('AllNew', new_list)
    sleep(3)

