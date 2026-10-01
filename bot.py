import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 My Trades Journal\n\n"
        "Welcome!\n"
        "Use /newtrade to add a new trade.\n"
        "Use /day for today's statistics.\n"
        "Use /week for weekly statistics."
    )

async def newtrade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📝 New Trade\n\n"
        "Trading journal system is ready.\n"
        "Full trade-entry flow will be added next."
    )

async def day(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📅 Day P&L\n\nNo trades recorded yet.")

async def week(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📆 Weekly P&L\n\nNo trades recorded yet.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("newtrade", newtrade))
    app.add_handler(CommandHandler("day", day))
    app.add_handler(CommandHandler("week", week))

    app.run_polling()

if __name__ == "__main__":
    main()
