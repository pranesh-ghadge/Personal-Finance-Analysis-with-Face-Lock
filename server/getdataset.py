import numpy as np
import cv2
import time
import os
import shutil

timeout = 10
timeout_start = time.time()
cap = cv2.VideoCapture(0)

image_folder_path = "D:/Data Science Projects/Project 7/model/dataset/full_images/person/"

count_of_image = 658

while time.time() < timeout_start + timeout :
    ret, frame = cap.read()

    image = np.zeros(frame.shape, np.uint8) 
    image = frame

    cv2.imshow('frame',image)

    if cv2.waitKey(1) == ord('q'):
        break

    imagepath = image_folder_path + "training_image" + str(count_of_image) + ".png"

    cv2.imwrite(imagepath, image)
    count_of_image +=1


    # sending 'image' to backend to classify it
    # it can return two results: empty list-not identified, filled dictionary/list-identified

    # code:
    # result = send_to_backend(image)
    # if isempty(result):
    #   continue
    # else:
    #   flag_to_indicate_that_image_is_classified = 1
    #   break


# if flag_to_indicate_that_image_is_classified == 1:
#   redirect to the homepage


# print(image.shape)
# print(image)