# @Time: 2023/2/16 12:36
# @Author: Yuxuan Wang
# @File :exercise5.py
# @Software: PyCharm

# Python将多人分配进房间
import random

girl = ["欧阳娜娜", "杨幂", "佘诗曼", "迪丽热巴", "钟嘉欣"]
room = [[], [], []]

print("你旗下的女艺人有",end="")
for girl_name in girl:
    print(girl_name,end="、")
print("\b")

# 邀请女孩进房间
for girl_name in girl:
    number = random.randint(0,2)
    room[number].append(girl_name)

roomA_len = len(room[0])
roomB_len = len(room[1])
roomC_len = len(room[2])

print("你好，我是客服王宇轩！\n请输入以下命令进行查询\na代表打印所有房间信息；b代表查询房间号；c代表查询女艺人")
print("-"*50)
order = input("请输入命令：")

if order == "a":
    d = 0
    for i in range(0,2+1):
        if i == 0:
            print("房间%d有%d人"%(i,roomA_len))
            if roomA_len != 0:
                print("名字为",end="")
                for i in room[i]:
                    print(i,end="、")
                print("\b")
            print("*"*50)
        if i == 1:
            print("房间%d有%d人"%(i,roomB_len))
            if roomB_len != 0:
                print("名字为", end="")
                for i in room[i]:
                    print(i, end="、")
                print("\b")
            print("*" * 50)
        if i == 2:
            print("房间%d有%d人"%(i,roomC_len))
            if roomC_len != 0:
                print("名字为", end="")
                for i in room[i]:
                    print(i, end="、")
                print("\b")
            print("*" * 50)

elif order == "b":
    room_number = int(input("请输入你要查询的房间号："))
    print("-" * 50)
    print("该房间一共有%d人" % len(room[room_number]))
    if len(room[room_number]) != 0:
        print("名字为",end="")
    for i in room[room_number]:
        print(i,end="、")
    print("\b")

elif order == "c":
    name = input("请输入你要查询的女艺人名字:")
    print("-" * 50)
    save = 100
    if name in room[0]:
        save = 0
    elif name in room[1]:
        save = 1
    elif name in room[2]:
        save = 2
    else:
        print("抱歉，这位女士她不在我们的房间内入住")
    if save <= 2:
        print("她在%d号房间"%save)
    else:
        pass
