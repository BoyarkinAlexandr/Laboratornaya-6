import telebot
import psycopg2
import datetime
token = "2125768824:AAEfUwuy7CC0BmX8ikZU-WJn6QtlY7fmw68"

bot = telebot.TeleBot(token)


conn = psycopg2.connect(database="bot",
                        user="alexandrboyarkin",
                        password="1234",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()


def weeker():
    today = datetime.datetime.today().strftime("%W")

    if int(today) % 2 == 0:
        return 'нижняя неделя'
    else:
        return 'верхняя неделя'




@bot.message_handler(commands=["start"])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("Понедельник", "Вторник", "Среда")
    keyboard.row("Четверг","Пятница")
    keyboard.row("Расписание на текущую неделю","Расписание на следующую неделю")
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

@bot.message_handler(content_types=["text"])
def answer(message):
    a = message.text.lower()
    bot.send_message(message.chat.id, a)
    if a == "понедельник":
        cursor.execute("Select id, full_name from teacher")
        teachers= list(cursor.fetchall())
        cursor.execute("Select timetable.subject, room_numb, start_time from timetable"
                       " Where day = 'Понедельник'")
        Time = list(cursor.fetchall())

        bot.send_message(message.chat.id,text =''
                         "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                         "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                         "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                         "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n".format(

                             Time[0][0], Time[0][1], Time[0][2], teachers[14][1],
                             Time[1][0], Time[0][1], Time[0][2], teachers[8][1],
                             Time[2][0], Time[0][1], Time[0][2], teachers[3][1],
                             Time[3][0], Time[0][1], Time[0][2], teachers[3][1]))

    elif a == "вторник":
        cursor.execute("Select id, full_name from teacher")
        teachers = list(cursor.fetchall())
        cursor.execute("Select timetable.subject, room_numb, start_time from timetable"
                       " Where day = 'Вторник'")
        Time = list(cursor.fetchall())

        bot.send_message(message.chat.id, text=''
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n".format(

                                               Time[4][0], Time[4][1], Time[4][2], teachers[0][1],
                                               Time[5][0], Time[5][1], Time[5][2], teachers[0][1],
                                               Time[6][0], Time[6][1], Time[6][2], teachers[0][1],
                                               Time[1][0], Time[1][1], Time[1][2], teachers[0][1],
                                               Time[1][0], Time[1][1], Time[1][2], teachers[0][1]))
    elif a == "среда":
        cursor.execute("Select id, full_name from teacher")
        teachers = list(cursor.fetchall())
        cursor.execute("Select timetable.subject, room_numb, start_time from timetable"
                       " Where day = 'Среда'")
        Time = list(cursor.fetchall())

        bot.send_message(message.chat.id, text=''
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n".format(

                                                Time[4][0], Time[4][1], Time[4][2], teachers[0][1],
                                                Time[5][0], Time[5][1], Time[5][2], teachers[0][1],
                                                Time[6][0], Time[6][1], Time[6][2], teachers[0][1],
                                                Time[1][0], Time[1][1], Time[1][2], teachers[0][1],
                                                Time[1][0], Time[1][1], Time[1][2], teachers[0][1]))
    elif a == "четверг":
        cursor.execute("Select id, full_name from teacher")
        teachers = list(cursor.fetchall())
        cursor.execute("Select timetable.subject, room_numb, start_time from timetable"
                       " Where day = 'Четверг'")
        Time = list(cursor.fetchall())

        bot.send_message(message.chat.id, text=''
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадоватль: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадоватль: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадоватль: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадоватль: {}\n".format(

            Time[0][0], Time[0][1], Time[0][2], teachers[12][1],
            Time[1][0], Time[0][1], Time[0][2], teachers[12][1],
            Time[2][0], Time[0][1], Time[0][2], teachers[12][1],
            Time[3][0], Time[0][1], Time[0][2], teachers[12][1]))
    elif a == "пятница":
        cursor.execute("Select id, full_name from teacher")
        teachers = list(cursor.fetchall())
        cursor.execute("Select timetable.subject, room_numb, start_time from timetable"
                       " Where day = 'Пятница'")
        Time = list(cursor.fetchall())

        bot.send_message(message.chat.id, text=''
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадоватль: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадоватль: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадоватль: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадоватль: {}\n".format(

            Time[0][0], Time[0][1], Time[0][2], teachers[12][1],
            Time[1][0], Time[0][1], Time[0][2], teachers[12][1],
            Time[2][0], Time[0][1], Time[0][2], teachers[12][1],
            Time[3][0], Time[0][1], Time[0][2], teachers[12][1]))
    elif a == "расписание на текущую неделю":
        bot.send_message(message.chat.id, "расписание на текущую неделю:")
    elif a == "расписание на следующую неделю":
        bot.send_message(message.chat.id, "Расписание на следующую неделю:")
    else:
        bot.send_message(message.chat.id, "Извините, я вас не понял!")





bot.infinity_polling()


# cursor.execute("SELECT * FROM public.timetable ")
        # ad = list(cursor.fetchall())
        # answer = 'Понедельник\n _____________________________\n' + str(ad[0][2]+str(ad[0][3]))
        # print(ad[2])