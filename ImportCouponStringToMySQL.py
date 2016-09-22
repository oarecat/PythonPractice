#第0002题:将0001题生成的200个激活码或者优惠券）保存到 MySQL 关系型数据库中。

import pymysql , random

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
        insertCoupon(couponString)

#向本机的MySQL插入数据，参数为需要插入的优惠码
def insertCoupon(couponString):
    config = {
          'host':'127.0.0.1',
          'port':3306,
          'user':'root',
          'password':'tszx11hcm',
          #等待链接的数据库名称
          'db':'coupon',
          }
    #connect函数的参数使用可变参数传入 *表示为元组参数传入 **表示为字典参数传入
    connect = pymysql.connect(**config)
    #根据链接生成游标
    cursor = connect.cursor()
    #执行SQL语句
    cursor.execute("INSERT INTO coupon (couponKeyString) VALUES ('%s')" % couponString)
    connect.commit()
    #关闭游标和数据库的链接
    cursor.close()
    connect.close()

couponMake(10 , 200)