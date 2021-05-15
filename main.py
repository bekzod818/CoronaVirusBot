import telebot
from config import TOKEN
from telebot import types
from covid import Covid
covid = Covid()

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('🌎 Dunyo bo\'ylab')
    btn2 = types.KeyboardButton("🇺🇿 O'zbekistan")
    btn3 = types.KeyboardButton('🇷🇺 Rossiya')
    btn4 = types.KeyboardButton('🔎 Izlash')
    markup.add(btn1, btn2, btn3, btn4)
    send_mes = f"<b>Assalomu aleykum {message.from_user.first_name}</b>"
    bot.send_message(message.chat.id, send_mes, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '🌎 Dunyo bo\'ylab':
        confirmed = covid.get_total_confirmed_cases()
        active = covid.get_total_active_cases()
        recovered = covid.get_total_recovered()
        deaths = covid.get_total_deaths()
        mes = f"<i><b>Butun dunyo bo'yicha</b></i>\n\n🦠 Yuqtirganlar: <b>{confirmed}</b> ta\n💊 Tuzalganlar: <b>{recovered}</b> ta\n🌡 Kasallar: <b>{active}</b> ta\n⚰️ Vafot etganlar: <b>{deaths}</b> ta"
        bot.send_message(message.chat.id, mes, parse_mode='html')
    elif message.text == '🇺🇿 O\'zbekistan':
        uzb = covid.get_status_by_country_name('Uzbekistan')
        mes = f"<i><b>O'zbekiston davlatida</b></i>\n\n🦠 Yuqtirganlar: <b>{uzb['confirmed']}</b> ta\n💊 Tuzalganlar: <b>{uzb['recovered']}</b> ta\n🌡 Kasallar: <b>{uzb['active']}</b> ta\n⚰️ Vafot etganlar: <b>{uzb['deaths']}</b> ta"
        bot.send_message(message.chat.id, mes, parse_mode='html')
    elif message.text == '🇷🇺 Rossiya':
        rus = covid.get_status_by_country_name('Russia')
        mes = f"<i><b>{rus['country'].title()} davlatida</b></i>\n\n🦠 Yuqtirganlar: <b>{rus['confirmed']}</b> ta\n💊 Tuzalganlar: <b>{rus['recovered']}</b> ta\n🌡 Kasallar: <b>{rus['active']}</b> ta\n⚰️ Vafot etganlar: <b>{rus['deaths']}</b> ta"
        bot.send_message(message.chat.id, mes, parse_mode='html')
    elif message.text == '🔎 Izlash':
        bot.send_message(message.chat.id, '<b>Davlat nomini inglizcha kiriting 🔽</b>', parse_mode='html')
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('🌎 Dunyo bo\'ylab')
        btn2 = types.KeyboardButton("🇺🇿 O'zbekistan")
        btn3 = types.KeyboardButton('🇷🇺 Rossiya')
        btn4 = types.KeyboardButton('🔎 Izlash')
        markup.add(btn1, btn2, btn3, btn4)
        try:
            country = covid.get_status_by_country_name(message.text.lower())
            mes = f"<i><b>{country['country'].title()} davlatida</b></i>\n\n🦠 Yuqtirganlar: <b>{country['confirmed']}</b> ta\n💊 Tuzalganlar: <b>{country['recovered']}</b> ta\n🌡 Kasallar: <b>{country['active']}</b> ta\n⚰️ Vafot etganlar: <b>{country['deaths']}</b> ta"
            bot.send_message(message.chat.id, mes, parse_mode='html', reply_markup=markup)
        except:
            bot.send_message(message.chat.id, '<b>Davlatning inglizcha nomini kiriting: <i>(Spain)</i></b>', parse_mode='html', reply_markup=markup)

bot.polling(none_stop=True)
