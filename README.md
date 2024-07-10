# Briefly-AI

<img src="https://github.com/deepparekh02/ai-assistant/assets/65657471/00888051-d86e-4562-9eb2-dfc90bf3402c" width=400>

## Table of Contents
- [Description](#description)
- [Inspiration](#inspiration)
- [Technologies and Libraries](#technologies-and-libraries)
- [Main Features](#main-features)
- [How to Use](#how-to-use)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

## Description

Briefly AI is a cutting-edge AI Assistant designed to streamline your communication management. Leveraging advanced AI models and APIs, Briefly AI generates concise summaries for emails and Slack messages, drafts intelligent email responses, and automates these tasks for continuous operation. The assistant uses credentials stored in a secure `.env` file and operates seamlessly to keep you updated.

## Inspiration

The inspiration for this AI Assistant came from my own struggle to keep up with the loads of emails and Slack messages I receive daily. As an undergraduate juggling classes, projects, and internships, I found myself spending way too much time trying to sift through endless threads of messages and emails. I thought, "There has to be a smarter way to handle this!"

That's when I decided to harness the power of AI to help me out. I wanted something that could give me quick summaries and draft responses so I could focus on more important things—like coding, studying, or, let's be honest, binge-watching my favorite shows. This project was born out of a need for more efficiency and a desire to see how far I could push AI to make my life easier. Plus, it’s pretty cool to say you built an AI assistant. By the way, if you have read this far, let me tell you that this readme file was written by an LLM too.

## Technologies and Libraries

- **Frontend Technologies:**
  - Angular for a sleek and responsive user interface
  - Ngx-Markdown for rendering Markdown content
- **Backend Technologies:**
  - Python for robust backend operations
  - Flask for a lightweight and efficient web framework
- **Google Cloud APIs for seamless integration and authentication:**
  - `google-auth`
  - `google-auth-oauthlib`
  - `google-auth-httplib2`
  - `google-api-python-client`
- **Environment Management:**
  - `python-dotenv` for secure credential management
- **AI and Machine Learning:**
  - `google-generativeai` for state-of-the-art language models
- **Communication Platform Integration:**
  - `slack-sdk` for Slack integration
- **Others:**
  - `requests` for handling HTTP requests
  - `flask-cors` for handling cross-origin requests

## Main Features

- **Advanced Email Summarization:** Utilizes Gemini AI to generate insightful and concise summaries of email threads using sophisticated prompt engineering techniques.
- **Intelligent Slack Summarization:** Produces comprehensive summaries of Slack conversations, ensuring users stay updated without reading every message.
- **AI-Driven Email Response Drafting:** Employs machine learning algorithms to draft contextually relevant email responses, tailored to user preferences and communication style.
- **Automated and Secure Workflow:** Periodically performs tasks using credentials securely stored in a `.env` file, ensuring data privacy and continuous operation.
- **Seamless AI API Integration:** Integrates with Google Generative AI APIs to harness the full potential of LLMs for natural language understanding and generation.
- **User-Friendly Interface:** A modern and sleek frontend built with Angular, providing an intuitive user experience.
- **Multi-Platform Support:** Supports both email and Slack integrations, with future plans for additional platforms.
- **Real-Time Updates:** Keeps you informed with real-time summaries and drafts, enhancing productivity and efficiency.

## How to Use

1. **Enter your credentials:** Input your Google and Slack credentials securely into the `.env` file.
2. **Specify the time range:** Define the number of hours for which you want to generate summaries.
3. **Generate Summaries:** Click on the respective buttons to generate email or Slack summaries.
4. **Draft Responses:** Use the AI-driven drafting feature to automatically generate email responses.

## Installation

### Prerequisites
- Python 3.x
- Node.js and npm (for the Angular frontend)

### Backend Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/briefly-ai.git
    cd briefly-ai/backend
    ```
2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Create a `.env` file in the backend directory and add your credentials:
    ```plaintext
    GOOGLE_CLIENT_ID=your-google-client-id
    GOOGLE_CLIENT_SECRET=your-google-client-secret
    GOOGLE_REFRESH_TOKEN=your-google-refresh-token
    SLACK_USER_TOKEN=your-slack-user-token
    SLACK_USER_ID=your-slack-user-id
    ```

5. Run the backend server:
    ```bash
    python app.py
    ```

### Frontend Setup
1. Navigate to the frontend directory:
    ```bash
    cd ../frontend
    ```
2. Install the required packages:
    ```bash
    npm install
    ```
3. Run the Angular development server:
    ```bash
    ng serve
    ```

### Accessing the Application
Open your web browser and navigate to `http://localhost:4200` to access Briefly AI.
