import telegram

my_token = '825907431:AAH_3LTZ40DKGSJivCXKcSjAEErjtCcb2U8'

bot = telegram.Bot(token = my_token)

updates = bot.getUpdates()

for u in updates :
    print(u.message)


