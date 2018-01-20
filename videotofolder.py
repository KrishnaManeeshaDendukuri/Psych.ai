import cv2
import pathlib

videoname = input("Enter video name")

pathlib.Path('./'+videoname+"images").mkdir(parents=True, exist_ok=True)

path = "./"+videoname
#print(videofile)
def get_frames(path):
        count = 0
        cam = cv2.VideoCapture(path)
        print("Creating Video Folder")
        #success = True
        success, frame = cam.read()
        print(success)
        while success:
            success, frame = cam.read()
            if success:

                frame1 = cv2.resize(frame, (640, 480))
                #print 'Read a new frame: ', success
                cv2.imwrite("./"+videoname+"images"+"/%d.jpg" % count, frame1)  # save frame as JPEG file
                count += 1
            else:
                break


get_frames(path)
