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
    caption = '🔐 <b>CASİNRA’YA HOŞ GELDİN!</b>\n'
              'Hızlı ve güvenli işlem ayrıcalığını keşfet!\n\n'
              '✨ <b>Sadece Sana Özel Fırsatlar:</b>\n'
              '⚡ %100 Happy Hour Bonusu\n'
              '🎁 100 TL Deneme Bonusu\n'
              '👑 VIP Seviye Atlama Bonusu\n'
              '🎰 %20 Anlık Discount\n\n'
              '🔥 VE DAHA FAZLASI SENİ BEKLİYOR!\n\n'
              '📲 <a href="https://csnr.site/MHHaD">Hemen Giriş Yap: CASİNRA GİRİŞ</a>\n\n'
              '🎉 Bota özel sürprizler ve özel porsiyonlar için takipte kal!',
    parse_mode='HTML',
    reply_markup=reply_markup
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, start))
    

    print("Bot başlatıldı...")
    app.run_polling()
