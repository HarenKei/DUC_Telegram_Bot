import telegram
import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=*'

data = requests.get(url).json()

my_token = **********************

bot = telegram.Bot(token = my_token)

updates = bot.getUpdates()

for u in updates :
    print(u.message)

print(data)
