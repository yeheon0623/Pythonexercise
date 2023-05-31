# @Time: 2023/2/02 10:25
# @Author: Yuxuan Wang
# @File :exercise3.py
# @Software: PyCharm

#使用for循环和while循环打印九九乘法表

# for+字符串转换
for i in range(1, 10):
    for j in range(1, i+1):
        print(str(i)+"*"+str(j)+"="+str(i*j), end=" ")  # end=" "作用①不换行②间隔
    print()  # 换行

#  for+格式化
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("{}*{}={}".format(i, j, i * j), end=" ")  # end=" "作用①不换行②间隔
        print()  # 换行

i = 1
j = 1

#while循环
while j <= i < 10 and j < 10:
    print("%d*%d=%d" % (i, j, i*j), end="\t")
    if i > j:
        j += 1
    else:               # i == j
        i += 1
        j = 1
        print("\n")
        continue

