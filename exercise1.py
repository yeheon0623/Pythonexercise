# 电脑随机生成一个数
import random
number2 = random.randint(0, 2)

computer = 0
if number2 == 0:
    computer = "剪刀（0）"
elif number2 == 1:
    computer = "石头（1）"
elif number2 == 2:
    computer = "布（2）"
# 用户输入
number1 = int(input("请输入一个数字，0代表剪刀，1代表石头，2代表布："))

user = 0
if number1 == 0:
    user = "剪刀（0）"
elif number1 == 1:
    user = "石头（1）"
elif number1 == 2:
    user = "布（2）"

# 打印用户输入的and电脑随机生成的
print("你输入的是：", user)
print("随机生成的是", computer)

# 判断输赢
if number1 == number2:
    print("平手，再来一次")
elif number1 == 0 and number2 == 1:
    print("抱歉，你输了。")
elif number1 == 0 and number2 == 2:
    print("恭喜你赢了！！！")
elif number1 == 1 and number2 == 0:
    print("恭喜你赢了！！！")
elif number1 == 1 and number2 == 2:
    print("抱歉，你输了。")
elif number1 == 2 and number2 == 0:
    print("抱歉，你输了。")
elif number1 == 2 and number2 == 1:
    print("恭喜你赢了！！！")

