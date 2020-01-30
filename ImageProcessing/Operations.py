import cv2 
import os
import matplotlib.pyplot as plt

#If it doesn't work Change the Directories in Constants

from utils.constants import *

from ProcessImage import ProcessImage

frame_dir1 = FramesFile+'/'+vid1+"_"+"FRAME"

images=os.listdir(frame_dir1)

tst = images[0]
tst = cv2.imread(frame_dir1+'/'+tst)
tst = tst[:,:,::-1]

'''
def main():
'''    
src = cv2.imread(frame_dir1+'/'+images[0])
img = src.copy()

if __name__ == '__main__':
    #process()
    blur = ProcessImage.Bluring(img)
