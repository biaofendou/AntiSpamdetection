import json
json_labels=json.load(open('E:\\Python_workspace\\yolov5\\data\\train\\raw\\instances_train2017.json',"r"))
# E:\Python_workspace\yolov5\valid\train\raw\instances_train2017.json
print(json_labels["info"])