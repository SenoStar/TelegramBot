import telebot
from telebot import types


bot = telebot.TeleBot("7179112853:AAHuHYPqufobrnGUbCBIYbYNTLQ2NoEGqzg")


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Мой профиль👤", url="https://steamcommunity.com/sharedfiles/filedetails/?id=2962634922")
    markup.row(button1)
    button2 = types.InlineKeyboardButton("Различные фишки🤓", url="https://steamcommunity.com/sharedfiles/filedetails/?id=2962634922")
    button3 = types.InlineKeyboardButton("Игры🕹", url="https://steamcommunity.com/sharedfiles/filedetails/?id=2962634922")
    markup.row(button2,button3)
    markup.add(types.InlineKeyboardButton("Написать разработчику", url="t.me/SirAbobaGay"))
    bot.send_message(message.chat.id, "Выбери нужный раздел:", reply_markup=markup)


#@bot.message_handler(commands=["profile"])
#def profile(message):12313



@bot.message_handler(content_types=["photo"])
def get_photo(message):
    bot.reply_to(message, "И зачем мне твоё фото?")  #Ответ на фото с ссылкой сообщения


@bot.message_handler(commands=["sosat"])
def sosat(message):
    bot.send_message(message.chat.id, "Соси <b>ХУЙ</b>", parse_mode='html')  #Можно юзать теги из html


@bot.message_handler(commands=["info"])
def info(message):
    bot.send_message(message.chat.id, message)  #Ответ на /info


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.send_message(message.chat.id, "Ты пидор! " + message.text)


bot.polling(none_stop=True)  #Работает 24/7 пока не офну