import pandas as pd

df = pd.read_excel("sample.xlsx") 
result = df.groupby("科目")["分数"].mean().sort_values(ascending=False)
print(result)

result.to_excel("avg.xlsx")