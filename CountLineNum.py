#第0007题:有个目录,里面是你自己写过的程序,统计一下你写过多少行代码.包括空行和注释,但是要分别列出来.
# -*- coding: utf-8 -*-

fileData = open("C:\\Users\\hanch\\Desktop\\text.java" , "r")
codeLineNum = 0
zhushiLineNum = 0
for line in fileData:
    #用if...in...来判断字符串中是否包含xxx
    if '//' in line :
        codeLineNum = codeLineNum + 1
        zhushiLineNum = zhushiLineNum + 1
    else:
        codeLineNum = codeLineNum + 1
print(codeLineNum , zhushiLineNum)