import os
import requests
from dotenv import load_dotenv

load_dotenv()

class DiscordNotifier:
    def __init__(self):
        self.url = os.getenv("DISCORD_WEBHOOK_URL")

    def send_message(self, message):
        if not self.url:
            print("⚠️ Discord Webhook URL missing.")
            return

        payload = {"content": message}
        
        try:
            response = requests.post(self.url, json=payload, timeout=10)
            if response.status_code == 204:
                print("✅ Discord Notification Sent!")
        except Exception as e:
            print(f"❌ Notifier Error: {e}")

if __name__ == "__main__":
    notifier = DiscordNotifier()
    notifier.send_message("🤖 **Sovereign Agent:** System Online. Testing Discord Link.")