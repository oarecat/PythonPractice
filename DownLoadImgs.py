#第0013题:用Python写一个爬图片的程序

from html.parser import HTMLParser
from urllib import request

#下载处理函数
def downLoadImg(imgName , imgUrl):
    #将解析出来的URL地址按照"."来分割然后取结尾的元素
    suffix = imgUrl.split(".")[-1]
    #判断URL的结尾是不是常见的图片后缀名若是则进入处理函数，若不是则输出url并提示错误信息
    if suffix in ["jpg" , "png" , "gif"]:
        #拼接图片的保存路径
        imgFilePath = "C:\\Users\\hanch\\Desktop\\img\\" + str(imgName) + "." + suffix
        imgRequest = request.Request(imgUrl)
        imgData = request.urlopen(imgRequest).read()
        #"wb"表示以二进制的方式写入文件
        imgFile = open(imgFilePath , "wb")
        imgFile.write(imgData)
        imgFile.flush()
        imgFile.close()
    else:
        print ("%s传输失败！！！" %(imgUrl))
        return

class MyHTMLParser(HTMLParser):
    #记录已下载的文件个数
    imgNum = 0
    def handle_starttag(self, tag, attrs):
        if tag == "img":
            for name , value in attrs:
                if name == "src":
                    self.imgNum = self.imgNum + 1
                    downLoadImg(self.imgNum , value)

myHTMLParser = MyHTMLParser()
htmlRequest = request.Request('http://tieba.baidu.com/p/2166231880')
htmlData = request.urlopen(htmlRequest).read()
htmlData = str(htmlData)
myHTMLParser.feed(htmlData)