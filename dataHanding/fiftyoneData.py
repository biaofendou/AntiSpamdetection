import fiftyone.zoo as foz
import fiftyone as fo

dataset = foz.load_zoo_dataset(
    "coco-2017",
    split="validation",  # 下载训练集validation
    label_types=["detections"],  # 下载目标检测标注文件
    classes=['cell phone','book','clock','backpack'],  # 下载数据集中的某几类别
    # max_samples=50,  # 下载图片数目
    only_matching=True,  # 只下载匹配到类别的图片
    dataset_dir="../data/CoCo",  # 下载到当前目录
)
session = fo.launch_app(dataset)
session.wait()