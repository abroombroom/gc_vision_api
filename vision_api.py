@author __author__: "Alyse Kim"
@version __version__: "1.0"
@created __date__ : "2018/08/20"

import io
import os
from PIL import Image

import ipywidgets as widgets
from IPython.display import display

from google.cloud import vision
from google.cloud.vision import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "" #specify the path for your api key

client = vision.ImageAnnotatorClient()

filename = '' #specify the path + image file name

with io.open(filename, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content = content)
response = client.label_detection(image = image)
labels = response.label_annotations

for label in labels:
    print (label.description)
