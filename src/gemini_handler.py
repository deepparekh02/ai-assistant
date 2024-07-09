import os
import requests
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_draft(email_content):
    response = model.generate_content(["Draft the body of the reply to this email in a style suiting the tone of the sender", email_content])
    return response.text

def summarize_emails(emails):
    email_texts = "\n\n".join(emails)
    response = model.generate_content(["Summarize these emails for me and highlight anything crucial", email_texts])
    return response.text

def summarize_channels(messages):
    message_texts = "\n\n".join(messages)
    response = model.generate_content(["For each channel, give me a summary of all the messages and highlight anything crucial", message_texts])
    return response.text
