# USAGE
# python flipping.py minions.jpg

# import the necessary packages
import os
import cv2
import numpy as np
import imutils
import random 
import sys
from pathlib import Path
import shutil

dirpath = Path('C:/AugmentedImages/')
if dirpath.exists() and dirpath.is_dir():
    shutil.rmtree(dirpath)

#creating directory to save the images
root_dir = 'C:/AugmentedImages/'
list_ = ['RotatedImages', 'TranslatedImages', 'ContrastImages', 
'ColourAugmentationImages','NoiseImages','ScaledImages','Brightness','Saturation']
for folder in list_:
    os.makedirs(root_dir + folder)
#creating a Directory for storing Images
Rotatepath = 'C:/AugmentedImages/RotatedImages'
Translatedpath = 'C:/AugmentedImages/TranslatedImages'
Contrastpath = 'C:/AugmentedImages/ContrastImages' 
ColourAugmentpath = 'C:/AugmentedImages/ColourAugmentationImages'
NoiseImagespath = 'C:/AugmentedImages/NoiseImages'
ScaledImagespath = 'C:/AugmentedImages/ScaledImages'
Saturationpath = 'C:/AugmentedImages/Saturation'


'''if not os.path.exists(path):
    os.makedirs(path)'''

#reading the image as first argument
img = sys.argv[1]

# load the image and show it
image = cv2.imread(img)
cv2.imshow("Original", image)

##Rotate and saving the image
#Rotation by 90

rotated = cv2.flip(image, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite(os.path.join(Rotatepath,"Rotate_90.jpg"),rotated)

#Rotation by 180
rotated = cv2.flip(image, cv2.ROTATE_180)
cv2.imwrite(os.path.join(Rotatepath,"Rotate_180.jpg"),rotated)

#Rotation by 270 
rotated = cv2.flip(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite(os.path.join(Rotatepath,"Rotate_270.jpg"),rotated)

##Rotating from 0 to 360 

for angle in np.arange(0, 360, 1):
	rotated = imutils.rotate_bound(image, angle)
	cv2.imwrite(os.path.join(Rotatepath,'Rotated_'+str(angle)+'.jpg'), rotated)



##translation
for i,j in zip(range(-100,100, 10),range(-100,100,10)):

	shifted = imutils.translate(image, i, j)
	cv2.imwrite(os.path.join(Translatedpath,'Shifted_'+str(i)+str(j)+'.jpg'), shifted)


#Brightneess and contast control 
#formula = >  new image = alpha* old image + beta (on every pixels)

for alpha in range(0,100):
	for beta in range(1,100):
		adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

		cv2.imwrite(os.path.join(Contrastpath,'Adjusted_'+str(alpha)+'.jpg'), adjusted)

#Noise image

'''img = sys.argv[1]
image = cv2.imread(img)
grey_imag = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def add_noise(grey_imag):
	# Getting the dimensions of the image
	row , col= cv.GetSize(grey_imag)
   # row , col = grey_imag.shape[:2]
      
    # Randomly pick some pixels in the
    # image for coloring them white
    # Pick a random number between 300 and 10000
number_of_pixels = random.randint(10,100)

for i in range(number_of_pixels):
        
        # Pick a random y coordinate
        y_coord=random.randint(0, row - 1)
          
        # Pick a random x coordinate
        x_coord=random.randint(0, col - 1)
          
        # Color that pixel to white
        grey_imag[y_coord][x_coord] = 255
          
    # Randomly pick some pixels in
    # the image for coloring them black
    # Pick a random number between 300 and 10000
number_of_pixels = random.randint(300 , 10000)
for i in range(number_of_pixels):
        
        # Pick a random y coordinate
        y_coord=random.randint(0, row - 1)
          
        # Pick a random x coordinate
        x_coord=random.randint(0, col - 1)
          
        # Color that pixel to black
        grey_imag[y_coord][x_coord] = 0

	

cv2.imwrite(os.path.join(NoiseImagespath,'Noise.jpg'), add_noise(grey_imag))'''
  