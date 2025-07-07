from telegram import Bot
from news_scraper import get_econ_news
from scholarships_scraper import get_scholarships
from ai_generator import get_econ_tip, get_econ_note, get_econ_bio
from image_search import download_image_for_keyword

BOT_TOKEN = "7808230335:AAG4gKjKROwjRJhodEWSJSVYLSlhFXHhrXQ"
CHANNEL = "@sample_123456"
FOOTER = "\n\n📢 @HUESAchannel"

bot = Bot(token=BOT_TOKEN)

def send_post_with_image(text, keyword):
    img_path = download_image_for_keyword(keyword)
    if img_path:
        bot.send_photo(chat_id=CHANNEL, photo=open(img_path, "rb"), caption=text + FOOTER)
    else:
        bot.send_message(chat_id=CHANNEL, text=text + FOOTER)

def post_news():
    for news in get_econ_news():
        # Use first 3 words as image keyword
        keyword = " ".join(news.split()[0:3])
        send_post_with_image(news, keyword)

def post_scholarships():
    for sch in get_scholarships():
        # Use university name or "university logo"
        if "DAAD" in sch:
            keyword = "DAAD university logo"
        elif "Erasmus" in sch:
            keyword = "Erasmus Mundus logo"
        else:
            keyword = "African Union logo"
        send_post_with_image(sch, keyword)

def post_tip():
    tip = get_econ_tip()
    send_post_with_image(f"💡 Tip of the Day\n{tip}", "economics study tips")

def post_note():
    note = get_econ_note()
    send_post_with_image(f"📘 Economic Theory\n{note}", "economics theory")

def post_bio():
    bio = get_econ_bio()
    # Extract economist name for keyword (naive)
    first_line = bio.splitlines()[0] if bio else "economist"
    keyword = first_line.split()[-1] if first_line else "economist"
    send_post_with_image(f"👤 Economist Bio\n{bio}", keyword)
