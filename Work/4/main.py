# -*- coding: UTF-8 -*-
from imageai.Detection import ObjectDetection
import os
import socket
import keras
import shutil

keras.backend.clear_session()
execution_path = os.getcwd()
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel(detection_speed="fastest")
print("loading successful!!!")

def P(path):
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, path),output_image_path=os.path.join(execution_path, "1.jpg"))
    for eachObject in detections:
        print(eachObject["name"])
        if eachObject["name"]=="car":
            shutil.copy(path,"./car/")
            print("OK")
            break
while True:
    try:
        rootdir = "./img/"
        list = os.listdir(rootdir)
        for i in range(0,len(list)):
            path = os.path.join(rootdir,list[i])
            if os.path.isfile(path):
                print(path)
                try:
                    P(path)
                except:
                    pass
                os.remove(path)
    except:
        pass
