import telebot
from telebot import types
token = "5481177672:AAE1DNoBavUlvB-0gcjlXAxS0THi36g2qYg"
admin='140058404'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])

def start(message):
    keyboard = types. InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text = 'مقترح ',callback_data="click1")
    button2 = types.InlineKeyboardButton(text = 'ملاحظة ',callback_data="click2")
    keyboard.add(button1, button2)
    bot.reply_to(message,"مرحبا بك عزيزي الطالب في بوت بكم نكمل👋🏻\nفي هذا البوت يمكنك تقديم المقترحات لإدارة الثانوية وأيضا الملاحظات بسرية تامة من اجل تحسين العملية التعليمية 🧑🏻‍🎓✨\n\n قم باختيار ماتريد تقديمه من القائمة أدناه 👇🏻\n تحياتي لكم مبرمج البوت الطالب : علي محمد حسان", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):
    if call.message:
        if call.data == "click2":
            bot.send_message(call.message.chat.id,'فضلاً أكتب الملاحظة في رسالة واحدة فقط وبكل أدب واحترام')
            @bot.message_handler(content_types=['text'])
            def ee(call):
                msg1 = (call.text)
                bot.send_message(admin,"رسالة جديدة من إبنك 🙏🏻الرجاء وضعها بعين الإعتبار\n"+ msg1)
                bot.send_message(call.chat.id,'تم استلام رسالتك شكرا لك على تعاونك ♥')
        if call.data == "click1":
            bot.send_message(call.message.chat.id,'فضلاً قم بكتابة المقترح في رسالة واحدة فقط ')
            @bot.message_handler(content_types=['text'])
            def hh(call):
                msg2 = (call.text)
                bot.send_message(admin,"رسالة جديدة من إبنك الرجاء وضعها بعين الإعتبار\n"+ msg2)
                bot.send_message(call.chat.id,'تم استلام رسالتك شكرا لك على تعاونك♥')


print('aloshy')
bot.polling()

