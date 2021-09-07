import tweepy

f = open("./API_KEY/Twitter_Key", 'r')
tkn = f.readlines()

global link
link = "https://heibondk.tistory.com"

def twitting(notiTitle, notiDate, notiLink):
        api_key = str(tkn[0]).rstrip('\n') #컨슈머키
        api_key_secret = str(tkn[1]).rstrip('\n') #컨슈머 시크릿
        access_token = str(tkn[2]).rstrip('\n') #Access
        access_token_secret = str(tkn[3]).rstrip('\n') #Acceess 시크릿

        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        api.update_status("STARGAZER 블로그에 다음과 같은 새 포스팅이 있습니다. \n " +
                                           "\n" + notiTitle + "\n" + "업로드일 : " + notiDate + "\n" + link + notiLink)


