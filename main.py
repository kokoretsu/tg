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
def nkf(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    end2 = types.KeyboardButton(text="благодарю!")
    startKboard.add(end2)
    bot.send_message(message.chat.id, 'вот о нескафе!"https://ru.wikipedia.org/wiki/Nescaf%C3%A9" ', reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="монарх")
def nkf(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    end = types.KeyboardButton(text="спасибо!")
    startKboard.add(end)
    bot.send_message(message.chat.id, 'вот о монарх!"https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D0%BD%D0%B0%D1%80%D1%85" ', reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="малиновый чай")
def mch(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    cherniy = types.KeyboardButton(text="черный чай")
    chernichny = types.KeyboardButton(text="черничный чай")
    startKboard.add(cherniy, chernichny)
    bot.send_message(message.chat.id, 'вот о малиновом чае! " https://teawiki.ru/chai/malinovyj-polza-i-vred/ "', reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="зеленый чай")
def zch(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    onchan = types.KeyboardButton(text="чай анчан")
    mint = types.KeyboardButton(text="мятный чай")
    startKboard.add(onchan, mint)
    bot.send_message(message.chat.id, 'вот о зеленом чае! "https://ru.wikipedia.org/wiki/%D0%97%D0%B5%D0%BB%D1%91%D0%BD%D1%8B%D0%B9_%D1%87%D0%B0%D0%B9" ', reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="чай анчан")
def ach(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    end = types.KeyboardButton(text="спасибо!")
    startKboard.add(end)
    bot.send_message(message.chat.id, 'вот о чае ончан! "https://ru.wikipedia.org/wiki/%D0%9A%D0%BB%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D1%8F_%D1%82%D1%80%D0%BE%D0%B9%D1%87%D0%B0%D1%82%D0%B0%D1%8F" ', reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="мятный чай")
def mich(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    end2 = types.KeyboardButton(text="благодарю!")
    startKboard.add(end2)
    bot.send_message(message.chat.id, 'вот о чае ончан!"https://zavarka.life/recepty/chaj-s-mjatoy.html" ' , reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="черный чай")
def mich(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    end2 = types.KeyboardButton(text="благодарю!")
    startKboard.add(end2)
    bot.send_message(message.chat.id, 'вот о черном чае!"https://ru.wikipedia.org/wiki/%D0%A7%D1%91%D1%80%D0%BD%D1%8B%D0%B9_%D1%87%D0%B0%D0%B9" ' , reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="черничный чай")
def mich(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    end = types.KeyboardButton(text="спасибо!")
    startKboard.add(end)
    bot.send_message(message.chat.id, 'вот о черничном чае!"https://tutknow.ru/meal/15259-chernichnyy-chay-polza-vred-zagotovka-syrja-recepty.html" ' , reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="благодарю!")
def mich(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bot.send_message(message.chat.id, 'пока-пока! чтобы снова запустить бота напишите "/start" <3', reply_markup=startKboard)

@bot.message_handler(func=lambda m: m.text =="спасибо!")
def nkf(message):
    startKboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    bot.send_message(message.chat.id, 'удачи! чтобы снова запустить бота напишите "/start" ;3', reply_markup=startKboard)
bot.polling()