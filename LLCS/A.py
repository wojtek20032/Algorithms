import numpy as np
import matplotlib.pyplot as plt
import skimage as ski

# read image
img = ski.io.imread('two_objects.png')
img = ski.img_as_ubyte(img)

# count pixels which belongs to object
object_1_anchor = (200, 200)
object_2_anchor = (220, 500)

def label(img, min_number_of_pixels_per_object=10):
    cur_label = 1
    labels = np.zeros(img.shape, dtype=np.uint8)
    for i in range(1, len(img)):
        if img[i][0] == 255:
            labels[i][0] = cur_label
            cur_label += 1
        for j in range(1, len(img[i])):
            if img[i][j] == 255:
                b = labels[i-1][j]
                c = labels[i][j-1]
                if b == 0 and c == 0:
                    labels[i][j] = cur_label
                    cur_label += 1
                elif b != 0:
                    labels[i][j] = b
                elif c != 0:
                    labels[i][j] = c

                if b != 0 and c != 0 and b != c:
                    labels[labels == c] = b

    for i in range(1, cur_label):
        if np.count_nonzero(labels == i) < min_number_of_pixels_per_object:
            labels[labels == i] = 0

    return labels


def count_pixels(labels, anchor):
    label = labels[anchor]
    return np.count_nonzero(labels == label)

labels = label(img)

print('Number of pixels in object 1:', count_pixels(labels, object_1_anchor))
print('Number of pixels in object 2:', count_pixels(labels, object_2_anchor))

plt.imshow(img, cmap='gray')
plt.title('Original image')
plt.xticks([]), plt.yticks([])
plt.show()
