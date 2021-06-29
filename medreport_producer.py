import re

import os
from utils import *
from kafka import KafkaProducer
import json


# print(report)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x : json.dumps(x).encode('utf-8'))


def send_value(producer_instance, topic_name, key,data) :
    try :
        #key_bytes = bytes(key, encoding='utf-8')
        #value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key , data)
        #producer_instance.flush()
        print('Value extraction successfully.')
    except Exception as ex :
        print('Exception in value extraction')
        print(str(ex))


medreport_paths = []

for root, dirs, files in os.walk(os.path.abspath("C:/Users/mpull/Desktop/bakdata_coding/medreports")) :
    for file in files :
        medreport_paths.append(os.path.join(root, file))


for report in medreport_paths :  # for continuous integration add check for timestamp
    with open(report) as f :
        report = f.read()

    send_value(producer,"AllNew",b"report",report)

