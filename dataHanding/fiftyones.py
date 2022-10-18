'''
 ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard',
 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']
 'cell phone','book','clock','backpack'
'''

from pycocotools.coco import COCO

dataDir = 'C:/Users/11527/Desktop/目标检测数据集/train2017'
# dataType='val2017'
dataType = 'train2017'
dataJson = 'C:/Users/11527/Desktop/目标检测数据集/annotations_trainval2017/annotations'
annFile = '{}/instances_{}.json'.format(dataJson, dataType)

# initialize COCO api for instance annotations
coco = COCO(annFile)

# display COCO categories and supercategories
cats = coco.loadCats(coco.getCatIds())
cat_nms = [cat['name'] for cat in cats]
print('number of categories: ', len(cat_nms))
print('COCO categories: \n', cat_nms)

# 统计各类的图片数量和标注框数量
for cat_name in cat_nms:
    catId = coco.getCatIds(catNms=cat_name)  # 1~90
    imgId = coco.getImgIds(catIds=catId)  # 图片的id
    annId = coco.getAnnIds(catIds=catId)  # 标注框的id
    print(catId,imgId,annId)