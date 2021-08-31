import telegram
import json

apiKey = open("./API_KEY/Telegram_Key", 'r')
my_token = apiKey.read().rstrip('\n')
bot = telegram.Bot(token=my_token)
updates = bot.getUpdates()
global link
link = "https://heibondk.tistory.com"

def sendNoti(notiTitle, notiDate, notiLink) :
    chat_id = bot.getUpdates()[-1].message.chat.id
    bot.send_message(chat_id=chat_id, text="STARGAZER 블로그에 다음과 같은 새 포스팅이 있습니다. \n " + "\n" + notiTitle +"\n"+ "업로드일 : " + notiDate + "\n" + link + notiLink)
