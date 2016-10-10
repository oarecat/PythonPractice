#第0009题:一个HTML文件,找出里面的链接.
from html.parser import HTMLParser
from urllib import request

#定义HTMLParser类的子类
class MyHTMLParser(HTMLParser):

#覆写HTMLParser类中的方法作为事件处理函数(tag为标签,attrs表示属性,属性可能有多个)
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name , value in attrs:
                if name == "href":
                    print (value)
#生成MyHTMLParser类的对象
myHTMLParser = MyHTMLParser()
#生成URL请求对象
htmlRequest = request.Request('http://www.douban.com/')

htmlData = request.urlopen(htmlRequest).read()
htmlData = str(htmlData)

#为MyHTMLParser类的对象导入HTML代码
myHTMLParser.feed(htmlData)