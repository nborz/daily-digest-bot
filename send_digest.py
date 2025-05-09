import requests
import os

# Retrieve the token from GitHub Actions secrets
TOKEN = os.getenv("BOT_TOKEN")

# Replace with your actual chat/channel ID
CHAT_ID = "-1002693285869"

# Load message content from a file
with open("digest_message.txt", "r", encoding="utf-8") as f:
    MESSAGE = f.read()

def send_to_telegram():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": MESSAGE,
        "parse_mode": "HTML",
        "disable_web_page_preview": True
    }

    response = requests.post(url, data=payload)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

if __name__ == "__main__":
    send_to_telegram()
