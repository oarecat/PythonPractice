# 第0000题:将你的QQ头像(或者微博头像)右上角加上红色的数字,类似于微信未读信息数量那种提示效果
from PIL import Image , ImageFont , ImageDraw

#读入一个图片文件
image = Image.open("C://Users//hanch//Desktop//1.jpg")
#获得图片的尺寸
w , h = image.size
#设置偏移量
offset = 30
#生成imageDraw对象
imageDraw = ImageDraw.Draw(image)
#生成imageFont对象
imageFont = ImageFont.truetype("C://WINDOWS//Fonts//SIMYOU.TTF" , 50)
#在图片上添加文字或数字
imageDraw.text((w-offset , offset/2) , "4" , (255,0,0) , font=imageFont)
#保存图片
image.save('C://Users//hanch//Desktop//A.jpg' , 'JPEG')