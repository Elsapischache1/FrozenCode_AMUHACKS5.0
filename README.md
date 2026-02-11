# Synapse (FrozenCode_AMUHACKS5.0)

**Synapse** is a personalized learning platform designed to assess skills through interactive quizzes and an AI-powered tutor named **Luna**. Built for **AMUHacks 5.0**, this application leverages generative AI to provide tailored guidance and feedback based on the user's proficiency level.

## 🚀 Features

* **Skill Assessment Quizzes:** Dynamic quizzes that adapt to different skill levels.
* **AI Tutor (Luna):** An integrated chatbot powered by Google's Gemini API that answers questions and clears doubts specific to the user's current level.
* **Real-time Feedback:** Instant scoring and level progression logic.
* **Modern UI:** A clean, responsive React frontend.

## 🛠️ Tech Stack

### Backend
* **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
* **AI Integration:** Google Gemini API (`google-generativeai`)
* **Server:** Uvicorn

### Frontend
* **Library:** [React.js](https://reactjs.org/)
* **Routing:** React Router DOM
* **Styling:** CSS Modules / Standard CSS

---

## ⚙️ Prerequisites

Before you begin, ensure you have the following installed:
* [Python 3.9+](https://www.python.org/downloads/)
* [Node.js](https://nodejs.org/) (v16 or higher) & npm
* A **Google Gemini API Key** (Get one [here](https://aistudio.google.com/app/apikey))

---

## 📦 Installation & Run Instructions

### 1. Backend Setup

The backend is built with FastAPI and handles the AI logic and quiz engine.

**Prerequisites:** Python 3.9+

1.  Navigate to the backend directory:
    ```bash
    cd backend
    ```

2.  Create and activate a virtual environment (recommended):
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    The application requires a Google Gemini API key to function. You can set this as an environment variable or create a `.env` file.
    * **Variable Name:** `GEMINI_API_KEY`

5.  Start the server:
    ```bash
    uvicorn app.main:app --reload
    ```
    The backend API will be available at `http://127.0.0.1:8000`.

### 2. Frontend Setup

The frontend is a React application that serves the user interface.

**Prerequisites:** Node.js & npm

1.  Navigate to the frontend directory:
    ```bash
    cd frontend
    ```

2.  Install the node modules:
    ```bash
    npm install
    ```

3.  Start the development server:
    ```bash
    npm start
    ```
    The application will run at `http://localhost:3000`.

---

## 🔗 API Endpoints

The backend provides RESTful endpoints to manage the quiz flow and AI interaction. You can view the interactive documentation at `http://127.0.0.1:8000/docs` when the server is running.

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | **Health Check.** Verifies that the Synapse Backend is running. |
| `POST` | `/quiz/start` | **Start Quiz.** Initializes a new quiz session for a selected skill (e.g., "Python"). |
| `GET` | `/quiz/question/{level}` | **Get Question.** Fetches the next question for the specified difficulty level (e.g., "Beginner"). |
| `POST` | `/quiz/answer` | **Submit Answer.** Receives the user's selected option, validates it, and updates the score. |
| `GET` | `/quiz/result` | **Get Results.** Retrieves the final score breakdown and determined proficiency level after the quiz ends. |
| `POST` | `/luna/chat` | **Luna AI Chat.** Sends a user message to the AI tutor (Luna) and returns a context-aware response based on the current skill and level. |

---

## 📂 Project Structure

```text
FrozenCode_AMUHACKS5.0/
├── backend/
│   ├── app/
│   │   ├── services/
│   │   │   ├── luna.py         # Gemini AI integration logic
│   │   │   └── quiz_logic.py   # Core quiz engine
│   │   └── main.py             # FastAPI entry point & endpoints
│   ├── prompts/
│   │   └── luna_base.txt       # System prompts for the AI
│   └── requirements.txt        # Backend dependencies
├── frontend/
│   ├── public/                 # Static assets (images, icons)
│   ├── src/
│   │   ├── assets/             # Project images (Luna, Cat avatars)
│   │   ├── components/         # Reusable UI components (e.g., Chatbot)
│   │   ├── pages/              # Main route views (Landing, Quiz, Result)
│   │   ├── styles/             # CSS files for individual pages
│   │   ├── App.js              # Main React component & Routing
│   │   └── index.js            # Entry point
│   └── package.json            # Frontend dependencies & scripts
└── README.md

