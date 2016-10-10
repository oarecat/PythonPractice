#第0006题:你有一个目录,放了你一个月的日记,都是txt,为了避免分词的问题,假设内容都是英文,请统计出你认为每篇日记最重要的词.

import collections

fileData = open("C://Users//hanch//Desktop//text.txt" , "r")
#按照空格将文章分割开
words = fileData.read().split()
count = collections.Counter(words)
print (count)