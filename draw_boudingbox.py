import cv2
from PIL import Image,ImageChops

fname = '5_8.jpg'



## Set the bouding box position
x1_1=470;x1_2=570;y1_1=920;y1_2=1020
x2_1 =1850; x2_2=1950;y2_1=750;y2_2=850

def draw(fname):
    img = cv2.imread(fname)
    img =cv2.rectangle(img, (x1_1,y1_1), (x1_2,y1_2), (0,0,255), 4)
    img = cv2.rectangle(img, (x2_1, y2_1), (x2_2, y2_2), (0, 255, 0), 4)
    cropImg1 = img[y1_1:y1_2,x1_1:x1_2]
    cv2.imwrite("crop5_8_1.jpg", cropImg1)
    cropImg2 = img[y2_1:y2_2,x2_1:x2_2]
    cv2.imwrite("crop5_8_2.jpg", cropImg2)

    cv2.imwrite("5_8_rec.jpg", img)
    img =cv2.resize(img,(1000,1000))
    cv2.imshow('img',img)
    cv2.waitKey(0)

def fuse(fname1,fname2,fname3):
    base_img = Image.open(fname1)
    # box = (0, 0, 400, 400)  # 底图上需要P掉的区域
    # box1 = (0,1136,400,1536)

    # 加载需要P上去的图片
    tmp_img = Image.open(fname2)
    region = tmp_img
    region = region.resize((1024,1024))

### 合并图片
    tmp_img1 = Image.open(fname3)
    region1 = tmp_img1
    region1 = region1.resize((1024, 1024))
    img3 = Image.new('RGB', (2048,1536+1024))
    img3.paste(base_img, (0, 0))
    img3.paste(region, (0,1536 ))
    img3.paste(region1, (1024, 1536))
    # base_img.paste(region, box)
    # base_img.paste(region1, box1)

    img3.save('out8.jpg')


# draw(fname)


fname1 = '5_8_rec.jpg'
fname2 = 'crop5_8_2.jpg'
fname3 = 'crop5_8_1.jpg'
fuse(fname1,fname2,fname3)
