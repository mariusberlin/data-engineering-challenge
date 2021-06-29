import re

import os
from utils import *
from kafka import KafkaProducer
import json


# print(report)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x : json.dumps(x).encode('utf-8'))


def send_value(producer_instance, topic_name, data) :
    try :
        #key_bytes = bytes(key, encoding='utf-8')
        #value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, data)
        #producer_instance.flush()
        print('Value extraction successfully.')
    except Exception as ex :
        print('Exception in value extraction')
        print(str(ex))

def process_reports(data_request) :
    medreport_paths = []
    data_pairs = []
    for root, dirs, files in os.walk(os.path.abspath("/medreports")) :
        for file in files :
            medreport_paths.append(os.path.join(root, file))

    for report in medreport_paths :  # for continuous integration add check for timestamp
        print(report)

        data_pair = (report, get_value(data_request, report))
        print(data_pair)
        #send value to topic
        send_value(producer,"AllNew",data_pair)

    print(data_pairs)


def get_value(data_request, report) :
    with open(report) as f :
        report = f.read()
        report = report.lower()

    if data_request == "temperature" :
        candidates = re.findall('\d{2,3}\.\d{1}', report)
        print(candidates)

        prefixes = ["temperature"]  # also covers:, "temperature is", "temperature was","temperature of", "temperature:"
        prefix_distance = 20
        suffixes = ["deg", "celsius", "fahrenheit"]  # also covers:"degree","degrees"
        suffix_distance = 15
        exception = ["down from", "gained", "increased", "decreased", "days ago",
                     "week ago"]  # includes increased by, increased to
        exception_distance = 30

    elif data_request == "age" :
        candidates = re.findall('\d{1,2}\-[a-z]{3,4}\-[o,l,d]{3}', report) + re.findall(
            '[e,x]{1,2}\-\d{2}\s[a-z]{3,5}', report)  # covers xx-year/week/day format and ex-XX weeks/week/day format

        prefixes = ["female", "male", "patient", "child",
                    "baby"]  # also covers:, "temperature is", "temperature was","temperature of", "temperature:"
        prefix_distance = 15
        suffixes = ["gentlemen", "women", "man", "male", "female"]  # also covers:"degree","degrees"
        suffix_distance = 15
        exception = ["father", "dad", "mother", "mom", "grandma", "grandpa", "sister", "brother", "uncle", "aunt",
                     "friend", "wife", "husband", "partner", "spouse"]
        exception_distance = 30

    return_values = []

    for candidate in candidates :

        cand_position = report.find(candidate)
        # print(cand_position)

        # check temperature prefix/suffix/exception
        prefix_state = prefix_check(report=report, cand_position=cand_position, prefixes=prefixes,
                                    prefix_distance=prefix_distance)
        suffix_state = suffix_check(report, candidate=candidate, cand_position=cand_position, suffixes=suffixes,
                                    suffix_distance=suffix_distance)
        exception_state = exception_check(report, candidate=candidate, cand_position=cand_position, exception=exception,
                                          exception_distance=exception_distance)

        if ((prefix_state == True) or (suffix_state == True)) & (exception_state == False) :
            # print(candidate)
            return_values.append(candidate)

    if len(return_values) == 1 :

        print((data_request).capitalize(), ": ", return_values[0])
        return return_values

    elif len(return_values) > 1 :
        print("Multiple values found: ", return_values)
        return return_values

    elif len(return_values) == 0 :
        return_values = ["nan"]
        print(return_values)
        return return_values
        print("No value was found.")

#run for "age" or "temperature"
process_reports("age")



#create kafka producer



#Test
#extracted_value = "age"
#data_pairs = process_reports(extracted_value)