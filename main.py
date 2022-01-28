import telebot
import key
from telebot import types
bot = telebot.TeleBot(key.token)
@bot.message_handler(commands=["start"])
def keyboard_start(messadge):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    privet = types.KeyboardButton(text="Привет")
    startKboard.add(privet)
    bot.send_message(messadge.chat.id, "хайо!", reply_markup=startKboard)
@bot.message_handler(func=lambda m: m.text =="Привет")
def echo_all(messadge):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    ochae = types.KeyboardButton(text="поговорить о чае")
    kofe = types.KeyboardButton(text="поговорить о кофе")
    startKboard.add(ochae, kofe)
    bot.send_message(messadge.chat.id, "выберете группу :3", reply_markup=startKboard)
@bot.message_handler(func=lambda m: m.text =="поговорить о чае")
def echo_all(messadge):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    malinovi = types.KeyboardButton(text="малиновый чай")
    zeleniy = types.KeyboardButton(text="зеленый чай")
    startKboard.add(malinovi, zeleniy)
    bot.send_message(messadge.chat.id, "о каком чае хочешь послушать?", reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="поговорить о кофе")
def echo_all(messadge):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    neskafe = types.KeyboardButton(text="нескафе")
    monarch = types.KeyboardButton(text="монарх")
    startKboard.add(neskafe, monarch)
    bot.send_message(messadge.chat.id, "о каком кофе желаешь поговорить?", reply_markup=startKboard)
@bot.message_handler(func=lambda m: m.text =="нескафе")
def url(message):
    markup = types.InlineKeyboardMarkup()
    viki_neskafe = types.InlineKeyboardButton(text='вот о нескафе!', url='https://ru.wikipedia.org/wiki/Nescaf%C3%A9')
    markup.add(viki_neskafe)
    bot.send_message(message.chat.id, "Тыкай, там о нескафе! <3", reply_markup=markup)
@bot.message_handler(func=lambda m: m.text =="монарх")
def url(message):
    markup = types.InlineKeyboardMarkup()
    viki_monarch = types.InlineKeyboardButton(text='вот о монарх!', url='https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D0%BD%D0%B0%D1%80%D1%85')
    markup.add(viki_monarch)
    bot.send_message(message.chat.id, "Тяпай, там о монарх! <3", reply_markup=markup)


@bot.message_handler(func=lambda m: m.text =="малиновый чай")
def mch(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    cherniy = types.KeyboardButton(text="черный чай")
    chernichny = types.KeyboardButton(text="черничный чай")
    startKboard.add(cherniy, chernichny)
    bot.send_message(message.chat.id, 'вот о малиновом чае! " https://teawiki.ru/chai/malinovyj-polza-i-vred/ "')

@bot.message_handler(func=lambda m: m.text =="зеленый чай")
def zch(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    onchan = types.KeyboardButton(text="чай ончан")
    mint = types.KeyboardButton(text="мятный чай")
    startKboard.add(onchan, mint)
    bot.send_message(message.chat.id, 'вот о зеленом чае! "https://ru.wikipedia.org/wiki/%D0%97%D0%B5%D0%BB%D1%91%D0%BD%D1%8B%D0%B9_%D1%87%D0%B0%D0%B9" ')

bot.polling()