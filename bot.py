from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '7737557959:AAHdDUiREt-aT9QYxdc4bR4Vr-Ik4hPiu7k'

duas = {
    'المرض': "اللهم رب الناس، اذهب البأس، اشفِ أنت الشافي، لا شفاء إلا شفاؤك...",
    'السفر': "اللهم إني أعوذ بك من وعثاء السفر، وكآبة المنظر، وسوء المنقلب في المال والأهل والولد...",
    'الصباح': "اللهم بك أصبحنا وبك أمسينا، وبك نحيا وبك نموت وإليك النشور...",
    'المساء': "أمسينا على فطرة الإسلام، وعلى كلمة الإخلاص، وعلى دين نبينا محمد صلى الله عليه وسلم..."
}

buttons = [['المرض', 'السفر'], ['الصباح', 'المساء']]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_keyboard = ReplyKeyboardMarkup(buttons, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text(
        "السلام عليكم! اختر نوع الدعاء الذي تود سماعه:",
        reply_markup=reply_keyboard
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text in duas:
        await update.message.reply_text(duas[text])
    else:
        await update.message.reply_text("اختار من القائمة فقط من فضلك.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == '__main__':
    main()