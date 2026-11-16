import pandas as pd
import random

names = ["张三", "李四", "王五", "赵六", "钱七", "孙八", "周九", "吴十"]
subjects = ["语文", "数学", "英语", "物理"]

rows = []
for i in range(80):
    rows.append({
        "姓名": random.choice(names),
        "科目": random.choice(subjects),
        "分数": random.randint(40, 100),
        "日期": f"2026-11-{(i % 28) + 1:02d}",
    })

df = pd.DataFrame(rows)
df.to_excel("sample.xlsx", index=False)
print("生成完成，共", len(df), "行")