import numpy as np
import os
import cv2
import re
from scipy import misc

path = "./scam"
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)', text) ]

def create_array(path):
    images = []
    folder = os.listdir(path)
    #print()
    #print(folder)

    for image in sorted(folder, key=natural_keys):
        img = cv2.imread(path+"/"+image)
        images.append(img)
    images = np.array(images)
    return images

print(create_array(path))