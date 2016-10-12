#第0012题:敏感词文本文件filtered_words.txt,里面的内容和0011题一样,当用户输入敏感词语,则用星号*替换,例如当用户输入[北京是个好城市],则变成[**是个好城市].

userInput = input("请输入文字：")

#增加的encoding = "utf-8"表示读取文件时按照UTF-8的编码方式
filterWords = open("C:\\GitHub\\PythonPractice\\filtered_words.txt" , "r" , encoding="utf-8").read().split(",")

for filterWord in filterWords:
    if filterWord in userInput:
        userInput = userInput.replace(filterWord , "*")
        print (userInput)
        break
    else:
        print (userInput)
        break
