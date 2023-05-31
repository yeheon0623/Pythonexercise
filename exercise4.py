# @Time: 2023/2/05 15:45
# @Author: Yuxuan Wang
# @File :exercise4.py
# @Software: PyCharm

#购物车

products = [["iphone", 6888], ["MacPro", 14800], ["小米6", 2499], ["Coffee", 31], ["Book", 60], ["Nike", 699]]

print("-"*5, "\t", "商品列表", "-"*5)

for i in range(6):
    print(i, end="\t")
    print(products[i][0], end="\t")
    print(products[i][1])

shopping_cart = []
sum_money = 0
while 1:
    user = input("请输入要购买的商品编号(q为结账)：")
    if user != "q" and 0-1 < int(user) < 5+1:
        user = int(user)
        shopping_cart.append(products[user][0])
        sum_money += products[user][1]
        print("请问还需要其他的商品吗？（q为结账）")
    elif user == "q":
        print("你购买的商品有：", end="")
        for i in shopping_cart:
            print(i,end="、")
        print("\b")
        print("一共%d元，谢谢光临！"%sum_money)
        break
    else:
        print("你输入的商品编号不存在，请重新输入")
