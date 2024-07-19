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

@app.route('/api/slack-summary', methods=['POST'])
def get_slack_summary():
    data = request.json
    slack_user_token = data['SLACK_USER_TOKEN']
    slack_user_id = data['SLACK_USER_ID']
    hours = data.get('hours', 24)
    
    slack_handler = SlackHandler(slack_user_id, slack_user_token)
    
    slack_channels = slack_handler.get_channels()
    slack_contents = []
    for channel in slack_channels:
        messages = slack_handler.read_messages(channel['id'], channel['name'], hours=hours)
        slack_contents.extend(messages)
    slack_summary = summarize_channels(slack_contents)

    summary = {'slack_summary': slack_summary}

    return jsonify(summary)
    
@app.route('/api/email-summary', methods=['POST'])
def get_email_summary():
    data = request.json
    google_client_id = data['GOOGLE_CLIENT_ID']
    google_client_secret = data['GOOGLE_CLIENT_SECRET']
    google_refresh_token = data['GOOGLE_REFRESH_TOKEN']
    hours = data.get('hours', 24)
    
    email_handler = EmailHandler(google_client_id, google_client_secret, google_refresh_token)
    
    emails = email_handler.read_emails(hours=hours)
    email_contents = []
    for email in emails:
        email_content = email['snippet']
        email_contents.append(email_content)

    email_summary = summarize_emails(email_contents)
    
    summary = {'email_summary': email_summary}
    return jsonify(summary)

@app.route('/api/draft-response-emails', methods=['POST'])
def draft_response_emails():
    data = request.json
    google_client_id = data['GOOGLE_CLIENT_ID']
    google_client_secret = data['GOOGLE_CLIENT_SECRET']
    google_refresh_token = data['GOOGLE_REFRESH_TOKEN']
    hours = data.get('hours', 24)
    
    email_handler = EmailHandler(google_client_id, google_client_secret, google_refresh_token)
    
    emails = email_handler.read_emails(hours=hours)
    drafts_created = []
    for email in emails:
        email_content = email['snippet']
        headers = {h['name']: h['value'] for h in email['payload']['headers']}
        subject = headers.get('Subject', 'No Subject')
        from_email = headers.get('From', '')
        if "reply-to" in email['payload']['headers'] or "RE:" in subject or "FWD:" in subject:
            response = generate_draft(email_content)
            email_handler.create_draft("Re: " + subject, response, from_email)
            draft = {"subject": "Re: " + subject, "response": response, "to": from_email}
            drafts_created.append(draft)
    
    if (len(drafts_created) == 0):
        summary = {
            "message": "No drafts created as none needed. Please check at your own discretion too.",
            "drafts": drafts_created
        }
    else:
        summary = {
            "message": str(len(drafts_created)) + " Drafts added successfully to your email account",
            "drafts": drafts_created
        }

    return jsonify(summary)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
