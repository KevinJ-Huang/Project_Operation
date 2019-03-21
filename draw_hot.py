from skimage import io,color
import matplotlib.pyplot as plt
import numpy as np

plt.figure()
img = io.imread('4/res_my.png')
img = color.rgb2gray(img)*255
plt.imshow(img, cmap=plt.cm.hot, vmin=0, vmax=80)
plt.colorbar()
plt.imsave('res_my.png',img,cmap=plt.cm.hot, vmin=0, vmax=80)
plt.show()
