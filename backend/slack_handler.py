import os
import time
import datetime
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

load_dotenv()

SLACK_USER_TOKEN = os.getenv('SLACK_USER_TOKEN')
SLACK_USER_ID = os.getenv('SLACK_USER_ID')

class SlackHandler:
    def __init__(self, slack_user_id, slack_user_token):
        self.client = WebClient(token=slack_user_token)
        self.slack_user_id = slack_user_id
        
    def get_channels(self):
        try:
            response = self.client.conversations_list(exclude_archived=True)
            channels = response['channels']
            return channels
        except SlackApiError as e:
            print(f"Error fetching channels: {e.response['error']}")
            return []

    def read_messages(self, channel_id, channel_name, hours):
        hours_ago = datetime.datetime.now() - datetime.timedelta(hours=hours)
        oldest_timestamp = int(time.mktime(hours_ago.timetuple()))
        try:
            response = self.client.conversations_history(
                channel=channel_id,
                oldest=oldest_timestamp
            )
            messages = [f"From {channel_name}: {message['text']}" for message in response['messages'] if 'text' in message and message['user'] != self.slack_user_id]
            return messages
        except SlackApiError as e:
            print(f"Error fetching messages: {e.response['error']}")
            return []