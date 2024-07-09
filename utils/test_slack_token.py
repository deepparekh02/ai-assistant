import os
import requests
from dotenv import load_dotenv

load_dotenv()

SLACK_USER_TOKEN = os.getenv('SLACK_USER_TOKEN')

def get_user_id():
    url = "https://slack.com/api/auth.test"
    headers = {
        "Authorization": f"Bearer {SLACK_USER_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    if data.get("ok"):
        print(f"User ID: {data['user_id']}")
    else:
        print("Error fetching user ID")
        print(response.text)

if __name__ == "__main__":
    get_user_id()
