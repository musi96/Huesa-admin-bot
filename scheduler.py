import schedule
import time
from datetime import datetime
from main import post_news, post_scholarships, post_tip, post_note, post_bio, post_image
from keep_alive import keep_alive

keep_alive()

print("🤖 Bot is running...")

schedule.every().day.at("05:00").do(post_news)
schedule.every().day.at("07:00").do(post_scholarships)
schedule.every().day.at("09:00").do(post_tip)
schedule.every().day.at("11:00").do(post_note)
schedule.every().day.at("13:00").do(post_bio)
schedule.every().day.at("15:00").do(post_image)

while True:
    print(f"⏰ {datetime.utcnow()} - checking...")
    schedule.run_pending()
    time.sleep(60)
