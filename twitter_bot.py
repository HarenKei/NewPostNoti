import tweepy

f = open("./API_KEY/Twitter_Key", 'r')
tkn = f.readlines()



def twitting(message):
        apikey = str(tkn[0]).rstrip('\n') #컨슈머키
        apisecret = str(tkn[1]).rstrip('\n') #컨슈머 시크릿
        access_token = str(tkn[2]).rstrip('\n') #Access
        access_token_secret = str(tkn[3]).rstrip('\n') #Acceess 시크릿

        auth = tweepy.OAuthHandler(apikey, apisecret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        api.update_status(message)


