import requests
from PIL import Image
import os

HF_TOKEN = "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"
TEXT_API = "https://api-inference.huggingface.co/models/gpt2"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query_text(prompt):
    response = requests.post(TEXT_API, headers=headers, json={"inputs": prompt})
    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    return "❌ Failed to generate text."

def generate_image(prompt="Economics AI Graphic", filename="econ_image.jpg"):
    image_url = f"https://source.unsplash.com/600x400/?{prompt.replace(' ', '%20')}"
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        try:
            with Image.open(filename) as img:
                print("✅ Image OK:", img.format)
                return filename
        except Exception as e:
            print("❌ Image Error:", e)
            os.remove(filename)
    return None

def get_econ_tip():
    return query_text("Give a useful tip for undergraduate economics students.")

def get_econ_note():
    return query_text("Explain an important economic theory briefly.")

def get_econ_bio():
    return query_text("Write a short biography of a famous economist.")
