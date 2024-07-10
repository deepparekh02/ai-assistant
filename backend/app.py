import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from email_handler import EmailHandler
from slack_handler import SlackHandler
from gemini_handler import generate_draft, summarize_emails, summarize_channels

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/summary', methods=['POST'])
def get_summary():
    data = request.json
    google_client_id = data['GOOGLE_CLIENT_ID']
    google_client_secret = data['GOOGLE_CLIENT_SECRET']
    google_refresh_token = data['GOOGLE_REFRESH_TOKEN']
    slack_user_token = data['SLACK_USER_TOKEN']
    slack_user_id = data['SLACK_USER_ID']
    hours = data.get('hours', 24)

    email_handler = EmailHandler(google_client_id, google_client_secret, google_refresh_token)
    slack_handler = SlackHandler(slack_user_id, slack_user_token)

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

    slack_channels = slack_handler.get_channels()
    slack_contents = []
    for channel in slack_channels:
        messages = slack_handler.read_messages(channel['id'], channel['name'], hours=hours)
        slack_contents.extend(messages)
    slack_summary = summarize_channels(slack_contents)

    summary = {
        'email_summary': email_summary,
        'slack_summary': slack_summary
    }

    return jsonify(summary)

if __name__ == '__main__':
    app.run(debug=True)
