import telegram

my_token = '1766599250:AAFUu45A-eb4VnQ4IYy83DtPKTg-7nAhhAw'
bot = telegram.Bot(token=my_token)
updates = bot.getUpdates()

for u in updates :
    print(u.message.text)

chat_id = bot.getUpdates()[-1].message.chat.id
bot.send_message(chat_id = chat_id, text= "저는 봇입니다.")

