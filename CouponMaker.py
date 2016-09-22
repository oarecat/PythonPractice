# 第0001题:做为Apple Store App独立开发者,你要搞限时促销,为你的应用生成激活码(或者优惠券),使用Python如何生成200个激活码(或者优惠券)?

import random

code = chr(random(65 , 90))

print (code)