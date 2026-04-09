import telebot
import random
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8365110465:AAF5i3MQnm64M-iyCSLomlnjc3nqhJEM0OM"
bot = telebot.TeleBot(TOKEN, parse_mode="Markdown")
def get_user_name(user):
    if user.username:
        return f"@{user.username}"
    else:
        return f"[{user.first_name}](tg://user?id={user.id})"

efsane = [
    "Aranızdaki bağ tarif edilemeyecek kadar güçlü.",
    "Bu uyum nadir bulunur, gerçekten özelsiniz.",
    "Kalpleriniz sanki aynı ritimde atıyor.",
    "Birbirinizi tamamlayan iki parça gibisiniz.",
    "Bu kadar uyum tesadüf olamaz.",
    "Göz göze gelmeniz bile yeterli olabilir.",
    "Aranızda çok derin bir bağ var.",
    "Bu ilişki uzun ve sağlam olur.",
    "Birbiriniz için yaratılmış gibisiniz.",
    "Aranızdaki enerji çok farklı bir seviyede.",
    "Bu uyum kolay kolay yakalanmaz.",
    "Birlikteyken her şey daha anlamlı olur.",
    "Bu bağ zamanla daha da güçlenir.",
    "Gerçek bir aşkın başlangıcı olabilir.",
    "Birbirinizi anlamanız çok doğal olacak.",
    "Bu ilişki güven üzerine kurulur.",
    "Kalbiniz doğru kişiyi bulmuş gibi.",
    "Birlikte çok güzel anılar birikir.",
    "Bu uyum gerçekten etkileyici.",
    "Aranızda özel bir hikaye yazılacak gibi."
]
cok_iyi = [
    "Aranızda ciddi bir çekim var.",
    "Birbirinize karşı boş değilsiniz.",
    "Bu ilişki güzel başlayabilir.",
    "Aranızda sıcak bir enerji var.",
    "Birlikte vakit geçirmek keyifli olur.",
    "Bu bağ zamanla büyüyebilir.",
    "Birbirinize uyum sağlamak zor olmayacak.",
    "Güzel bir ilişki potansiyeli var.",
    "Aranızdaki çekim fark ediliyor.",
    "İlk adımı atarsanız devamı gelir.",
    "Birbirinizi anlamaya açıksınız.",
    "Bu ilişki sizi mutlu edebilir.",
    "Aranızda doğal bir yakınlık var.",
    "Birlikteyken rahat hissedersiniz.",
    "İkiniz de uyum sağlayabilecek yapıdasınız.",
    "Bu bağ gelişmeye çok açık.",
    "Zamanla daha da yakınlaşırsınız.",
    "Aranızdaki iletişim güçlü olabilir.",
    "Birbirinize karşı ilginiz artabilir.",
    "Güzel bir hikaye başlayabilir."
]

# 🙂
iyi = [
    "Aranızda bir uyum var.",
    "Zamanla güzel bir bağ oluşabilir.",
    "Birbirinizi tanırsanız daha iyi olur.",
    "Bu ilişki emek ister ama olabilir.",
    "Ufak bir kıvılcım var.",
    "Birlikte vakit geçirmek keyifli olabilir.",
    "İlk adım önemli burada.",
    "Birbirinize alışabilirsiniz.",
    "Bu bağ gelişmeye açık.",
    "Zamanla daha iyi anlaşabilirsiniz.",
    "Ortak noktalar bulabilirsiniz.",
    "Bu ilişki sabır ister.",
    "Başlangıç için fena değil.",
    "Daha iyi olabilir.",
    "Biraz çaba ile ilerler.",
    "İletişim önemli olacak.",
    "Orta seviyede uyum var.",
    "Zaman gösterecek.",
    "Şans vermeye değer.",
    "Kararsız ama umut var."
]
orta = [
    "Biraz karışık bir uyum.",
    "Olabilir de olmayabilir de.",
    "Zamanla netleşir.",
    "İkinizin çabasına bağlı.",
    "Çok güçlü değil ama var.",
    "Zor bir ilişki olabilir.",
    "Biraz uğraş gerektirir.",
    "Kararsız bir durum.",
    "Birbirinizi anlamanız gerek.",
    "İletişim olmazsa zor.",
    "Orta seviyede bir bağ.",
    "İlerleyebilir ama garanti değil.",
    "Sabır önemli.",
    "İlişki denge ister.",
    "Çok kolay olmayacak.",
    "Zaman belirleyici olur.",
    "Biraz riskli.",
    "Şartlara bağlı değişir.",
    "Net bir şey yok.",
    "Karışık sinyaller var."
]
kotu = [
    "Aranızda güçlü bir uyum görünmüyor.",
    "Bu ilişki zor başlayabilir.",
    "Pek enerji yok gibi.",
    "Birbirinize uzak kalabilirsiniz.",
    "Zor bir eşleşme.",
    "Çok uyumlu değilsiniz.",
    "Farklı dünyalar gibisiniz.",
    "Bağ kurmak zor olabilir.",
    "İletişim sıkıntı yaratabilir.",
    "Zayıf bir eşleşme.",
    "Başlamak bile zor olabilir.",
    "Uyum düşük seviyede.",
    "Birbirinizi anlamakta zorlanırsınız.",
    "Bu ilişki yürümeyebilir.",
    "Fazla ortak nokta yok.",
    "Zor bir kombinasyon.",
    "Uyumsuzluk baskın.",
    "İlişki yıpratıcı olabilir.",
    "Zor bir süreç olur.",
    "Bu eşleşme pek umut vermiyor."
]

def yorum_getir(yuzde):
    if yuzde >= 95:
        return random.choice(efsane)
    elif yuzde >= 85:
        return random.choice(cok_iyi)
    elif yuzde >= 70:
        return random.choice(iyi)
    elif yuzde >= 50:
        return random.choice(orta)
    else:
        return random.choice(kotu)
def ana_menu():
    markup = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton("➕ Beni Gruba Ekle", url="https://t.me/erosasikbot?startgroup=botstart")
    btn2 = InlineKeyboardButton("👨‍💻 Kurucu", callback_data="kurucu")
    btn3 = InlineKeyboardButton("ℹ️ Hakkında", callback_data="hakkimda")
    btn4 = InlineKeyboardButton("❓ Yardım", callback_data="yardim")
    markup.add(btn1, btn2, btn3, btn4)
    return markup
@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, 
                         "✨ *Eros Aşk Botu'na Hoş Geldin!* ✨\n\n"
                         "💘 Beni bir gruba ekle ve /eros komutuyla rastgele iki kişinin aşk uyumunu öğren!\n\n"
                         "🔮 *Nasıl Kullanılır?*\n"
                         "➡️ Beni grubuna ekle\n"
                         "➡️ `/eros` yaz ve sihri izle\n\n"
                         "💫 Aşkın kalbine yolculuk yap!",
                         reply_markup=ana_menu())
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "kurucu":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🔙 Geri", callback_data="geri"))
        markup.add(InlineKeyboardButton("💬 İletişim", url="https://t.me/kyattin"))
        
        bot.edit_message_text("👑 *Botun Kurucusu*\n\n"
                              "📝 İsim: Eros Team\n"
                              "💬 Kullanıcı adı: @SihalBen\n"
                              "⭐ Destek ve iletişim için kurucuya yazabilirsin!",
                              call.message.chat.id, call.message.message_id, 
                              reply_markup=markup, parse_mode="Markdown")
    
    elif call.data == "hakkimda":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🔙 Geri", callback_data="geri"))
        
        bot.edit_message_text("ℹ️ *Eros Aşk Botu Hakkında*\n\n"
                              "💘 Bu bot, gruplarda rastgele iki kişi seçer ve aşk uyumluluğunu gösterir.\n\n"
                              "✨ *Özellikler:*\n"
                              "• 🎲 Rastgele eşleştirme\n"
                              "• 📊 %1 ile %100 arasında uyumluluk\n"
                              "• 💬 Özel yorumlar\n"
                              "• 🎉 Eğlenceli ve romantik\n\n"
                              "📌 *Versiyon:* 2.0\n"
                              "👨‍💻 *Yapımcı:* @kyattin\n\n"
                              "🔧 *Komutlar:*\n"
                              "• /start - Botu başlat\n"
                              "• /eros - Aşk uyumunu ölç (sadece grup)",
                              call.message.chat.id, call.message.message_id, 
                              reply_markup=markup, parse_mode="Markdown")
    
    elif call.data == "yardim":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🔙 Geri", callback_data="geri"))
        
        bot.edit_message_text("❓ *Yardım Menüsü*\n\n"
                              "📌 *Nasıl Kullanılır?*\n\n"
                              "1️⃣ Beni grubuna ekle\n"
                              "2️⃣ `/eros` komutunu gönder\n"
                              "3️⃣ Rastgele iki kişi eşleşir\n"
                              "4️⃣ Aşk uyumluluğunu öğren!\n\n"
                              "💡 *İpucu:* Bot sadece gruplarda çalışır!\n\n"
                              "🔗 *Botu eklemek için:*\n"
                              "• 'Beni Gruba Ekle' butonunu kullan",
                              call.message.chat.id, call.message.message_id, 
                              reply_markup=markup, parse_mode="Markdown")
    
    elif call.data == "geri":
        bot.edit_message_text("✨ *Eros Aşk Botu'na Hoş Geldin!* ✨\n\n"
                              "💘 Beni bir gruba ekle ve /eros komutuyla rastgele iki kişinin aşk uyumunu öğren!\n\n"
                              "🔮 *Nasıl Kullanılır?*\n"
                              "➡️ Beni grubuna ekle\n"
                              "➡️ `/eros` yaz ve sihri izle\n\n"
                              "💫 Aşkın kalbine yolculuk yap!",
                              call.message.chat.id, call.message.message_id, 
                              reply_markup=ana_menu(), parse_mode="Markdown")
@bot.message_handler(commands=['eros'])
def eros(message):
    chat_id = message.chat.id
    if message.chat.type not in ['group', 'supergroup']:
        bot.reply_to(message, "❌ Bu komut sadece gruplarda kullanılabilir!\n\nBeni bir gruba ekle ve tekrar dene.")
        return

    try:
        members = bot.get_chat_administrators(chat_id)
        if len(members) < 2:
            members = bot.get_chat_members(chat_id)
             
        if len(members) < 2:
            bot.reply_to(message, "❌ Yeterli kişi yok! En az 2 kişi olmalı.")
            return
        kisi1, kisi2 = random.sample(members, 2)
        user1 = kisi1.user
        user2 = kisi2.user
        isim1 = get_user_name(user1)
        isim2 = get_user_name(user2)
        yuzde = random.randint(1, 100)
        yorum = yorum_getir(yuzde)
        if yuzde >= 85:
            emoji = "💘🔥"
        elif yuzde >= 70:
            emoji = "💖✨"
        elif yuzde >= 50:
            emoji = "💕🌸"
        else:
            emoji = "💔🥀"

        text = f"""
🏹 Eros hedefini şaşırmadı...💘
┏━━━━━━━━━━━━━━━━━┓
💑  {isim1} 💞 {isim2}
┗━━━━━━━━━━━━━━━━━┛
📊 *Uyumluluk:* *%{yuzde}*
💬 _{yorum}_

━━━━━━━━━━━━━━━━━━━
✨ *Bazı karşılaşmalar tesadüf değildir.*
"""
        bot.send_message(chat_id, text, parse_mode="Markdown")

    except Exception as e:
        bot.reply_to(message, f"  {str(e)}")

print("Bot pasif")
bot.infinity_polling()