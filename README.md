# NewPostNoti

공부한 내용을 기록하는 제 [Stargazer](https://heibondk.tistory.com) 블로그에 새 글을 올리면 제 트위터에 자동으로 트윗을 해 주는 파이썬 프로그램입니다.

## 사용한 Python 패키지
* Requests - 블로그를 파싱할 때 사용
* BeautifulSoup4 - 블로그를 파싱할 때 사용
* Tweepy - Python에서 Twitter를 제어하기 위해 사용
* OrderedDict - 파싱한 데이터의 순서를 보장받기 위해 사용
* json - 파싱한 내용을 Json 파일로 저장하고 활용하기 위해 사용

## 작동 방식
* myblogparser.py에서 [Stargazer](https://heibondk.tistory.com) 블로그의 HTML을 파싱하여 OrderedDict 패키지를 통해 정렬, 포스팅의 **링크**, **제목**, **작성일**을 가져와 '기존의 새 글'을 뜻하는 ExiNewPost.json 파일에 기록.
* twitter_bot.py에서는 단순히 트위터에 자동 트윗을 날리는 기능만을 함수로 구현해두었음.
* main.py에서 myblogparser.py와 twitter_bot.py를 import해서 사용. main.py가 실행되면 블로그를 main.py 내에서 다시 파싱하여 '새 글'을 뜻하는 NewPost.json에 저장, myblogparser.py에서 만들어진 ExiNewPost.json과 "title"을 비교하여 다를 경우 NewPost.json의 내용을 트윗해줌. (비교 부분은 효율을 감안해 차후 수정 및 보완해나갈 예정.)

## ssh 서버에서 crontab을 통해 실시간 서비스 구현

새 글이 올라오는 즉시 트윗을 하는 기능을 의도하였으므로 실시간으로 스크립트를 구동하는 것이 필요했음.

ssh 서버에서 crontab을 사용하여 쉘 스크립트로 실행명령을 입력해주었음.
