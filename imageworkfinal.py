from EmotionAPIIntegration import get_emotion
from videotofolder import get_frames
import os
import re
import shutil
import subprocess
import cv2
import tensorflow as tf


required_emotion = input("Enter the required emotion")
videoname = input("Enter the name of the file")

path = "./" + videoname + "images"
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [atoi(c) for c in re.split('(\d+)', text)]

def get_folder_details():
    folder = sorted(os.listdir(path), key=natural_keys)
    return folder


emotions = get_emotion()

def get_image_index():
    transfer_indices = []
    for i in range(len(emotions)):
        if required_emotion == "Scary":
            if emotions[i] in ["fear", "disgust", "sadness", "anger"]:
                transfer_indices_scary.append(folder_list[i])
                transfer_indices.append(folder_list[i])
        elif required_emotion == "Comic":
            if emotions[i] in ["happiness", "neutral", "surprise"]:
                transfer_indices.append(folder_list[i])
    
    return transfer_indices
stylepaths = get_image_index()

stylepaths_scary = get_image_index()[0]
stylepaths_comic = get_image_index()[1]

for jpgfile in stylepaths:
    shutil.copy(path+"/"+jpgfile, "./styletransfer/styleimages")
if required_emotion == "Scary":
    value = "scary"
elif required_emotion == "Comic":
    value = "comic/udnie.ckpt"
elif required_emotion == "Diversify":
    value = "diversity/rain_princess.ckpt"
subprocess.call(["python", "/home/harsha/Desktop/Microsoft/styletransfer/evaluate.py",
              "--in-path", "/home/harsha/Desktop/Microsoft/styletransfer/styleimages",
              "--out-path", "/home/harsha/Desktop/Microsoft/styletransfer/styleoutput",
              "--checkpoint", "/home/harsha/Desktop/Microsoft/styletransfer/checkpoints/"+value])
print("Style Transfer Complete")
outpath = "./styletransfer/styleoutput"

output = os.listdir(outpath)

for y in sorted(output, key=natural_keys):
    shutil.copy(outpath+"/"+y, path+"/"+y)

def dumpvideo():
    os.chdir(path)
    subprocess.call(["ffmpeg -r 30 -f image2 -i %0d.jpg -vframes 830 -vcodec libx264 -crf 25 -pix_fmt yuv420p video.mp4"],shell=True)

dumpvideo()
print("Video Created!")
