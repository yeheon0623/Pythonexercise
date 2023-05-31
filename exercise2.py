# @Time: 2023/1/31 13:22
# @Author: Yuxuan Wang
# @File :exercise2.py
# @Software: PyCharm

import random  # 调用随机库
# 用户
user = int(input('请输入：剪刀（0)、石头（1）、布（2）：'))

if user == 1 and user != 0:
    chinese = "石头"
elif user == 0:
    chinese = "剪刀"
else:
    chinese = "布"
print("你的输入为%s（%d）"%(chinese,user))
# 电脑
computer = random.randint(0,2)
print("随机生成数字为%d"%computer)
# 判断输赢
if user == 0:
    if computer == 1:
        print("哈哈，你输了")
    else:
        print("这次不算，再来一次吧")
elif user == 1:
    if computer > user:
        print("哈哈，你输了")
    else:
        print("这次不算，再来一次吧")
elif user == 2:
    if computer == 0:
        print("哈哈，你输了")
    else:
        print("这次不算，再来一次吧")