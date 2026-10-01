import os
import threading
import telebot
from flask import Flask

# TOKEN diambil otomatis dari Environment Variable di Render
TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

# Web Server Mini agar Render tidak "Tidur"
app = Flask(__name__)


@app.route("/")
def home():
  app.logger.info("Ping received, keeping bot alive.")
  return "Bot Telegram sedang aktif dan berjalan 24/7!"


def run_web():
  port = int(os.environ.get("PORT", 10000))
  app.run(host="0.0.0.0", port=port)


# Logika Bot Telegram
@bot.message_handler(commands=["start"])
def kirim_selamat_datang(message):
  bot.reply_to(
      message,
      (
          "Halo! Bot Anda sudah online 24 jam di Render dan siap menerima"
          " form!"
      ),
  )


if __name__ == "__main__":
  # Jalankan web server di background
  t = threading.Thread(target=run_web)
  t.start()

  # Jalankan bot telegram
  print("Bot sedang berjalan...")
  bot.infinity_polling()
