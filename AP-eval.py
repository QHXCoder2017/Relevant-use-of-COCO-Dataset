from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import pylab
import numpy as np


pylab.rcParams['figure.figsize'] = (10.0, 8.0)
annType = ['segm', 'bbox', 'keypoints']
annType = annType[2]
prefix = 'person_keypoints' if annType == 'keypoints' else 'instances'
print('Annotation Type: %s' %(annType))

# running demo for bbox results
# initialize coco ground truth api          person_keypoints_val2017
annFile = 'path/name.json'

# dataType = 'val2017'
cocoGT = COCO(annFile)

# initialize COCO detection api           results
resFile = 'path/name.json'
cocoDT = cocoGT.loadRes(resFile)
imgIds = sorted(cocoGT.getImgIds())
# imgIds = imgIds[0:100]
# imgId = imgIds[np.random.randint(100)]

# runing evaluation
cocoEval = COCOeval(cocoGT, cocoDT, annType)
cocoEval.params.imgIds = imgIds
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()