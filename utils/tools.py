import cv2
import os

#SET Working Directory Into the Project
project_dir = "../"

os.chdir(project_dir)
#Change the Directories in Constants
from utils.constants import *

def mkdir():
    os.mkdir(frame_dir1)
    os.mkdir(frame_dir2)


def CreateVideoFrames(videoFile,frame_dir):
 vidcap = cv2.VideoCapture(videoFile)
 success,image = vidcap.read()
 count = 0
 while success:
  cv2.imwrite(frame_dir+"/frame%d.jpg" % count, image) # save frame as JPEG file      
  success,image = vidcap.read()
  print('Frame written', success,",",count)
  count += 1

