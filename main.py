from telegram import Bot
from news_scraper import get_econ_news
from scholarships_scraper import get_scholarships
from ai_generator import get_econ_tip, get_econ_note, get_econ_bio, generate_image

BOT_TOKEN = "7808230335:AAG4gKjKROwjRJhodEWSJSVYLSlhFXHhrXQ"
CHANNEL = "@sample_123456"
FOOTER = "\n\n📢 @HUESAchannel"

bot = Bot(token=BOT_TOKEN)

def post_news():
    for news in get_econ_news():
        bot.send_message(chat_id=CHANNEL, text=news + FOOTER, parse_mode="HTML")

def post_scholarships():
    for sch in get_scholarships():
        bot.send_message(chat_id=CHANNEL, text=sch + FOOTER, parse_mode="HTML")

def post_tip():
    tip = get_econ_tip()
    bot.send_message(chat_id=CHANNEL, text=f"💡 <b>Tip of the Day</b>\n{tip}" + FOOTER, parse_mode="HTML")

def post_note():
    note = get_econ_note()
    bot.send_message(chat_id=CHANNEL, text=f"📘 <b>Economic Theory</b>\n{note}" + FOOTER, parse_mode="HTML")

def post_bio():
    bio = get_econ_bio()
    bot.send_message(chat_id=CHANNEL, text=f"👤 <b>Economist Bio</b>\n{bio}" + FOOTER, parse_mode="HTML")

def post_image():
    img_file = generate_image("economic infographic")
    if img_file:
        bot.send_photo(chat_id=CHANNEL, photo=open(img_file, "rb"), caption="🖼️ AI-generated economic image\n" + FOOTER)
