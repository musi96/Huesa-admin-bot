import requests

HF_TOKEN = "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"
TEXT_API = "https://api-inference.huggingface.co/models/gpt2"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query_text(prompt):
    response = requests.post(TEXT_API, headers=headers, json={"inputs": prompt})
    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    return "❌ Failed to generate text."

def get_econ_tip():
    return query_text("Give a useful tip for undergraduate economics students.")

def get_econ_note():
    return query_text("Explain an important economic theory briefly.")

def get_econ_bio():
    return query_text("Write a short biography of a famous economist.")
