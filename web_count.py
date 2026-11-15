import requests


web = input("请输入网址：")
word = input("请输入关键词：")


try:
    content = requests.get(web, timeout=5).text
    count = content.count(word)
    print(f"关键词{word}的数量是{count}")
except Exception:
    print("出错了")




