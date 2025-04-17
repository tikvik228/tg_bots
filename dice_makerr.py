# Импортируем необходимые классы.
import logging
from telegram import ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler
from datetime import datetime

BOT_TOKEN = '7659787190:AAGnP4w_IXOK3YS-Qdz-N7qVK2ZCbTyj3qo'
# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

base_keyboard = [['/dice', '/timer']]
dice_keyboard = [['/6', '/2x6', '/20', '/back']]
timer_keyboard = [['/30s', '/1m', '/5m', '/back']]
close_keyboard = [['/close']]

base_markup = ReplyKeyboardMarkup(base_keyboard, one_time_keyboard=False)
dice_markup = ReplyKeyboardMarkup(dice_keyboard, one_time_keyboard=False)
timer_markup = ReplyKeyboardMarkup(timer_keyboard, one_time_keyboard=False)
active_timer_markup = ReplyKeyboardMarkup(close_keyboard, one_time_keyboard=False)

async def echo(update, context):
    await update.message.reply_text(f"Я получил сообщение {update.message.text}")

async def start(update, context):
    await update.message.reply_text('Привет, я бот-гадалка!')
    await update.message.reply_text("/dice: кинуть кубики, /timer: засечь время", reply_markup=base_markup)


def main():
    # Создаём объект Application.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    application = Application.builder().token(BOT_TOKEN).build()
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)

    # Регистрируем обработчик в приложении.
    application.add_handler(text_handler)
    application.add_handler(CommandHandler("start", start))

    # Запускаем приложение.
    application.run_polling()

# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()