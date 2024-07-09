# AI Assistant for Communication

https://files.oaiusercontent.com/file-0acmjATOFp1powVMwJTF21TO?se=2024-07-09T10%3A36%3A53Z&sp=r&sv=2023-11-03&sr=b&rscc=max-age%3D604800%2C%20immutable%2C%20private&rscd=attachment%3B%20filename%3D89163bc5-00e5-46e9-8351-20d3b4b797c9.webp&sig=cypxWDdzx6/n0CS0I1el9n0NHRFk6VOHYSQaxD0tp7M%3D![image](https://github.com/deepparekh02/ai-assistant/assets/65657471/3e5ace13-5b18-4f38-83ac-04aee1a75fd6)

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


