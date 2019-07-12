import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import time
import json
import re


l_pair = [[16, 14], [14, 12], [17, 15], [15, 13], [12, 13], [6, 12], [7, 13],
          [6, 7], [6, 8], [7, 9], [8, 10], [9, 11], [2, 3], [1, 2], [1, 3], [2, 4]
          [3, 5], [4, 6], [5, 7]]

time1 = time.time()
annFile = 'path/name.json'
imageDir = 'path/name.jpg'
f = open(annFile, encoding='utf-8')
jsonFile = json.load(f)
length = len(jsonFile)
string = jsonFile[0]['image']
img_id = re.findall(r"\d+\d*", string)

I = io.imread(imageDir)
plt.imshow(I)
plt.axis('off')

for k in range(0, length):
    sks = np.array(l_pair)-1
    keypoints = jsonFile[k]['keypoints']
    kp = np.array[keypoints]
    x = kp[0::3]
    y = kp[1::3]
    for sk in sks:
        plt.plot(x[sk], y[sk], linewidth=0.5, color=[1, 1, 0])
plt.show()
plt.close()
time2 = time.time()
print('time cost = %.2f min' % (time2-time1)/60)
print('well done!')
