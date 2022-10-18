import re  #为了正则表达式
import requests#请求网页url
import os #操作系统
num=0    #给图片名字加数字
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        'Cookie':'',#这里需要大家根据自己的浏览器情况自行填写
        'Accept':'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9'
        }  #请求头，谷歌浏览器里面有，具体在哪里找到详见我上一条csdn博客
#图片页面的url
url='https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word=%E5%A4%B4%E5%83%8F'
#通过requests库请求到了页面
html=requests.get(url,headers=header)
#防止乱码
html.encoding='utf8'
#打印页面出来看看
print(html.text)

html=html.text
pachong_picture_path= ''
if not os.path.exists(pachong_picture_path):
    os.mkdir(pachong_picture_path)



res=re.findall('"objURL":"(.*?)"',html)  #正则表达式，筛选出html页面中符合条件的图片源代码地址url
for i in res:   #遍历
    num=num+1       #数字加1，这样图片名字就不会重复了
    picture=requests.get(i)       #得到每一张图片的大图
    file_name='../data/earphone/'+str(num)+".jpg"   #给下载下来的图片命名。加数字，是为了名字不重复
    f=open(file_name,"wb")    #以二进制写入的方式打开图片
    f.write(picture.content)   # 往图片里写入爬下来的图片内容，content是写入内容的意思

    print(i)    #看看有哪些url
f.close()      #结束f文件操作