#coding=utf-8
'''
Environment requirement: ubunutu 16.04, python2.7

pip install wget
pip install subprocess
'''
from __future__ import print_function
import urllib
import re
import os
import wget
import subprocess
import argparse

#py抓取页面图片并保存到本地

parser = argparse.ArgumentParser(description='Download data from FIVE-K website')
parser.add_argument('--savepath',               type=str,   help='path to save data',      default='Expert_C/')
parser.add_argument('--format',           default='tif' ,     type=str,   help='dng,tif or hdr',      required=False)
parser.add_argument('--index',           default=0 ,     type=int,   help='index of download',      required=False)

args = parser.parse_args()

#获取页面信息
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
# https://data.csail.mit.edu/graphics/fivek/img/tiff16_c/a0001-jmac_DSC1459.tif
#通过正则获取图片
def getImg(html):
    reg = r"img/tiff16_c/.{0,50}?\."+args.format
    # prepare for jpg
    #<img src="http://icvl.cs.bgu.ac.il/wp-content/uploads/2016/08/omer_0331-1104chs.-20513258_1-200x215.jpg">
    # reg = r"http://icvl.cs.bgu.ac.il/.{0,120}?\.jpg"

    imgre = re.compile(reg)
    imglist_pre = re.findall(imgre,html)
    imglist=sorted(set(imglist_pre), key = imglist_pre.index)

    imglist = imglist[1000*args.index:1000*(args.index+1)]
    print (imglist,'\n')
    print ('Total file_num:', len(imglist))

    #循环把图片存到本地
    print('Downloading...')
    print(args.index)
    x=1
    for imgurl in reversed(imglist):
        #保存到本地
        try:
            cmd = 'wget ' '-c '+ 'https://data.csail.mit.edu/graphics/fivek/'+imgurl +' -P '+ args.savepath
            print (cmd)
            status = subprocess.call(cmd,shell= True)
            if status != 0:
                print (imgurl[42:-4],"failed")
                continue
            print ('success')

            print (x, end=' ')
            if x % 30 == 0:
                print('\n')
        except IOError:
            print(imgurl[42:-4])
        x += 1

if __name__ == '__main__':

    html = getHtml("https://data.csail.mit.edu/graphics/fivek/")
    # http://icvl.cs.bgu.ac.il/img/hs_pub/4cam_0411-1640-1.hdr

    image = getImg(html)

    print (image)
