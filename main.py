import requests
from bs4 import BeautifulSoup
import json
from collections import OrderedDict
import telegram_bot as tgb

myblog = requests.get("https://heibondk.tistory.com/")
soup = BeautifulSoup(myblog.content, "html.parser")

postNum = 68 #2021년 4월 14일 기준 STARGAZER 블로그 최근 포스트 번호.

def NewPost_file() :
    file_data = OrderedDict()
    file_data["title"] = soup.select(".title")[0].get_text()
    file_data["date"] = soup.select(".date")[0].get_text()
    with open('NewPost.json', 'w', encoding="utf-8") as make_file:
        json.dump(file_data, make_file, ensure_ascii=False, indent="\t")

NewPost_file()

def CompNewPost(posNum):
    with open('ExiNewPost.json', 'r') as orig_file, open('NewPost.json', 'r') as new_file:
        orig = json.load(orig_file)
        newp = json.load(new_file)

        if orig.get('title') != newp.get('title'):
            tgb.sendNoti(newp.get('title'), newp.get('date'), posNum)
            global postNum
            postNum+= 1
            print(postNum)
        else:
            tgb.sendNoti(orig.get('title'), orig.get('date'), posNum)

CompNewPost(postNum)



