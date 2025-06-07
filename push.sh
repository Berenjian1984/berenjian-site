#!/data/data/com.termux/files/usr/bin/bash

echo "📦 در حال آماده‌سازی فایل‌ها برای آپلود در GitHub..."

cd ~/berenjian-site

git add .
git commit -m "🔄 به‌روزرسانی خودکار سایت با ربات ترموکس"

# تنظیم ریموت با توکن (موقت)
git remote set-url origin https://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@github.com/berenjian1984/berenjian-site.git

git push origin main

# بازگرداندن ریموت به حالت عادی
git remote set-url origin https://github.com/berenjian1984/berenjian-site.git

echo "✅ با موفقیت آپلود شد: https://berenjian1984.github.io/berenjian-site/"
