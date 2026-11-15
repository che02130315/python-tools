import os

folder = r"c"

names = os.listdir(folder)
print("一共", len(names), "个")

for i, name in enumerate(names, start=1):
    old_path = os.path.join(folder, name)
    new_name = f"文件{i}_{name}"
    new_path = os.path.join(folder, new_name)
    os.rename(old_path, new_path)
    print(name, "->", new_name)

print("完成")