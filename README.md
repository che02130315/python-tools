# 我的 Python 练习

学 Python 时写的小工具。

## 文件

- rename.py：批量给文件名加序号
- count_txt.py：数文件夹里指定后缀的文件有几个
- web_count.py：数网页里某个关键词出现几次
- make_data.py：生成测试用的 sample.xlsx
- report.py：统计每科平均分，输出 avg.xlsx

## 运行方式

    python 文件名.py

## 依赖

web_count.py 需要 requests，report.py 需要 pandas：

    pip install requests pandas openpyxl
