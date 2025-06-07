import asyncio
from telegram import Bot

BOT_TOKEN = "7988347665:AAHYqtaYB5-mDeuwfkgyJW52Lki8UhSrpJQ"

bot = Bot(token=BOT_TOKEN)

HTML_FILE = "/data/data/com.termux/files/home/berenjian-site/posts.html"

async def fetch_and_save():
    updates = await bot.get_updates()
    posts = []
    for u in updates:
        if u.message:
            txt = u.message.text or ''
            if u.message.caption:
                txt += f"\n{u.message.caption}"
            if txt:
                posts.append(f"<p>{txt}</p>")
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(posts))
    print("✅ فایل posts.html بروزرسانی شد.")

asyncio.run(fetch_and_save())
