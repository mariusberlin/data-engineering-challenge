from kafka import KafkaConsumer, KafkaProducer
import json

sys.path.insert(1, 'C:\Users\mpull\Desktop\bakdata_coding\utils')
from utils import *

#1. consumes the reports from the topic reports
#2. extracts the desired value (in this case age)
#3. publishes the values into the topic results


#create consumer, join a consumer group 'value_processing' for dynamic partition assignment
consumer = KafkaConsumer(
    'reports',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='value_processing',
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

    producer.send('results', {None : topic_entry})










