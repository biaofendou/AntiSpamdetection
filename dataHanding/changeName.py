import os,sys                       #导入模块
def add_prefix_files():             #定义函数名称
    mark = 18292               #准备添加的前缀内容
    for foldName, subfolders, filenames in os.walk(path):     #用os.walk方法取得path路径下的文件夹路径，子文件夹名，所有文件名
        for filename in filenames:     #遍历列表下的子文件夹名
            if  filename!= sys.argv[0]:  #代码本身文件路径，防止脚本文件放在path路径下时，被一起重命名
                # if filename.endswith():   #当文件名以.txt后缀结尾时
                    mark+=1
                    os.rename(os.path.join(foldName,filename),os.path.join(foldName,str(mark)+'.jpg'))  #重命名文件
                    print (filename,"has been renamed successfully! New name is: ",str(mark)+'.jpg')  #输出提示

if __name__ == '__main__':
    path = r'../data/self/earphones'   #运行程序前，记得修改主文件夹路径！
    add_prefix_files()         #调用定义的函数，注意名称与定义的函数名一致