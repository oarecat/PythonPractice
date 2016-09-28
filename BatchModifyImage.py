# 第0005题:你有一个目录,装了很多照片,把它们的尺寸变成都不大于iPhone5分辨率的大小.
from  PIL import Image
import  os

filePath = "C://Users//hanch//Desktop//1"
# os.walk()函数由3个返回值：1、父目录路径 2、路径下的文件夹名 3、路径下的文件名
files = os.walk(filePath)
for parentFileName , dirNames , fileNames in files:
        for dirName in dirNames:
            # os.path.join()方法将父目录路径和路径下的文件名或文件夹名拼成完整路径
            print (os.path.join(parentFileName , dirName))
        for fileName in fileNames:
            image = Image.open(os.path.join(parentFileName , fileName))
            w , h = image.size
            image.thumbnail((w//2, h//2))
            mDir = os.path.join("C://Users//hanch//Desktop//2" , fileName)
            image.save(mDir , 'JPEG')