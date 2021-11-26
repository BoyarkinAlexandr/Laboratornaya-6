import telebot
import psycopg2
token = "2125768824:AAEfUwuy7CC0BmX8ikZU-WJn6QtlY7fmw68"

bot = telebot.TeleBot(token)


conn = psycopg2.connect(database="bot",
                        user="alexandrboyarkin",
                        password="54321",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()

bot = telebot.TeleBot(token)

import datetime
def weeker():
    today = datetime.datetime.today().strftime("%W")

    if int(today) % 2 == 0:
        return 'нижняя неделя'
    else:
        return 'верхняя неделя'




@bot.message_handler(commands=["start"])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row("Понедельник", "Не хочу")
    bot.send_message(message.chat.id, "Привет, выберите какое расписание вас интересует!", reply_markup=keyboard)

@bot.message_handler(commands=["week"])
def week(message):
    bot.send_message(message.chat.id, "Привет! Cейчас: " + weeker())

@bot.message_handler(commands=["mtuci"])
def mtuci(message):
    bot.send_message(message.chat.id, "Привет! Официальный сайт МТУСИ - mtuci.ru")

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "Здравствуйте! Данный бот сделан для расписания группы БФИ2101. Автор: Бояркин Александр"
                     "\n Команды: \n /help - сведения о работе телеграм бота. \n /start - запуск бота. \n /mtuci - ссылка на официальный сайт ВУЗА МТУСИ"
                        "\n /week - определяет какая сейчас неделя.")





bot.infinity_polling()
