

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

2. Command Line Appplication
- take two arguments (path of the medical report & the desired value) and outputs the value for that specific report
- generic example: python medicalreport_cla.py "medicalreport_path.txt" "value"
- specific example: python medicalreport_cla.py "./medreport1.txt" "temperature" or python medicalreport_cla.py "./medreport2.txt" "age"

3. Kafka implementation
- initalize zookeeper&kafka
- create topic medicalreports with desired amount of paritions (two in this example)
- run the scripts:
  - consumer_reports_producer_reports (run them as many times as you have paritions to ensure parallelisation)
  - cosumer_results (to see if results are correctly writen in topic "results")
  - producer_reports (to publish the medical reports in the topic "reports" to simulate a data stream)


All commands can be found in the txt.file: kafka commands
'''

import xai_vis.interact as interact

interact.vis(model,model_path,pixel_array)


#The calculation of the saliency maps may take up to 10 minutes depending on your GPU.


```

## Example
```python
import xai_vis.interact as interact
from vgg16_final import vgg16_model
from image_utils import resize


model = vgg16_model((30, 128, 128,1), 64, 2, 0.2, 2) #tensorflow model

model_path = "./storage/trained_models/t2_flair/vgg16_dummy.hdf5" #hdf5 format

image_path = "./storage/processed_data/3Dmri_dummy.npz"
imagedata = np.load(image_path, allow_pickle=True)
pixel_array = resize(imagedata) #output shape = (30, 128, 128)


interact.vis(model,model_path,pixel_array)
```

<img src="https://user-images.githubusercontent.com/51263484/112940011-cbe05f80-912c-11eb-97bd-7e776e645b65.png" width="550" height="396"> 
<img src="https://user-images.githubusercontent.com/51263484/112939970-b4a17200-912c-11eb-9c5b-ac51e0dfef12.png" width="550" height="396"> 
