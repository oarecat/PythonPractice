#第0011题:敏感词文本文件filtered_words.txt,里面的内容为以下内容,当用户输入敏感词语时,则打印出Freedom,否则打印出Human Rights.

userInput = input("请输入文字：")

#增加的encoding = "utf-8"表示读取文件时按照UTF-8的编码方式
filterWords = open("C:\\GitHub\\PythonPractice\\filtered_words.txt" , "r" , encoding="utf-8").read().split(",")

if userInput in filterWords:
    print ("Freedom")
else:
    print ("Human Rights")
