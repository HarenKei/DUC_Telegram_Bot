from telegram.ext import Updater, MessageHandler, Filters  # import modules

token_file = open('/Users/harenkei/PycharmProjects/DUC_bot/token','r')
my_token = token_file.read().rstrip('\n')

print('start telegram chat bot')


# message reply function
def get_message(bot, update):
    update.message.reply_text("got text")
    update.message.reply_text(update.message.text)


updater = Updater(my_token)

if "학식" in update.message.text:
    db = open("", 'r')
    context.bot.send_message(chat_id=update.effective_chat.id, text=db.read())


message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()