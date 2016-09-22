# 第0001题:做为Apple Store App独立开发者,你要搞限时促销,为你的应用生成激活码(或者优惠券),使用Python如何生成200个激活码(或者优惠券)?

import random

#优惠码生成函数参数为优惠码的位数(长度)
def couponStringMaker(couponLenght):
    couponString = ""
    i = 0
    while i < couponLenght:
        i = i + 1
        couponString = couponString + chr(random.randint(65,90))
    return couponString

#优惠码生成函数参数为优惠码的位数(长度),需要生成的优惠码数量
def couponMake(couponLenght , couponNum):
    i = 0
    while i < couponNum:
        i = i + 1
        couponString = couponStringMaker(couponLenght)
        print (couponString)

couponMake(10 , 200)