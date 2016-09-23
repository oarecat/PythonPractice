# 第0004题:任一个英文的纯文本文件，统计其中的单词出现的个数

# open()函数用来读取一个文件
wordFile = open("C://Users//hanch//Desktop//1.txt" , "r")
# 读取整个文件中的内容
words = wordFile.read()
# 文章字数统计值初始化
wordNum = 1
#遍历文件中读取到的字符
for word in words:
#文章统计字数分词条件：出现空格，逗号，句号，感叹号，分号，问号
    if  word == " " or word == "," or word == "." or word == "!" or word == ";" or word == "?":
        wordNum = wordNum + 1
print (wordNum)
# 关闭文件读取流
wordFile.close()