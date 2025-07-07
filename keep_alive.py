from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ HUESA Bot is alive."

def keep_alive():
    Thread(target=app.run, kwargs={"host": "0.0.0.0", "port": 8080}).start()
