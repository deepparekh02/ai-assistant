# AI Assistant for Communication

<img src="https://github.com/deepparekh02/ai-assistant/assets/65657471/00888051-d86e-4562-9eb2-dfc90bf3402c" width=400>

### Table of Contents
- Description
- Inspiration
- Technologies and Libraries
- Main Features


### Description

This project is an AI Assistant that utilizes the Gemini AI to generate summaries for emails and Slack messages. It also drafts responses to emails, helping users manage their communications more efficiently. The assistant periodically performs these tasks using credentials from a .env file, and sends emails to you every desired time interval to keep you updated.

### Inspiration

The inspiration for this AI Assistant came from my own struggle to keep up with the loads of emails and Slack messages I receive daily. As an undergraduate juggling classes, projects, and internships, I found myself spending way too much time trying to sift through endless threads of messages and emails. I thought, "There has to be a smarter way to handle this!"

That's when I decided to harness the power of AI to help me out. I wanted something that could give me quick summaries and draft responses so I could focus on more important things—like coding, studying, or, let's be honest, binge-watching my favorite shows. This project was born out of a need for more efficiency and a desire to see how far I could push AI to make my life easier. Plus, it’s pretty cool to say you built an AI assistant. By the way, if you have read this far, let me tell you that this readme file was written by an LLM too.

### Technologies and Libraries

- Python
  - Google Cloud APIs for seamless integration and authentication:
    - google-auth
    - google-auth-oauthlib
    - google-auth-httplib2
    - google-api-python-client
  - Environment Management:
    - python-dotenv
  - AI and Machine Learning:
    - google-generativeai for leveraging state-of-the-art LLMs
  - Communication Platform Integration:
    - slack-sdk

### Main Features

1) **Advanced Email Summarization**: 
Utilizes Gemini AI to generate insightful and concise summaries of email threads using sophisticated prompt engineering techniques.
2) **Intelligent Slack Summarization**: 
Produces comprehensive summaries of Slack conversations, ensuring users stay updated without reading every message.
3) **AI-Driven Email Response Drafting**: 
Employs machine learning algorithms to draft contextually relevant email responses, tailored to user preferences and communication style.
4) **Automated and Secure Workflow**: 
Periodically performs tasks using credentials securely stored in a .env file, ensuring data privacy and continuous operation.
5) **Seamless AI API Integration**: 
Integrates with Google Generative AI APIs to harness the full potential of LLMs for natural language understanding and generation.


