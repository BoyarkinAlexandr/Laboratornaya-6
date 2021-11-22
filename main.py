import telebot
# import psycopg2

# conn = psycopg2.connect(database="service",
#                         user="alexandrboyarkin",
#                         password="1234",
#                         host="localhost",
#                         port="5432")
# cursor = conn.cursor()

token = "2125768824:AAEfUwuy7CC0BmX8ikZU-WJn6QtlY7fmw68"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row("Понедельник", "Вторник", "Среда", "Четверг", "Пятница",
                 "Расписание на текущую неделю",
                 "Расписание на следующую неделю")
    bot.send_message(message.chat.id, "Привет! Хочешь узнать свежую информацию о МТУСИ?", reply_markup=keyboard)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "Я умею...")

@bot.message_handler(content_types=["text"])
def answer(message):
    if message.text.lower() == "хочу" or message.text.lower() == "да":
        bot.send_message(message.chat.id, "Тогда тебе сюда - mtuci.ru")
    elif message.text.lower() == "не хочу" or message.text.lower() == "нет":
        bot.send_message(message.chat.id, "Ладно... Пока... Ясно...")
    else:
        bot.send_message(message.chat.id, "Извините, я вас не понял!")







bot.infinity_polling()
