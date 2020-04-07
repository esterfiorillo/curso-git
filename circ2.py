#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 15:45:05 2019

@author: esterfiorillo
"""

import numpy as np
import cv2
i=0
j=47
k=0
l=44
img = np.zeros((1024,1024,3), np.uint8)
for i in range (60):
    j=4
    for k in range (60):
        cv2.circle(img,(l, j), 2, (0,0,255), -1)
        j = j+10
    l = l+10
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

new_line
