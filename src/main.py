import os
import argparse
from email_handler import EmailHandler
from gemini_handler import generate_draft, summarize_emails, summarize_channels
from slack_handler import SlackHandler
from dotenv import load_dotenv

load_dotenv()
SLACK_USER_ID = os.getenv('SLACK_USER_ID')

def main(hours=24):
    email_handler = EmailHandler()
    slack_handler = SlackHandler()
    
    emails = email_handler.read_emails(hours=hours)
    email_contents = []

    for email in emails:
        email_content = email['snippet']
        email_contents.append(email_content)
        headers = {h['name']: h['value'] for h in email['payload']['headers']}
        subject = headers.get('Subject', 'No Subject')
        from_email = headers.get('From', '')
        
        if "reply-to" in email['payload']['headers'] or "RE:" in subject or "FWD:" in subject:
            email_contents.append(email_content)
            response = generate_draft(email_content)
            email_handler.create_draft("Re: " + subject, response, from_email)
    
    email_summary = summarize_emails(email_contents)
    print(email_summary)
    # email_handler.send_email("Daily Email Summary", email_summary, 'deep.parekh02@gmail.com')
    
    
    channels = slack_handler.get_channels()
    slack_contents = []

    for channel in channels:
        messages = slack_handler.read_messages(channel['id'], channel['name'], hours=hours)
        slack_contents.extend(messages)

    slack_summary = summarize_channels(slack_contents)
    print(slack_summary)
    # email_handler.send_email("Daily Slack Summary", slack_summary, 'deep.parekh02@gmail.com')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--hours', type=int, help='an integer for the accumulator')
    args = parser.parse_args()
    main(hours=args.hours)
