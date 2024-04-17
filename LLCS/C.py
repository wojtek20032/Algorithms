#!/usr/bin/env python
# coding: utf-8

import skimage as sk
import numpy as np
from matplotlib import pyplot as plt


img = sk.io.imread('two_objects.png')
img = sk.img_as_ubyte(img)

object1Anchor = (200, 200)
object2Anchor = (220, 500)

def label(image, min_number_of_pixels_per_object=10):
    currentLabel = 1
    labels = np.zeros(image.shape, dtype=np.uint8)
    for i in range(1, len(image)):
        if image[i][0] == 255:
            labels[i][0] = currentLabel
            currentLabel += 1
        for j in range(1, len(image[i])):
            if image[i][j] == 255:
                b = labels[i-1][j]
                c = labels[i][j-1]
                if b == 0 and c == 0:
                    labels[i][j] = currentLabel
                    currentLabel += 1
                elif b != 0:
                    labels[i][j] = b
                elif c != 0:
                    labels[i][j] = c

                if b != 0 and c != 0 and b != c:
                    labels[labels == c] = b

    for i in range(1, currentLabel):
        if np.count_nonzero(labels == i) < min_number_of_pixels_per_object:
            labels[labels == i] = 0

    return labels

labels = label(img)

imageColored = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
objectLabels = np.unique(labels)
colors = [(0, 0, 0), (255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
colors = {label: colors[i] for i, label in enumerate(objectLabels)}
for k in objectLabels:
    for i in range(len(labels)):
        for j in range(len(labels[i])):
            if labels[i][j] == k:
                imageColored[i][j] = colors[k]

plt.imshow(imageColored)
plt.title('Colored objects')
plt.xticks([]), plt.yticks([])
plt.show()

sk.io.imsave('colored_objects.png', imageColored)

