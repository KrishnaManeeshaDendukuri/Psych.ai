from EmotionAPIIntegration import get_emotion
from videotofolder import get_frames
#from create_array import create_array
#from emotion_lists import emochap, emoshine, emodiv
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
#print(emotions)


def get_image_index():
    transfer_indices = []
    #transfer_indices_scary = []
    #transfer_indices_comic = []
    for i in range(len(emotions)):
        if required_emotion == "Scary":
            if emotions[i] in ["fear", "disgust", "sadness", "anger"]:
                #transfer_indices_scary.append(folder_list[i])
                transfer_indices.append(folder_list[i])
        elif required_emotion == "Comic":
            if emotions[i] in ["happiness", "neutral", "surprise"]:
                #transfer_indices_comic.append(folder_list[i])
                transfer_indices.append(folder_list[i])
    #print(transfer_indices)
    #print(videofile)
    return transfer_indices
stylepaths = get_image_index()

#stylepaths_scary = get_image_index()[0]
#stylepaths_comic = get_image_index()[1]
"""
if videoname == "cc.mp4":
    stylepaths = emochap
elif videoname == "shining.mp4":
    stylepaths = emoshine
elif videoname == "diversity.mp4":
    stylepaths = emodiv
#print(stylepaths)
content = stylepaths
#stylepaths = get_image_index()
#stylepath = [stylepaths_scary, stylepaths_comic]
"""

for jpgfile in stylepaths:
    #print(jpgfile)
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
