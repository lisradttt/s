from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen



bot = Client(
    "mo",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    # تحميل البوتات المحفوظة تلقائياً
    try:
        from Maker.KERO import auto_bot
        print("[INFO]: جاري تحميل البوتات المحفوظة...")
        await auto_bot()
        print("[INFO]: تم تحميل البوتات بنجاح")
    except Exception as e:
        print(f"[WARNING]: خطأ في تحميل البوتات: {e}")
    
    MAMI = "ISIIQ"
    await bot.send_message(MAMI, "**البوت اشتغل يبيبي 💋 .**")
    await bot.send_message(MAMI,"البتنجان اخد البرجر فحته تانيه")
    print("[INFO]: تم تشغيل الصانع وارسال رسالة للمطور⚡🚦.")
    await idle()

