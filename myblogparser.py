import requests
from bs4 import BeautifulSoup
import json
from collections import OrderedDict

myblog = requests.get("https://heibondk.tistory.com/")
soup = BeautifulSoup(myblog.content, "html.parser")

file_data = OrderedDict()
file_data["title"] = soup.select(".title")[0].get_text()
file_data["date"] = soup.select(".date")[0].get_text()

print(json.dumps(file_data, ensure_ascii=False, indent="\t"))

with open('ExiNewPost.json', 'w', encoding="utf-8") as make_file:
    json.dump(file_data, make_file, ensure_ascii=False, indent="\t")


#OldNewPost = soup.select(".title")[0].get_text()

"""while(1):
    NewPost = soup.select(".title")[0].get_text()
    if OldNewPost != NewPost:
        NewPost = OldNewPost
        print(NewPost)
        break
    else:
        print(OldNewPost)
        break
"""
