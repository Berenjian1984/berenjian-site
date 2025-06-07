#!/data/data/com.termux/files/usr/bin/bash

# مسیر پروژه
cd ~/berenjian-site

# اجرای اسکریپت برای دریافت پست‌ها
python fetch_posts.py

# افزودن همه فایل‌ها به git
git add .

# ساخت یک پیام کامیت
git commit -m "🔄 Auto update from Telegram"

# پوش به گیت‌هاب با استفاده از توکن
git push https://x-access-token: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@github.com/berenjian1984/berenjian-site.git main

# پیام موفقیت
echo "✅ آپلود در گیتهاب انجام شد."
