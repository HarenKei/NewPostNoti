import requests
from bs4 import BeautifulSoup
import json
from collections import OrderedDict
import telegram_bot as tgb

myblog = requests.get("https://heibondk.tistory.com/")
soup = BeautifulSoup(myblog.content, "html.parser")


def NewPost_file() : #새 포스팅을 검사하기 위한 함수
    file_data = OrderedDict()
    file_data["link"] = "https://heibondk.tistory.com"
    file_data["title"] = soup.select(".title")[0].get_text()
    file_data["date"] = soup.select(".date")[0].get_text()
    links = soup.select(".post-item")[0]
    href = links.find('a')
    href_last = href.attrs['href']
    file_data["href"] = href_last #새 포스팅의 포스트 번호를 가져오는 부분, 매우 지저분함;;
    with open('NewPost.json', 'w', encoding="utf-8") as make_file:
        json.dump(file_data, make_file, ensure_ascii=False, indent="\t")

NewPost_file()

def CompNewPost():
    with open('ExiNewPost.json', 'r') as orig_file, open('NewPost.json', 'r') as new_file:
        orig = json.load(orig_file)
        newp = json.load(new_file)

        if orig.get('title') != newp.get('title'):
            tgb.sendNoti(newp.get('title'), newp.get('date'),newp.get('link')+newp.get('href'))

        else:
            tgb.sendNoti(orig.get('title'), orig.get('date'),orig.get('link')+orig.get('href'))

CompNewPost()



