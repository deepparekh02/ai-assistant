import os
import base64
from datetime import datetime, timedelta
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

class EmailHandler:
    def __init__(self, google_client_id, google_client_secret, google_refresh_token):
        self.service = self.authenticate(google_client_id, google_client_secret, google_refresh_token)

    def authenticate(self, google_client_id, google_client_secret, google_refresh_token):
        creds = Credentials.from_authorized_user_info({
            "client_id": google_client_id,
            "client_secret": google_client_secret,
            "refresh_token": google_refresh_token,
            "token_uri": "https://oauth2.googleapis.com/token"
        })

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        
        service = build('gmail', 'v1', credentials=creds)
        return service

    def read_emails(self, hours=24):
        hours_ago = (datetime.now() - timedelta(hours=hours)).strftime('%Y/%m/%d')
        query = f'is:unread after:{hours_ago}'
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