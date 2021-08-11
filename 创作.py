
brand = ("欢迎来到娱乐商城")
print("--------------------------",brand,"----------------------")
tips = ("未成年人禁止娱乐")
print("--------------------------",tips,"---------------------------")
nem = input("请输入您的名字：")
if nem=='阮红英':
    print('欢迎荣耀段位的大神来到娱乐城')
elif nem=='张宇航':
    print('欢迎王者20性段位的大神来到娱乐城')
elif nem=='王赛':
    print('欢迎王者段位10星的大神来到娱乐城')
elif nem=='诗磊':
     print('欢迎王者段位5星的大神来到娱乐城')
else:
    print('三分靠技术，七分靠运气')
age =input("请输入您的年龄：")
age = int(age)
if age >= 18:
    print("欢迎来到本娱乐城")
elif age >=0 and age<18:
    breakpoint("未成年人禁止娱乐")
else:
    breakpoint('未成年人禁止娱乐')

import random
num = random.randint(0, 1000)
count = 0
i = 1
gold = 5000
while i <= 20:
    count = count + 1
    chose = input("请输入本次猜的数据：")
    chose = int(chose)
    if chose > num:
        gold = gold - 500
        print("大了","金币剩余",gold)
    elif chose < num:
        gold = gold - 500
        print("小了","金币剩余",gold)
    else:
       gold = gold + 10000
       print("恭喜，本次猜中，本次幸运数字为:",num,"，本次猜了,"
             ,count,"次，","金币剩余",gold)
       break
















