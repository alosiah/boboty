import requests,telebot
bot = telebot.TeleBot('6044177233:AAFuTYblhORVlVDkeSLrjAqboE8K2lWvUvM')
@bot.message_handler(commands=["start"])
def mes(message):
 bot.send_message(message.chat.id,"مرحبا بكم في بوت حضرم مترجم 🫡\nهذا البوت يقوم بترجمة جميع لغات العالم إلى اللغة العربية 🇾🇪✨\nكل ماعليك هو إرسال ماتود ترجمته هنا فقط\nخالص تحياتي مبرمج البوت : علي محمد حسان") 
@bot.message_handler(func=lambda m:True)
def inf(message):
 user = message.text
 s = requests.get(f'https://Trans.noxi8.repl.co/ar/text={user}').text
 for wrd in s.splitlines():
     if ('p' in wrd)or('{'in wrd) or ('}' in wrd) :
	     print('')
     else :
	     word= wrd.split(':')[-1]
	     word1= word.split(',')[0]
	     bot.send_message(message.chat.id,word1)
bot.polling(True)


