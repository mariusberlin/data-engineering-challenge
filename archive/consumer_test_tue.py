from kafka import KafkaConsumer, KafkaProducer
import json
from utils import *

import os
import pandas as pd
import csv

#create consumer, group: m-group for parallelisation with consumer 2
consumer = KafkaConsumer(
    'results',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='value_proccessing',
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x : json.dumps(x).encode('utf-8'))

for message in consumer :
    data = message.value

    report_text = data['null']
    report,value = get_value("age", report_text)
    topic_entry = [report, value]

    print("Processed text: ", report_text)
    print("Topic entry: ", topic_entry)



    producer.send('tuejsonresult', {None : topic_entry})










