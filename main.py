import requests
from bs4 import BeautifulSoup
import json
from collections import OrderedDict
import myblogparser as exipsr
import twitter_bot as tb

myblog = requests.get("https://heibondk.tistory.com/")
soup = BeautifulSoup(myblog.content, "html.parser")
global link

def NewPost_file() : #새 포스팅을 검사하기 위한 함수
    file_data = OrderedDict()
    file_data["title"] = soup.select(".title")[0].get_text()
    file_data["date"] = soup.select(".date")[0].get_text()
    links = soup.select(".post-item")[0]
    href = links.find('a')
    href_last = href.attrs['href']
    file_data["href"] = href_last #새 포스팅의 포스트 번호를 가져오는 부분, 매우 지저분함;;
    with open('./POST_JSON/NewPost.json', 'w', encoding="utf-8") as make_file:
        json.dump(file_data, make_file, ensure_ascii=False, indent="\t")

def CompNewPost():
    with open('./POST_JSON/ExiNewPost.json', 'r') as orig_file, open('./POST_JSON/NewPost.json', 'r') as new_file:
        orig = json.load(orig_file)
        newf = json.load(new_file)

        if orig.get('href') != newf.get('href'):
            tb.twitting(newf.get('title'), newf.get('date'), newf.get('href'))
            print("달라요~")
        

NewPost_file()
CompNewPost()
exipsr.exiNewPost_file()

