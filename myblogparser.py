import requests
from bs4 import BeautifulSoup
import json
from collections import OrderedDict

myblog = requests.get("https://heibondk.tistory.com/")
soup = BeautifulSoup(myblog.content, "html.parser")

def exiNewPost_file() :
    file_data = OrderedDict()
    file_data["link"] = "https://heibondk.tistory.com"
    file_data["title"] = soup.select(".title")[0].get_text()
    file_data["date"] = soup.select(".date")[0].get_text()
    links = soup.select(".post-item")[0]
    href = links.find('a')
    href_last = href.attrs['href']
    file_data["href"] = href_last

    with open('ExiNewPost.json', 'w', encoding="utf-8") as make_file:
        json.dump(file_data, make_file, ensure_ascii=False, indent="\t")

exiNewPost_file()


