import os
import datetime
import html
from telegram import Bot

# اطلاعات شما
TOKEN = "7988347665:AAHYqtaYB5-mDeuwfkgyJW52Lki8UhSrpJQ"
CHANNEL_USERNAME = "@berenjian_ads"
HTML_PATH = "/data/data/com.termux/files/home/berenjian-site/posts.html"

bot = Bot(token=TOKEN)

# گرفتن آخرین پست‌های کانال
updates = bot.get_updates()
messages = []
for update in updates:
    if update.channel_post and update.channel_post.chat.username == CHANNEL_USERNAME[1:]:
        msg = update.channel_post.text_html or update.channel_post.caption_html
        if msg:
            messages.append(msg.strip())

# حذف پست‌های تکراری و انتخاب فقط 5 پست آخر
messages = list(dict.fromkeys(messages))[-5:]

# نوشتن داخل posts.html
with open(HTML_PATH, "w") as f:
    f.write("<html><body>\n")
    f.write("<h2>🗞 جدیدترین پست‌های کانال برنجیان Ads:</h2>\n")
    for m in reversed(messages):
        f.write(f"<div style='margin-bottom:20px;border-bottom:1px solid #ccc;padding:10px;'>{html.unescape(m)}</div>\n")
    f.write(f"<p style='color:gray;font-size:12px'>آخرین به‌روزرسانی: {datetime.datetime.now()}</p>\n")
    f.write("</body></html>")

# اجرای push.sh برای آپلود در GitHub
os.system("sh /data/data/com.termux/files/home/berenjian-site/push.sh")
