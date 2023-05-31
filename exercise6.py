# @Time: 2023/2/18 14:48
# @Author: Yuxuan Wang
# @File :exercise6.py
# @Software: PyCharm

# 写古诗
f = open("gushi.txt", "w", encoding="utf-8")
f.write("""
        静夜思
         李白
 床前明月光，疑是地上霜。
 举头望明月，低头思故乡。""")
f.close()

# 复制
f = open("gushi.txt", "r", encoding="utf-8")
m = open("copy.txt", "w", encoding="utf-8")

content = f.readlines()
for i in content:
    m.write(i)
f.close()
m.close()
