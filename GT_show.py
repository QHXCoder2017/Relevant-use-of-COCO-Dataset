from pycocotools.coco import COCO
import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import time

time1= time.time()
annFile = '/home/myubuntu/Desktop/姿态估计标注0张-30张/new.json'
dataDir1 = '/home/myubuntu/Desktop/姿态估计标注0张-30张'

coco_kps = COCO(annFile)
catIds = coco_kps.getCatIds(catNms=['person'])
imgIds = coco_kps.getImgIds(catIds=catIds)
for i in imgIds:
    #i=30#np.random.randint(0, len(imgIds))
    #a=imgIds[i]
    img = coco_kps.loadImgs(i)[0]
    annIds = coco_kps.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
    anns = coco_kps.loadAnns(annIds)
    plt.figure(i)
    I = io.imread('%s/%s' % (dataDir1,img['file_name']))
    plt.imshow(I)
    plt.axis('off')
    coco_kps.showAnns(anns)
    #plt.show()
    plt.savefig('/home/myubuntu/Desktop/姿态估计标注0张-30张/GT/%s'% (i))
    plt.close()
time2=time.time()
print('spent t = %.2f min'%((time2-time1)/60))



