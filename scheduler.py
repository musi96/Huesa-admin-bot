import schedule
import time
from datetime import datetime
from main import post_news, post_scholarships, post_tip, post_note, post_bio, post_image
from keep_alive import keep_alive

keep_alive()

print("🤖 Bot is running...")

# Scheduled UTC times (Ethiopia UTC+3)
schedule.every().day.at("05:00").do(post_news)         # 8 AM Ethiopia
schedule.every().day.at("07:00").do(post_scholarships) # 10 AM
schedule.every().day.at("09:50").do(post_tip)          # 12 PM
schedule.every().day.at("11:00").do(post_note)         # 2 PM
schedule.every().day.at("14:00").do(post_bio)          # 4 PM
schedule.every().day.at("17:00").do(post_image)        # 6 PM

while True:
    print(f"⏰ {datetime.utcnow()} - checking...")
    schedule.run_pending()
    time.sleep(60)
