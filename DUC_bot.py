import telegram
import requests

#api key : cba6316cc66b10b108bc4dda1c1cacf1

url = 'http://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=cba6316cc66b10b108bc4dda1c1cacf1'

data = requests.get(url).json()

my_token = '825907431:AAH_3LTZ40DKGSJivCXKcSjAEErjtCcb2U8'

bot = telegram.Bot(token = my_token)

updates = bot.getUpdates()

for u in updates :
    print(u.message)

print(data)
