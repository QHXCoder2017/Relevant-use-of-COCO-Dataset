# 提取COCO关键点并保存在h5文件中 Date: 2018.11.22

from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import os
import h5py
from PIL import Image
from PIL import ImageDraw


pylab.rcParams['figure.figsize'] = (8.0, 10.0)

# initialize COCO api for person keypoints annotations
dataDir = 'path/filename'
dataType = 'train_val_new'
annFile = '{}/{}.json'.format(dataDir, dataType)
coco_kps = COCO(annFile)

# display COCO categories and supercategories
cats = coco_kps.loadCats(coco_kps.getCatIds())
nms = [cat['name'] for cat in cats]
print('COCO categories: \n{}\n'.format(' '.join(nms)))

nms = set([cat['supercategory'] for cat in cats])
print('COCO supercategories: \n{}'.format(' '.join(nms)))

# get all images containing given categories, select one at random
catIds = coco_kps.getCatIds(catNms=['person'])
imgIds = coco_kps.getImgIds(catIds=catIds)
print('there are %d images containing human' % len(imgIds))


def getBndboxKeypointsGT():
    '''
    firstRow = ['imagename','bndbox','nose',
            'left_eye','right_eye','left_ear','right_ear','left_shoulder','right_shoulder',
            'left_elbow','right_elbow','left_wrist','right_wrist','left_hip','right_hip',
            'left_knee','right_knee','left_ankle','right_ankle']
    keypointsWriter.writerow(firstRow)'''
    h5_imgname = []
    h5_bndbox = []
    h5_keypoints = []
    for i in range(len(imgIds)):
        imageNameTemp = coco_kps.loadImgs(imgIds[i])[0]
        imageName = imageNameTemp['file_name'].encode('raw_unicode_escape')
        img = coco_kps.loadImgs(imgIds[i])[0]
        annIds = coco_kps.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)
        anns = coco_kps.loadAnns(annIds)
        personNumber = len(anns)

        for i in range(personNumber):
            i = str(anns[i]['image_id'])
            while len(i) < 12:
                i = '0'+i
            i = i+'.jpg'
            temp3 = []
            for h in range(len(i)):
                tmp = ord(i[h])
                temp3.append(tmp)
            temp3 = np.array(temp3)
            temp3 = temp3.astype(np.float64)
            h5_imgname.append(temp3)
        for j in range(personNumber):
            temp = []
            b = anns[j]['bbox']
            b[2] = int(b[0]+b[2])
            b[3] = int(b[1]+b[3])
            b[0] = int(b[0])
            b[1] = int(b[1])
            temp.append(b)
            h5_bndbox.append(temp)
            temp1 = []
            for k in range(len(anns[j]['keypoints'])):
                if(k % 3 == 0):
                    temp2 = []
                if (k % 3 != 2):
                    temp2.append(anns[j]['keypoints'][k])
                if (k % 3 == 2):
                    temp1.append(temp2)
            h5_keypoints.append(temp1)

    h5_imgname = np.array(h5_imgname)
    h5_bndbox = np.array(h5_bndbox)
    h5_keypoints = np.array(h5_keypoints)
    h5file = h5py.File('path/filename.h5', 'w')
    h5file.create_dataset('imgname', data=h5_imgname)
    h5file.create_dataset('bndbox', data=h5_bndbox)
    h5file.create_dataset('part', data=h5_keypoints)
    h5file.close()


if __name__ == "__main__":
    print('Writing bndbox and keypoints to h5 files..."')
    getBndboxKeypointsGT()
