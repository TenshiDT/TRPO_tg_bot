from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from commands import start, set_city, today, tomorrow, week, month, change_city, notification
from handlers import handle_text
from weather import get_weather

# ТОКЕН СЮДЫ МАЛЬЧИКИ
TOKEN = 'your_bot_token'

# Словарь для хранения выбранного города для каждого пользователя
user_city = {}

def main() -> None:
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("set_city", set_city))
    dp.add_handler(CommandHandler("today", today))
    dp.add_handler(CommandHandler("tomorrow", tomorrow))
    dp.add_handler(CommandHandler("week", week))
    dp.add_handler(CommandHandler("month", month))
    dp.add_handler(CommandHandler("change_city", change_city))
    dp.add_handler(CommandHandler("notification", notification))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
