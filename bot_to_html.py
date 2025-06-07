import os
import html
import asyncio
from datetime import datetime
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = "7988347665:AAHYqtaYB5-mDeuwfkgyJW52Lki8UhSrpJQ"
POSTS_FILE = os.path.expanduser("~/berenjian-site/posts.html")

def ensure_html_file():
    if not os.path.exists(POSTS_FILE):
        with open(POSTS_FILE, "w") as f:
            f.write("<html><head><meta charset='utf-8'><title>پست‌ها</title></head><body>\n")

def save_post_to_html(text: str, photo_url: str = None):
    ensure_html_file()
    with open(POSTS_FILE, "a") as f:
        f.write("<div style='margin-bottom:20px; border-bottom:1px solid #ccc; padding:10px;'>\n")
        if photo_url:
            f.write(f"<img src='{photo_url}' style='max-width:100%; border-radius:12px;'><br>\n")
        if text:
            f.write(f"<p>{html.escape(text)}</p>\n")
        f.write(f"<small>{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</small>\n</div>\n")

async def handle_channel_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.channel_post
    text = message.caption or message.text or ""
    photo_url = None

    if message.photo:
        file = await context.bot.get_file(message.photo[-1].file_id)
        photo_url = file.file_path

    save_post_to_html(text, photo_url)
    print("✅ پست جدید ذخیره شد.")

async def start_bot():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.UpdateType.CHANNEL_POST, handle_channel_post))
    print("✅ ربات در حال اجراست...")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await asyncio.Event().wait()  # نگه‌داشتن برنامه

if __name__ == "__main__":
    try:
        asyncio.run(start_bot())
    except RuntimeError:
        # رفع خطای event loop در ترموکس
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(start_bot())
