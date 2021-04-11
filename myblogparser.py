import requests
from bs4 import BeautifulSoup
import os

myblog = requests.get("https://heibondk.tistory.com/")
soup = BeautifulSoup(myblog.content, "html.parser")


OldNewPost = soup.select(".title")[0].get_text()

while(1):
    NewPost = soup.select("title")[0].get_text()
    if OldNewPost != NewPost:
        NewPost = OldNewPost
        print(NewPost)
        break
    else:
        print(OldNewPost)
        break

#print(OldNewPost)

#oldPost = soup.select(".title")
#print(myblog.text)
