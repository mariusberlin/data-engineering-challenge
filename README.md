

# Bakdata coding challenge

1. Created two additional rules for "temperature" & "age"
2. Built a command line application the extract the desired value for a provided medical report (in folder command line application)
3. Built the Apache Kafka integration for extracting the value "age" from the medical report in topic 1 and write the results in topic 2


## Requirements

```
kafka
zookeeper
python
kafka-python
```

## Usage

```

1. Rules:

- established for temperature and age
- in alignment with existing rule: prefix, suffix and exception values are defined (non-exhaustive)

2. Command Line Appplication:

- take two arguments (path of the medical report & the desired value) and outputs the value for that specific report
- generic example: python medicalreport_cla.py "medicalreport_path.txt" "value"
- specific example: 
    - python medicalreport_cla.py "temperature" "./medreports/medreport1.txt"
    - python medicalreport_cla.py "age" "./medreports/medreport2.txt"

3. Kafka Implementation:

- initalize zookeeper&kafka
- create topic medicalreports with desired amount of partitions (two in this example)
- implementation for "age" value
- run the scripts:
  - consumer_reports_producer_reports (parallellisation: run them as many times as you created paritions in the topic "reports" & "results", here 2)
  - consumer_results (to see if results are correctly writen in topic "results")
  - producer_reports (to publish the medical reports in the topic "reports" to simulate a data stream)
- all necessary command line commands can be found in the txt.file: kafka commands

```

