import numpy as np                   #module that will convert image to array
import cv2                           #module that will create a clear image


#we create a function that will perform adaptive thressholding. CHECK GOOLGE FOR SYNTAX
def preprocess_image(img):
 # below we take the image file suplied by user and convert it to grey using the cv2.cvtColor function. Check google for syntax
    gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR) #resize the grey image
# Use cv2 adaptive method to get a clear picture
    processed_image = cv2.adaptiveThreshold(
        resized,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        61,
        11
    )
    return processed_image
