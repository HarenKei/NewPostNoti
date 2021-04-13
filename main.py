import requests
from bs4 import BeautifulSoup
import json
import myblogparser
from collections import OrderedDict
#import python_twitter

myblog = requests.get("https://heibondk.tistory.com/")
soup = BeautifulSoup(myblog.content, "html.parser")

def NewPost_file() :
    file_data = OrderedDict()
    file_data["title"] = soup.select(".title")[0].get_text()
    file_data["date"] = soup.select(".date")[0].get_text()
    with open('NewPost.json', 'w', encoding="utf-8") as make_file:
        json.dump(file_data, make_file, ensure_ascii=False, indent="\t")

