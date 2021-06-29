from time import sleep
import json
from kafka import KafkaProducer
import os

#Publishes the medical reports in the Topic: reports

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))


new_list = ["temperature",":"]
medreport_paths = []

for root, dirs, files in os.walk(os.path.abspath("../medreports")) :
    for file in files :
        medreport_paths.append(os.path.join(root, file))


for report in medreport_paths :  # for continuous integration add check for timestamp
    with open(report) as f :
        report = f.read()
        print(report)

    producer.send('reports', {None : report})



