import os
import cv2
import json
import xml.dom.minidom
import xml.etree.ElementTree as ET

data_dir = 'E:\\Python_workspace\\yolov5\\data\\self'  # 根目录文件，其中包含image文件夹和box文件夹（根据自己的情况修改这个路径）

image_file_dir = os.path.join(data_dir, 'valid')
# print(image_file_dir)

xml_file_dir = os.path.join(data_dir, 'Annotations')

annotations_info = {'images': [], 'annotations': [], 'categories': []}

# categories_map = {'holothurian': 1, 'echinus': 2, 'scallop': 3, 'starfish': 4}
categories_map = {'earphone': 80}

for key in categories_map:
    categoriy_info = {"id": categories_map[key], "name": key}
    annotations_info['categories'].append(categoriy_info)

all_file_names = [image_file_name.split('.')[0]
                  for image_file_name in os.listdir(image_file_dir)]

all_file_names.sort(key=lambda x: int(x.split('.')[0]))
# print(os.listdir(image_file_dir))
print(all_file_names)

# ps：ann_id表示instance的排序，从6399开始
ann_id = 581905
for i, file_name in enumerate(all_file_names):

    image_file_name = file_name + '.jpg'
    xml_file_name = file_name + '.xml'
    image_file_path = os.path.join(image_file_dir, image_file_name)
    xml_file_path = os.path.join(xml_file_dir, xml_file_name)

    image_info = dict()
    image = cv2.cvtColor(cv2.imread(image_file_path), cv2.COLOR_BGR2RGB)
    height, width, _ = image.shape

    # ps:id与file_name保持一致，581905
    image_info = {'file_name': image_file_name, 'id': i + 581905,
                  'height': height, 'width': width}
    annotations_info['images'].append(image_info)

    DOMTree = xml.dom.minidom.parse(xml_file_path)
    collection = DOMTree.documentElement

    names = collection.getElementsByTagName('name')
    names = [name.firstChild.data for name in names]

    xmins = collection.getElementsByTagName('xmin')
    xmins = [xmin.firstChild.data for xmin in xmins]
    ymins = collection.getElementsByTagName('ymin')
    ymins = [ymin.firstChild.data for ymin in ymins]
    xmaxs = collection.getElementsByTagName('xmax')
    xmaxs = [xmax.firstChild.data for xmax in xmaxs]
    ymaxs = collection.getElementsByTagName('ymax')
    ymaxs = [ymax.firstChild.data for ymax in ymaxs]

    object_num = len(names)

    for j in range(object_num):
        if names[j] in categories_map:

            # ps:这里image_id相当于上面image_info里的id
            image_id = i + 581905
            x1, y1, x2, y2 = int(xmins[j]), int(ymins[j]), int(xmaxs[j]), int(ymaxs[j])
            x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

            if x2 == width:
                x2 -= 1
            if y2 == height:
                y2 -= 1

            x, y = x1, y1
            w, h = x2 - x1 + 1, y2 - y1 + 1
            category_id = categories_map[names[j]]
            area = w * h

            annotation_info = {"id": ann_id, "image_id": image_id, "bbox": [x, y, w, h], "category_id": category_id,
                               "area": area, "iscrowd": 0}
            annotations_info['annotations'].append(annotation_info)
            ann_id += 1  #

with  open('./annotationsAll.json', 'w')  as f:
    json.dump(annotations_info, f, indent=4)

print('---整理后的标注文件---')
print('所有图片的数量：', len(annotations_info['images']))
print('所有标注的数量：', len(annotations_info['annotations']))
print('所有类别的数量：', len(annotations_info['categories']))
