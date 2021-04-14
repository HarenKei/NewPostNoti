import telegram
import json

my_token = '1766599250:AAFUu45A-eb4VnQ4IYy83DtPKTg-7nAhhAw'
bot = telegram.Bot(token=my_token)
updates = bot.getUpdates()

for u in updates :
    print(u.message.text)

def sendNoti(notiTitle, notiDate, notiLink) :
    chat_id = bot.getUpdates()[-1].message.chat.id
    bot.send_message(chat_id=chat_id, text="STARGAZER 블로그에 다음과 같은 새 포스팅이 있습니다. \n " + "\n" + notiTitle +"\n"+ "업로드일 : " + notiDate + "\n" + notiLink)
