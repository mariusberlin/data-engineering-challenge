from kafka import KafkaConsumer
from json import loads
import os
import pandas as pd
import csv

consumer = KafkaConsumer(
    'tuejsonresult',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='result_group',
    value_deserializer=lambda x : loads(x.decode('utf-8')))

for message in consumer :
    data = message.value
    print(data)









