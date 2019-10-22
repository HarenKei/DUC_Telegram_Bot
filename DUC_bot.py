import telegram
import requests
import json
import urllib



url = 'Your open weather API'
Token = "Your Telegram Bot Token" #Telegram_Bot_Token
bot = telegram.Bot(token = Token)
updates = bot.getUpdates()

data = requests.get(url).json()
print(data)

class dataObject:
    def __init__(self, last_name,temp,hum,weather):
        self.last_name = updates['chat']['last_name']
        self.temp = (int)(data['main']['temp'] - 273.15)
        self.hum = data['main']['humidity']
        self.weather = data['weather']['main']

dataObject = requests.get(url).json()

for u in updates:
    print(u.message)

chat_id = bot.getUpdates()[-1].message.chat.id
bot.sendMessage(chat_id = chat_id, text = "안녕하세요! 텔레그램 봇입니다.")


