import requests
import telebot
from settings import token, bot_url, weather_api_key, base_weather_url
from commands import eat, help, eatprice, toilets, time, practice, map, computers

bot = telebot.TeleBot(token)

print(f"Hi, go to {bot_url}")


@bot.message_handler(commands=['start'])
def send(message):
    bot.reply_to(message, help)


@bot.message_handler(commands=['eat'])
def send_eat(message):
	bot.reply_to(message, eat)


@bot.message_handler(commands=['eatprice'])
def send_eatprice(message):
	bot.reply_to(message, eatprice)


@bot.message_handler(commands=['toilets'])
def send_toilets(message):
	bot.reply_to(message, toilets)


@bot.message_handler(commands=['time'])
def send_time(message):
	bot.reply_to(message, time)


@bot.message_handler(commands=['practice'])
def send_practice(message):
	bot.reply_to(message, practice)


@bot.message_handler(commands=['map'])
def send_map(message):
	bot.reply_to(message, map)


@bot.message_handler(commands=['computers'])
def send_computers(message):
	bot.reply_to(message, computers)


@bot.message_handler(commands=['schedule'])
def sendFile(message):
    file = open("./img/ras.png", 'rb')
    _mess = "Отправка файла"
    bot.send_message(message.chat.id, _mess, parse_mode="html")
    bot.send_document(message.chat.id, file)


@bot.message_handler(commands=['weather'])
def wear(message):
    _message = f'Write your city and country ("by type Almaty, KZ"):'
    bot.send_message(message.chat.id, _message, parse_mode="html")


@bot.message_handler()
def weather(message):
    city = message.text
    url_weather = base_weather_url + city + '&units=imperial&APPID=' + weather_api_key
    response = requests.get(url_weather).json()
    _message = f'Temperature - ( {response["main"]["temp"]}°C )'
    bot.send_message(message.chat.id, _message, parse_mode="html")


bot.polling(none_stop=True)

print("bot stop")