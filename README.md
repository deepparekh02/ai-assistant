# AI Assistant for Emails and Slack Messages

### Table of Contents
- Description
- Inspiration
- Technologies and Libraries
- Main Features
- Installation
- Usage
- Screenshots
- Video Demo

### Description

This project is an AI Assistant that utilizes the Gemini AI to generate summaries for emails and Slack messages. It also drafts responses to emails, helping users manage their communications more efficiently. The assistant periodically performs these tasks using credentials from a .env file, ensuring user data privacy and security.

### Technologies and Libraries

- Python
-- Google Cloud APIs for seamless integration and authentication:
--- google-auth
--- google-auth-oauthlib
--- google-auth-httplib2
--- google-api-python-client
-- Environment Management:
--- python-dotenv
-- AI and Machine Learning:
--- google-generativeai for leveraging state-of-the-art LLMs
-- Communication Platform Integration:
--- slack-sdk

### Main Features

1) Advanced Email Summarization: 
Utilizes Gemini AI to generate insightful and concise summaries of email threads using sophisticated prompt engineering techniques.
2) Intelligent Slack Summarization: 
Produces comprehensive summaries of Slack conversations, ensuring users stay updated without reading every message.
3) AI-Driven Email Response Drafting: 
Employs machine learning algorithms to draft contextually relevant email responses, tailored to user preferences and communication style.
4) Automated and Secure Workflow: 
Periodically performs tasks using credentials securely stored in a .env file, ensuring data privacy and continuous operation.
5) Seamless AI API Integration: 
Integrates with Google Generative AI APIs to harness the full potential of LLMs for natural language understanding and generation.
