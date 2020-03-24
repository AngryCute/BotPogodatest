import telebot
import pyowm

owm = pyowm.OWM('02cf53ad01886e9dbc02b2e2f14fddc8', language= "ru")
bot = telebot.TeleBot("920219182:AAEbU2rJHKC39KcU2XZN-Q2HEU6vwemJSHI")

@bot.message_handler(content_types=['text'])
def weather(message):
    try:
        observation = owm.weather_at_place(message.text)
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
    except:
        answer = "Такого города нет"
    else:
        answer = f"В городе {message.text} сейчас {w.get_detailed_status()}\n " \
                 f"Температура в городе {message.text} сейчас {temp})\n\n"
        if temp < 5:
            answer += "Очень холодно! Одевайся потеплее!"
        elif temp < 10:
            answer += "Холодновато. Но уже можно выйти на улицу"
        elif temp < 20:
            answer += "Достатоно тепло для хорошей прогулки :)"
        else:
            answer += "ЖАРААА"
    bot.send_message(message.chat.id, answer)
bot.polling( none_stop= True)