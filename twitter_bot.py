import tweepy

f = open("./API_KEY/Twitter_Key", 'r')
tkn = f.readlines()

def twitting(message):

    def twitting(message):
        apikey = tkn[0] #'컨슈머키를 입력(작은 따옴표 지우지 마세요)'
        apisecret = tkn[1] #'컨슈머 시크릿 입력(작은따옴표 지우지 마세요)'
        access_token = tkn[2]#'Access 토큰을 입력(작은따옴표 지우지 마세요)'
        access_token_secret = tkn[3] #'Access 토큰 시크릿 입력(작은따옴표 지우지 마세요)'

        auth = tweepy.OAuthHandler(apikey, apisecret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        api.update_status(message)

    twitting('으악')
