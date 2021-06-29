from kafka import KafkaConsumer
from json import loads
import os
import pandas as pd
import csv

consumer = KafkaConsumer(
    'AllNew',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

if os.path.isfile('C:/Users/mpull/Desktop/bakdata_coding/patient_information.csv'):
    pass
else:
    data = []
    df = pd.DataFrame(data,columns = ['report','temperature','age'])
    df.to_csv('patient_information.csv', index=False)


with open(r'test.csv', 'a', newline='') as csvfile:
    for message in consumer :

        data = message.value
        print(data[1])
        print(data[2])

        #message = message.value

        fieldnames = ['Record','Temperature']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writerow({'Record':data[0], 'Temperature':data[1]})







