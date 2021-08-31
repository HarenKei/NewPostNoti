import tweepy

apiKey = open("./API_KEY/Twitter_Key", 'r')

def twitting(message):
    token = apiKey.read().rstrip()
    token_scret = 'yCwTliqVD0eXxfIHc5ellFGiTvQ4XaYmMVrbGVrmZsOejBulyO'