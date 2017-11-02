# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 20:54:35 2017
Generate a random phase mask of a mixture of two images.
The ratio between the Final Intensity generated on the by the SLM is input.
The ratio of pixels is the square root of the Final Intensity.
@author: Harsh Jain

"""

import numpy as np
from PIL import Image

global countA
global countB

countA=0
countB=0

add= 'C:/Users/Admin/Desktop/Jump_hysteresis/'  # Enter YOUR Address here. Note the forward slash.
img1=add+'img1.bmp'
img2=add+'img2.bmp'


def NUM(ratio,N=2):
    global countA    
    global countB
    NUM=int(np.random.rand()*1000)
    if NUM>int(np.sqrt(ratio)/(np.sqrt(ratio)+1)*1000):
        countA+=1
        return 0
    else:
        countB+=1
        return 1
def RandomPhaseMask(add1,add2,ratio=1.0,n=2):

    screenx=796 #Check
    screeny=600
    
    Images=[]
    Images+=[np.asarray(Image.open(img1))]
    Images+=[np.asarray(Image.open(img2))]
    
    output=np.zeros([screeny,screenx])
    for k in range(screeny):
        for l in range(screenx):
            if l<800:
                output[k][l]=Images[NUM(ratio)][k][l]
            else:
                output[k][l]=0
    return output

Output=RandomPhaseMask(img1,img2,ratio=1.0)
