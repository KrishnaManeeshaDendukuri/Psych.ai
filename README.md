# Psych.ai
Contributers : [Sree Harsha Nelaturu](https://github.com/TheBigFundamental), [Aparna Krishnakumar](https://github.com/Aparnaakk), [Anith Patel](https://github.com/anithp), Maneesha Dendukuri.

Making use of Deep Learning in Image Processing specifically Neural Style Transfer in order to create a tool which can be used to act as an aid for people with hearing disabilities and serve as a bridge for people of different cultures.
## Getting Started

Clone the Repository, following which please clone the following repository:
> [Fast Style Transfer](https://github.com/lengstrom/fast-style-transfer) - For fast style transfer which is applied to frames.
> Create an Azure account and acquire a key for the Microsoft Cognitive Emotion API which needs to be used in the EmotionAPIIntegration.py

### Prerequisites
<ol>
  <li> Tensorflow
  <li> Numpy
  <li> OpenCV
  <li> CUDA
</ol>

### File Requirements and Description:
<ol>
  <li> videofolder.py - creates a folder containig frames of the image.
  <li> create_array.py - creates numpy array of images
  <li> EmotionAPIIntegration.py - Uses Microsoft Cognitive Emotion API in order to analyze sentiments of the frames in 
        image folder.
  <li> imageworkfinal.py - Main script to be utilized for the completely automated process of selection and input of video, and   
       subsequent generation of video.
</ol>

## Working of the Model :
The input video is taken from the side of the user, he selects an enhancement he requires, which consists of "Scary" and "Comic" in the current iteration of the software, following this, the video is converted into frames and stores them in it a folder, following this it runs the emotion API on the frames, and the frames which contain the emotions related to enhancement sought are copied to a new folder, following which style transfer is applied, and subsequently they are replaced in the original folder and a video is compiled. Fully automated, works with Python 3.5.2 and runs on Tensorflow-GPU.


## Testing the Model:

In order to use the system please clone the repository and that of fast style transfer, replaced directory links to the folders
Create two folders, "styleimage" and "styletransferimages" and place the checkpoint file for style in the checkpoints files.
Checkpoints for "Scary" and "Comic" have been provided. Following this run imageworkfinal.py, ensure CUDA is installed for speedy computatition.

## Examples:

Diversify:
<iframe class="imgur-embed" width="100%" height="480" frameborder="0" src="https://i.imgur.com/PxFPz6N.gifv#embed">
</iframe>

Scary
