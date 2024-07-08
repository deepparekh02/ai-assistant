import os
import base64
from datetime import datetime, timedelta
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv('.env')

class EmailHandler:
    def __init__(self):
        self.service = self.authenticate()

    def authenticate(self):
        creds = Credentials.from_authorized_user_info({
            "client_id": os.getenv("GOOGLE_CLIENT_ID"),
            "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
            "refresh_token": os.getenv("GOOGLE_REFRESH_TOKEN"),
            "token_uri": "https://oauth2.googleapis.com/token"
        })

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        
        service = build('gmail', 'v1', credentials=creds)
        return service

    def read_emails(self):
        one_day_ago = (datetime.now() - timedelta(days=1)).strftime('%Y/%m/%d')
        query = f'is:unread after:{one_day_ago}'
        results = self.service.users().messages().list(userId='me', labelIds=['INBOX'], q=query).execute()
        messages = results.get('messages', [])
        emails = []
        for message in messages:
            msg = self.service.users().messages().get(userId='me', id=message['id']).execute()
            emails.append(msg)
        return emails
    
    def create_draft(self, subject, body, to):
        message = {
            'raw': base64.urlsafe_b64encode(f'To: {to}\nSubject: {subject}\n\n{body}'.encode()).decode()
        }
        self.service.users().drafts().create(userId='me', body=message).execute()

    def send_email(self, subject, body, to):
        message = {
            'raw': base64.urlsafe_b64encode(f'To: {to}\nSubject: {subject}\n\n{body}'.encode()).decode()
        }
        self.service.users().messages().send(userId='me', body=message).execute()