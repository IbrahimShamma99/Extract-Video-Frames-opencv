import cv2 
import os


class ProcessImage():
    
    def Bluring(image):
        blur = cv2.blur(image,(7,7))
        return blur
    def show(img):
        cv2.imshow('Source Image', img)
    def thresh(img):
        

