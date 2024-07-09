# AI Assistant for Emails and Slack Messages

### Table of Contents
- Description
- Technologies and Libraries
- Main Features
- Installation
- Usage
- Screenshots
- Video Demo

### Description

This project is an AI Assistant that utilizes the Gemini AI to generate summaries for emails and Slack messages. It also drafts responses to emails, helping users manage their communications more efficiently. The assistant periodically performs these tasks using credentials from a .env file, ensuring user data privacy and security.

### Technologies and Libraries

Python
google-auth
google-auth-oauthlib
google-auth-httplib2
google-api-python-client
python-dotenv
google-generativeai
slack-sdk

### Main Features

1) Email Summarization:
Uses Gemini AI to generate concise summaries of email threads and to bring up anything crucial.
2) Slack Summarization:
Generates summaries of Slack messages in each channel to keep users updated and highlight tasks of urgency
3) Drafting Email Responses:
Prepares and puts draft responses in your inbox based on the context of the sender's email and personal user preferences.
4) Automated Workflow:
Performs periodic tasks using credentials stored in a .env file.
