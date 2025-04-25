from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

TOKEN = os.environ["TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    # Fotoğraf URL'si
    photo_url = "https://iili.io/3VJTP9f.jpg"  # burayı kendi fotoğraf URL’inle değiştir

    # Butonlar
    keyboard = [
        [InlineKeyboardButton("👉GÜNCEL GİRİŞ👈", url="https://csnr.site/MHHaD")],
        [InlineKeyboardButton("🎁BONUS AL🎁", url="https://csnr.site/MHHaD")],
        [InlineKeyboardButton("✅KAYIT OL✅", url="https://csnr.site/MHHaD")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Fotoğraf + açıklama + buton gönderimi
    await context.bot.send_photo(
        chat_id=chat_id,
        photo=photo_url,
        caption = '🔐 Casinra’ya Hoş Geldin! \n Hızlı, güvenli ve kazanç dolu bir deneyim seni bekliyor! \n\n🎁 Sadece Bugüne Özel Fırsatlar: \n⚡ %20 Kayıp Bonusu \n🎁 100 TL Deneme Bonusu\n🤝 %100 Hoşgeldin Bonusu\n🤞🏻 %50’ye Varan Rakeback İmkanı\n\n📱 Hemen Casinra’ya Giriş Yap, Fırsatları Kaçırma!\n\n🍀 Bota özel sürpriz bonuslar ve özel porsiyonlar için takipte kal!',
        reply_markup=reply_markup
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, start))
    

    print("Bot başlatıldı...")
    app.run_polling()
