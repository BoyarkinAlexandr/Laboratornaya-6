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
    keyboard.row("Четверг", "Пятница")
    keyboard.row("Расписание на текущую неделю", "Расписание на следующую неделю")
    bot.send_message(message.chat.id, "Привет, выберите какое расписание вас интересует!", reply_markup=keyboard)


@bot.message_handler(commands=["week"])
def week(message):
    bot.send_message(message.chat.id, "Привет! Cейчас: " + weeker())


@bot.message_handler(commands=["mtuci"])
def mtuci(message):
    bot.send_message(message.chat.id, "Привет! Официальный сайт МТУСИ - mtuci.ru")


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id,
                     "Здравствуйте! Данный бот сделан для расписания группы БФИ2101. Автор: Бояркин Александр"
                     "\n Команды: \n /help - сведения о работе телеграм бота. \n /start - запуск бота. \n /mtuci - ссылка на официальный сайт ВУЗА МТУСИ"
                     "\n /week - определяет какая сейчас неделя.")


@bot.message_handler(content_types=["text"])
def answer(message):
    a = message.text.lower()
    bot.send_message(message.chat.id, a)
    if a == "понедельник":
        cursor.execute("Select id, full_name from teacher")
        teachers = list(cursor.fetchall())
        cursor.execute("Select timetable.subject, room_numb, start_time from timetable"
                       " Where day = 'Понедельник' and week_numb = 'Вверхняя'")
        Time = list(cursor.fetchall())

        bot.send_message(message.chat.id, text='\n___________Понедельник_______________Вверхняя неделя__________________________\n'
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               
                                               "\n___________Понедельник_______________Нижняя неделя___________________________\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n".format(

            Time[0][0], Time[0][1], Time[0][2], teachers[14][1],
            Time[1][0], Time[1][1], Time[1][2], teachers[9][1],
            Time[2][0], Time[2][1], Time[2][2], teachers[4][1],
            Time[3][0], Time[3][1], Time[3][2], teachers[4][1],

            Time[0][0], Time[0][1], Time[0][2], teachers[14][1],
            Time[1][0], Time[1][1], Time[1][2], teachers[9][1],
            Time[2][0], Time[2][1], Time[2][2], teachers[4][1],
            Time[3][0], Time[3][1], Time[3][2], teachers[4][1]))

    elif a == "вторник":
        cursor.execute("Select id, full_name from teacher")
        teachers = list(cursor.fetchall())
        cursor.execute("Select timetable.subject, room_numb, start_time from timetable"
                       " Where day = 'Вторник' and week_numb = 'Вверхняя'")
        Time = list(cursor.fetchall())

        cursor.execute("Select timetable.subject, room_numb, start_time from timetable"
                       " Where day = 'Вторник' and week_numb = 'Нижняя'")
        Time1 = list(cursor.fetchall())


        bot.send_message(message.chat.id, text='\n___________Вторник_______________Вверхняя неделя__________________________\n'
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"

                                                "\n___________Вторник_______________Нижняя неделя___________________________\n"
                                                "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                                "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n".format(

            Time[0][0], Time[0][1], Time[4][2], teachers[0][1],
            Time[4][0], Time[4][1], Time[0][2], teachers[0][1],
            Time[1][0], Time[1][1], Time[1][2], teachers[15][1],
            Time[2][0], Time[2][1], Time[2][2], teachers[11][1],
            Time[3][0], Time[3][1], Time[3][2], teachers[3][1],

            Time1[0][0], Time1[0][1], Time1[0][2], teachers[0][1],
            Time1[1][0], Time1[1][1], Time1[1][2], teachers[0][1]))

    elif a == "среда":
        cursor.execute("Select id, full_name from teacher")
        teachers = list(cursor.fetchall())
        cursor.execute("Select timetable.subject, room_numb, start_time from timetable"
                       " Where day = 'Среда' and week_numb = 'Вверхняя'")
        Time = list(cursor.fetchall())

        cursor.execute("Select timetable.subject, room_numb, start_time from timetable"
                       " Where day = 'Среда' and week_numb = 'Нижняя'")
        Time1 = list(cursor.fetchall())

        bot.send_message(message.chat.id, text='\n__________________________Среда___Вверхняя неделя__________________\n'
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"

                                               "\n___________Среда_______________Нижняя неделя___________________________\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n".format(

            Time[0][0], Time[0][1], Time[0][2], teachers[13][1],
            Time[1][0], Time[1][1], Time[1][2], teachers[12][1],

            Time1[0][0], Time1[0][1], Time1[0][2], teachers[11][1],
            Time1[1][0], Time1[1][1], Time1[1][2], teachers[12][1]))

    elif a == "четверг":
        cursor.execute("Select id, full_name from teacher")
        teachers = list(cursor.fetchall())
        cursor.execute("Select timetable.subject, room_numb, start_time from timetable"
                       " Where day = 'Четверг' and week_numb = 'Вверхняя'")
        Time = list(cursor.fetchall())

        cursor.execute("Select timetable.subject, room_numb, start_time from timetable"
                       " Where day = 'Четверг' and week_numb = 'Нижняя'")
        Time1 = list(cursor.fetchall())

        bot.send_message(message.chat.id, text='\nЧетверг___Вверхняя неделя___\n'
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"

                                               "\nЧетверг___Нижняя неделя___\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n".format(

            Time[0][0], Time[0][1], Time[0][2], teachers[7][1],
            Time[1][0], Time[1][1], Time[3][2], teachers[0][1],
            Time[3][0], Time[3][1], Time[1][2], teachers[0][1],
            Time[2][0], Time[2][1], Time[2][2], teachers[9][1],

            Time1[0][0], Time1[0][1], Time1[0][2], teachers[15][1],
            Time1[1][0], Time1[1][1], Time1[1][2], teachers[15][1]))
    elif a == "пятница":
        cursor.execute("Select id, full_name from teacher")
        teachers = list(cursor.fetchall())
        cursor.execute("Select timetable.subject, room_numb, start_time from timetable"
                       " Where day = 'Пятница' and week_numb = 'Вверхняя'")
        Time = list(cursor.fetchall())

        cursor.execute("Select timetable.subject, room_numb, start_time from timetable"
                       " Where day = 'Пятница' and week_numb = 'Нижняя'")
        Time1 = list(cursor.fetchall())

        bot.send_message(message.chat.id, text='\n__________________Пятница___Вверхняя неделя______________________\n'
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"

                                               '\n___________________Пятница___Нижняя неделя________________________\n'
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n".format(

            Time[1][0], Time[1][1], Time[0][2], teachers[2][1],
            Time[0][0], Time[0][1], Time[1][2], teachers[12][1],

            Time1[0][0], Time1[0][1], Time1[0][2], teachers[12][1],
            Time1[1][0], Time1[1][1], Time1[1][2], teachers[2][1]))
    elif a == "расписание на текущую неделю":
        cursor.execute("Select id, full_name from teacher")
        teachers = list(cursor.fetchall())
        cursor.execute("Select timetable.subject, room_numb, start_time from timetable"
                       " Where week_numb = 'Вверхняя'")
        Time = list(cursor.fetchall())

        bot.send_message(message.chat.id, text='\n___________Понедельник_______________Вверхняя неделя__________________________\n'
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"

                                                "\n___________Вторник_______________Вверхняя неделя__________________________\n"
                                                "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                                "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                                "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                                "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                                "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"

                                                "\n__________________________Среда___Вверхняянеделя__________________\n"
                                                "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                                "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"

                                               "\n__________________________Четверг___Вверхняя неделя________________\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"

                                               "\n__________________________Пятница___Вверхняя неделя________________\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n".format(
            Time[0][0], Time[0][1], Time[0][2], teachers[14][1],
            Time[1][0], Time[1][1], Time[1][2], teachers[9][1],
            Time[2][0], Time[2][1], Time[2][2], teachers[4][1],
            Time[3][0], Time[3][1], Time[3][2], teachers[4][1],

            Time[4][0], Time[4][1], Time[0][2], teachers[0][1],
            Time[16][0], Time[16][1], Time[16][2], teachers[0][1],
            Time[5][0], Time[5][1], Time[5][2], teachers[15][1],
            Time[6][0], Time[6][1], Time[6][2], teachers[11][1],
            Time[7][0], Time[7][1], Time[7][2], teachers[3][1],

            Time[8][0], Time[8][1], Time[8][2], teachers[13][1],
            Time[9][0], Time[9][1], Time[9][2], teachers[12][1],

            Time[10][0], Time[10][1], Time[10][2], teachers[7][1],
            Time[11][0], Time[11][1], Time[11][2], teachers[0][1],
            Time[15][0], Time[15][1], Time[15][2], teachers[0][1],
            Time[12][0], Time[12][1], Time[12][2], teachers[9][1],

            Time[13][0], Time[13][1], Time[13][2], teachers[2][1],
            Time[14][0], Time[14][1], Time[14][2], teachers[12][1]))
    elif a == "расписание на следующую неделю":
        cursor.execute("Select id, full_name from teacher")
        teachers = list(cursor.fetchall())
        cursor.execute("Select timetable.subject, room_numb, start_time from timetable"
                       " Where week_numb = 'Нижняя'")
        Time1 = list(cursor.fetchall())
        bot.send_message(message.chat.id, text='\n___________Понедельник_______________Нижняя неделя__________________________\n'
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"

                                                "\n___________Вторник_______________Нижняя неделя__________________________\n"
                                                "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                                "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                                

                                                "\n__________________________Среда___Нижняяя неделя__________________\n"
                                                "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                                "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"

                                               "\n__________________________Четверг___Нижняя неделя________________\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               

                                               "\n__________________________Пятница___Нижняя неделя________________\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n"
                                               "\nПредмет: {}\nКабинет: {}\nВремя: {}\nПрепадователь: {}\n".format(

            Time1[0][0], Time1[0][1], Time1[0][2], teachers[14][1],
            Time1[1][0], Time1[1][1], Time1[1][2], teachers[9][1],
            Time1[2][0], Time1[2][1], Time1[2][2], teachers[4][1],
            Time1[3][0], Time1[3][1], Time1[3][2], teachers[4][1],

            Time1[4][0], Time1[4][1], Time1[4][2], teachers[0][1],
            Time1[5][0], Time1[5][1], Time1[5][2], teachers[0][1],

            Time1[6][0], Time1[6][1], Time1[6][2], teachers[11][1],
            Time1[7][0], Time1[7][1], Time1[7][2], teachers[12][1],

            Time1[8][0], Time1[8][1], Time1[8][2], teachers[15][1],
            Time1[9][0], Time1[9][1], Time1[9][2], teachers[15][1],

            Time1[10][0], Time1[10][1], Time1[10][2], teachers[2][1],
            Time1[11][0], Time1[11][1], Time1[11][2], teachers[12][1]))
    else:
        bot.send_message(message.chat.id, "Извините, я вас не понял!")


bot.infinity_polling()

# cursor.execute("SELECT * FROM public.timetable ")
# ad = list(cursor.fetchall())
# answer = 'Понедельник\n _____________________________\n' + str(ad[0][2]+str(ad[0][3]))
# print(ad[2])
