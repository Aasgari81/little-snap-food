import logging
from telegram import Update
from telegram.ext import *
from alisdb import * 


level = 0 
def start_command(update, context):
    update.message.reply_text("سلام به بات رزرو آنلاین غدای من و علی :) خیلی خوش اومدید❤️ \n برای شروع لطفا ایمیل خود را وارد کنید ")


def message_handler(update, context):
    mydb_cursor.execute("SELECT email, password FROM customer")
    customers_info = mydb_cursor.fetchall()
    text = str(update.message.text)
    emial_checked = False

    if level == 0:
        for customer in customers_info:
            if text not in customer:
                update.message.reply_text("متاسفانه ایمیل شما یافت نشد 🥲")
            else:
                update.message.reply_text("لطفا رمز عبور خودتو برا ما بفرستید.") 
                level += 1






def main():
    updater = Updater("5468770056:AAF7wFuThfGLpeoOpoYEXzPUs7DQ1N8KnDM", use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    while True:
        dp.add_handler(MessageHandler(Filters.text, message_handler))

        updater.start_polling()
        updater.idle()

main()
