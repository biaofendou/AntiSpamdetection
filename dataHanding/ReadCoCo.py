################################################
# 如果本身已经下载好了coco数据集，那么采用下面的方式来导入
################################################
import fiftyone as fo
pth_标签文件路径 = "E:\\Python_workspace\\yolov5\\data\\CoCo\\validation\\labels.json"  # 这边的标签文件是用的前面下载的。
pth_图片文件夹路径 = "E:\\Python_workspace\\yolov5\\data\\CoCo\\images\\valid"  # 这个文件夹中是我之前下载的coco数据集中val系列的所有照片

# Import the dataset
dataset = fo.Dataset.from_dir(
    dataset_type=fo.types.COCODetectionDataset,
    data_path=pth_图片文件夹路径,
    labels_path=pth_标签文件路径,
    classes=['cell phone','book','clock','backpack','person'],  # 指定载入猫的类别
    only_matching=True,  # 指定仅下载符合条件的图片，即含有猫的图片
)
# dataset.name = "coco2"
session = fo.launch_app(dataset)
session.wait()
