import cv2
import numpy as np

img1 = cv2.imread('GT.png')
img2 = cv2.imread('MIRNet.png')
res = np.abs(np.float32(img1)-np.float32(img2))
cv2.imwrite('res_MIRNet.png',res)
