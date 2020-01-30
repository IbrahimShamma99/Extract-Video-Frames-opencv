import cv2
import os

#SET Working Directory Into the Project

project_dir = "../CV_IEEE/"

os.chdir(project_dir)
#Change the Directories in Constants
from utils.constants import *

frame_dir1 = FramesFile+'/'+vid1+"_"+"FRAME"
frame_dir2 = FramesFile+'/'+vid2+"_"+"FRAME"


def mkdir():
    os.mkdir(frame_dir1)
    os.mkdir(frame_dir2)


def vidtoframes(videoFile,frame_dir):
 vidcap = cv2.VideoCapture(videoFile)
 success,image = vidcap.read()
 count = 0

 while success:
  cv2.imwrite(frame_dir+"/frame%d.jpg" % count, image) # save frame as JPEG file      
  success,image = vidcap.read()
  print('Frame written', success,",",count)
  count += 1

Video1 = VideoFile+"/"+vid1+ext
Video2 = VideoFile+"/"+vid2+ext


if __name__ == '__main__':
    mkdir()
    vidtoframes(Video1,frame_dir1)
    vidtoframes(Video2,frame_dir2)
