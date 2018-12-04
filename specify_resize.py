from skimage.transform import resize
from skimage.io import imread
from skimage.io import imsave
from skimage.measure import compare_psnr
from skimage import img_as_uint
import os

def specify_resize(img,size):
    w, h = img.shape[0:2]
    if w < h:
        width, height = (size, int(size*h / w))
    else:
        width, height = (int(size*w / h), size)
    img = resize(img,(int(width), int(height)),mode='reflect')
    return img

def fine_resize(img, shape):
    w = shape[0]
    h = shape[1]
    img = resize(img, (int(w), int(h)), mode='reflect')
    return img


dir = 'test_input/'
dir2 = 'test_output/'
files = os.listdir(dir)
for file in files:
    rgb = imread(dir+file)
    rgb2 = imread(dir2+file)
    rgb_ = specify_resize(rgb,1080)
    rgb2_ = fine_resize(rgb2, rgb_.shape)
    imsave('input1080/'+file,img_as_uint(rgb_))
    imsave('output1080/'+file, img_as_uint(rgb2_))
