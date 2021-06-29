

# Bakdata coding challenge

1. Created two additional rules for temperatur & age
2. Built a command line application the extract the desired value for a provided medical text (in folder command line application)
3. Built the Apache Kafka integration for extracting the values from the medical text in topic 1 and write the results in topic 2


## Requirements

```
python
kafka-python

```

## Usage

```python
'''

1. Rules:

- established for temperature and age
- in alignment with existing rule: prefix, suffix and exception values are defined (non exhaustive)

2. Command Line Appplication:

- take two arguments (path of the medical report & the desired value) and outputs the value for that specific report
- generic example: python medicalreport_cla.py "medicalreport_path.txt" "value"
- specific example: python medicalreport_cla.py "./medreport1.txt" "temperature" or python medicalreport_cla.py "./medreport2.txt" "age"

3. Kafka Implementation:

- initalize zookeeper&kafka
- create topic medicalreports with desired amount of partitions (two in this example)
- run the scripts:
  - consumer_reports_producer_reports (parallellisation: run them as many times as you created paritions in the topic "reports" & "results", here 2 times)
  - consumer_results (to see if results are correctly writen in topic "results")
  - producer_reports (to publish the medical reports in the topic "reports" to simulate a data stream)


All commands for the command line can be found in the txt.file: kafka commands
