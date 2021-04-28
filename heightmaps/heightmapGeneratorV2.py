# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 19:40:30 2021

@author: hans_
"""
import png
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise
import numpy as np
import math
f = open('layeredtest2.png', 'wb')      # binary mode is important
xpix, ypix = 512,512
w = png.Writer(xpix, ypix, greyscale=True,bitdepth=16)
noise1 = PerlinNoise(octaves=3)
noise2 = PerlinNoise(octaves=6)
noise3 = PerlinNoise(octaves=12)
noise4 = PerlinNoise(octaves=24)

#xpix, ypix = 100, 100
pic = []
for i in range(xpix):
    row = []
    for j in range(ypix):
        noise_val =         noise1([i/xpix, j/ypix])
        noise_val += 0.5  * noise2([i/xpix, j/ypix])
        noise_val += 0.25 * noise3([i/xpix, j/ypix])
        noise_val += 0.125* noise4([i/xpix, j/ypix])

        row.append(noise_val)
    print("i "+str(i))
    pic.append(row)
#pic2=np.array(pic)
#print(np.amax(pic2))
#print(np.amin(pic2))
#plt.imshow(pic, cmap='gray')
#plt.show()


oldRange = 1 - -1
newRange = 65535 - 0
for x in range(xpix):
        for y in range(ypix):
            newValue = (pic[x][y] - -1) * newRange / oldRange
            pic[x][y] = math.floor(newValue)
            #print(math.floor(newValue))

        print("x "+str(x))
   # print(max)
w.write(f, pic)
f.close()
