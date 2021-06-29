

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
Provide model, trained model and pixel array in a Jupyter Notebook.

Provide model and trained model with identical architecture.
Provide 3D pixel_array as numpy array in the same shape as the input size of the 3D model.
Pixel_array dimensions: (depth, length, width) or (1, depth, length, width,1); depth = dimension of interactive slider.
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
