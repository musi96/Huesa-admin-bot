import requests
from PIL import Image
import os

def download_image_for_keyword(keyword, filename="temp.jpg"):
    url = f"https://source.unsplash.com/600x400/?{keyword.replace(' ', '%20')}"
    resp = requests.get(url)
    if resp.status_code == 200:
        with open(filename, "wb") as f:
            f.write(resp.content)
        try:
            with Image.open(filename) as img:
                return filename
        except:
            os.remove(filename)
    return None
