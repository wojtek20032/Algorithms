#!/usr/bin/env python
# coding: utf-8


from matplotlib import pyplot as plt
import numpy as np
from skimage import color
from skimage import io
from skimage import morphology
import cv2
from PIL import Image 

  
im = cv2.imread("two_objects.png")
plt.imshow(im, cmap='gray' )
plt.show()

  
height, width = im.shape[:2] 

imArea = height * width

object1 = im[0:350,0:320]
plt.imshow(object1, cmap='gray' )
plt.show()

numWhitePixelObject1= np.sum(object1 == (255,255,255))
print(numWhitePixelObject1)
areaObjc1 = (numWhitePixelObject1 / imArea )* 100

print("Area object 1 = ",areaObjc1)

object2 = im[0:440,400:650]
plt.imshow(object2, cmap='gray' )
plt.show()

numWhitePixelObject2= np.sum(object2 == (255,255,255))
print(numWhitePixelObject2)

areaObjc2 = (numWhitePixelObject2 / imArea )* 100
print("Area object 2 = ",areaObjc2)
