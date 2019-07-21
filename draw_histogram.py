from skimage import io
import os
import matplotlib.pyplot as plt
import numpy as np
import math

filepath = 'result/target/'
#
ratio_total = 0
data = []
for img in os.listdir(filepath):
    input = io.imread(filepath+img)
    input1 = io.imread('result/input/' + img)
    pixel = int(input1.mean())
    ratio = input.mean()/pixel

    data.append(ratio)
    print(ratio,img)

data = np.array(data)
plt.hist(data, bins=60, normed=5, facecolor="blue", edgecolor="black", alpha=0.7)

plt.xlabel("pixel")
plt.ylabel("number")
plt.title("distribution")
plt.show()
