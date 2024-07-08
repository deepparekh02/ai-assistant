from email_handler import EmailHandler
from gemini_handler import generate_draft, summarize_emails

def main():
    email_handler = EmailHandler()

    emails = email_handler.read_emails()
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
    email_handler.send_email("Daily Email Summary", email_summary, 'deep.parekh02@gmail.com')

if __name__ == "__main__":
    main()
