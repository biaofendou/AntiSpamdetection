#-----------------------------批量重命名图片------------------------------------
#-----------重命名《图片》《xml文件》《任何格式的文件》都可以自定义序号来命名------------
import os
'''
该路径存储原始的图片，重命名后会覆盖掉原始的图片，所以在重命名之前选择复制一份，以免被失误重命名
建议在路径中使用：\\ 双斜杠
'''
path = 'E:\\Python_workspace\\yolov5\\data\\self\\earphones'
# 绝对路径
filelist = os.listdir(path)
'''
起始数字，重命名的第一个文件的名字会加1
'''
i =581904
# 仅用于数字开头的图片命名方法
for item in filelist:
    #print('item name is ',item)
    # jpg\png\bmp\xml  任何格式都支持，但是需要手动修改格式类型
    if item.endswith('.jpg'):
        i = i + 1
        # 第一张图片命名为1.png
        name = str(i)
        # 将数字转换为字符串才能命名
        src = os.path.join(os.path.abspath(path),item)
        # 原始图像的路径
        dst = os.path.join(os.path.abspath(path),name + '.jpg')
        # 目标图像路径
    try:
        os.rename(src,dst)
        print('rename from %s to %s'%(src,dst))
        # 将转换结果在终端打印出来以便检查
    except:
        continue