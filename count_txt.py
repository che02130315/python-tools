import os

folder = input("请输入路径：")
suffix = input("请输入筛选后缀：")

names = os.listdir(folder)
count = 0
for i in names:
    if i.endswith(suffix):
        count += 1
print("一共", count, "个")