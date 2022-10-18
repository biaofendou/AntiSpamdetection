#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        :2022/2/17 10:03
# @Author      :weiz
# @ProjectName :coco_evaluate
# @File        :add_key_word.py
# @Description :
# Copyright (C) 2021-2025 Jiangxi Institute Of Intelligent Industry Technology Innovation
import json
import glob
import os


def add_key(annotation_path, dest_path):
    """
    coco数据集添加缺损字段
    :param annotation_path:
    :param dest_path:
    :return:
    """
    with open(annotation_path, 'r') as load_f:
        s_json = json.load(load_f)

    # print(s_json["annotations"])


    for i, value in enumerate(s_json["annotations"]):
        s_json["annotations"][i]["iscrowd"] = 0
        print(s_json["annotations"][i])

    with open(dest_path, "w") as dump_f:
        json.dump(s_json, dump_f)


def check_set(annotation_path, images_path):
    """
    检测coco数据集的标注文件和图片是否一致
    :param annotation_path:
    :param images_path:
    :return:
    """
    with open(annotation_path, 'r') as load_f:
        s_json = json.load(load_f)

    annotation_image_list = []
    for images_value in s_json["images"]:
        # print(images_value)
        annotation_image_list.append(images_value["file_name"])

    image_path_list = glob.glob(os.path.join(images_path, "*.png"))
    image_list = []
    for image_path in image_path_list:
        image_list.append(os.path.basename(image_path))

    print(len(annotation_image_list))
    print(len(annotation_image_list))
    print(set(annotation_image_list) - set(image_list))
    print(set(image_list) - set(annotation_image_list))


annotation_path = "E:\\Python_workspace\\yolov5\\data\\train\\train\\labels.json"
dest_path = "E:\\Python_workspace\\yolov5\\dataHanding\\annotationsAll.json"
images_path = "E:\\Python_workspace\\yolov5\\data\\self\\data"
if __name__ == "__main__":
    # add_key(annotation_path, dest_path)
    check_set(dest_path, images_path)