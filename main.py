import telebot
from config import TOKEN
from telebot import types
from covid import Covid
covid = Covid()

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('π Dunyo bo\'ylab')
    btn2 = types.KeyboardButton("πΊπΏ O'zbekistan")
    btn3 = types.KeyboardButton('π·πΊ Rossiya')
    btn4 = types.KeyboardButton('π Izlash')
    markup.add(btn1, btn2, btn3, btn4)
    send_mes = f"<b>Assalomu aleykum {message.from_user.first_name}</b>"
    bot.send_message(message.chat.id, send_mes, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'π Dunyo bo\'ylab':
        confirmed = covid.get_total_confirmed_cases()
        active = covid.get_total_active_cases()
        recovered = covid.get_total_recovered()
        deaths = covid.get_total_deaths()
        mes = f"<i><b>Butun dunyo bo'yicha</b></i>\n\nπ¦  Yuqtirganlar: <b>{confirmed}</b> ta\nπ Tuzalganlar: <b>{recovered}</b> ta\nπ‘ Kasallar: <b>{active}</b> ta\nβ°οΈ Vafot etganlar: <b>{deaths}</b> ta"
        bot.send_message(message.chat.id, mes, parse_mode='html')
    elif message.text == 'πΊπΏ O\'zbekistan':
        uzb = covid.get_status_by_country_name('Uzbekistan')
        mes = f"<i><b>O'zbekiston davlatida</b></i>\n\nπ¦  Yuqtirganlar: <b>{uzb['confirmed']}</b> ta\nπ Tuzalganlar: <b>{uzb['recovered']}</b> ta\nπ‘ Kasallar: <b>{uzb['active']}</b> ta\nβ°οΈ Vafot etganlar: <b>{uzb['deaths']}</b> ta"
        bot.send_message(message.chat.id, mes, parse_mode='html')
    elif message.text == 'π·πΊ Rossiya':
        rus = covid.get_status_by_country_name('Russia')
        mes = f"<i><b>{rus['country'].title()} davlatida</b></i>\n\nπ¦  Yuqtirganlar: <b>{rus['confirmed']}</b> ta\nπ Tuzalganlar: <b>{rus['recovered']}</b> ta\nπ‘ Kasallar: <b>{rus['active']}</b> ta\nβ°οΈ Vafot etganlar: <b>{rus['deaths']}</b> ta"
        bot.send_message(message.chat.id, mes, parse_mode='html')
    elif message.text == 'π Izlash':
        bot.send_message(message.chat.id, '<b>Davlat nomini inglizcha kiriting π½</b>', parse_mode='html')
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('π Dunyo bo\'ylab')
        btn2 = types.KeyboardButton("πΊπΏ O'zbekistan")
        btn3 = types.KeyboardButton('π·πΊ Rossiya')
        btn4 = types.KeyboardButton('π Izlash')
        markup.add(btn1, btn2, btn3, btn4)
        try:
            country = covid.get_status_by_country_name(message.text.lower())
            mes = f"<i><b>{country['country'].title()} davlatida</b></i>\n\nπ¦  Yuqtirganlar: <b>{country['confirmed']}</b> ta\nπ Tuzalganlar: <b>{country['recovered']}</b> ta\nπ‘ Kasallar: <b>{country['active']}</b> ta\nβ°οΈ Vafot etganlar: <b>{country['deaths']}</b> ta"
            bot.send_message(message.chat.id, mes, parse_mode='html', reply_markup=markup)
        except:
            bot.send_message(message.chat.id, '<b>Davlatning inglizcha nomini kiriting: <i>(Spain)</i></b>', parse_mode='html', reply_markup=markup)

bot.polling(none_stop=True)
