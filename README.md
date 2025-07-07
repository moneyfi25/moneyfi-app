# moneyfi-app
# 💸 Money-Fi: Gamified Financial Education App

**Money-Fi** is a full-stack educational platform that teaches users how to invest through:
- 🧠 Interactive Quizzes
- 🧪 Simulations
- 📊 AI-Generated Investment Strategies
- 🏆 Leaderboards
- 🧩 Multilingual Support

---

## 🚀 Tech Stack

| Layer      | Technology       |
|------------|------------------|
| Frontend   | React, TailwindCSS |
| Backend    | FastAPI, OpenAI GPT-4 |
| Database   | Firebase (optional), Local Storage (MVP) |
| Hosting    | Vercel (frontend), Render (backend) |

---

## 📦 Folder Structure

moneyfi-app/
├── backend/ # FastAPI server with GPT strategy endpoint
├── frontend/ # React app (UI, quiz, simulator)
├── .gitignore
├── README.md


---

## ⚙️ How to Run Locally

### 🔹 Backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
Then go to: http://localhost:8000

###🔹 Frontend (React)
cd frontend
npm install
npm start
🔐 Environment Variables
Create a .env file in the backend/ directory:
OPENAI_API_KEY=your-openai-api-key
🧪 Features
🎯 Goal-Based Onboarding

📘 Beginner to Advanced Learning Modules

📊 Portfolio Builder + Simulation Engine

🤖 GPT-4 Strategy Generator (/llm-strategy endpoint)

🎮 Market Scenario Games

🧠 Quiz-Based Learning with XP System

🏆 Leaderboard for Gamification

🌍 Multilingual UX (planned)

🌐 Deployment
Frontend → Vercel
Connect frontend/ folder to GitHub

Deploy via Vercel dashboard

Backend → Render
Deploy backend/ with uvicorn main:app --host 0.0.0.0 --port 8000

Add OPENAI_API_KEY to environment variables in Render dashboard

🙌 Contribution
This project is open to contributions.
Feel free to fork, suggest features, and create pull requests.
📧 Contact
Built by Moneyfiai for global financial literacy.
Reach out via gmail **moneyfiai25@gmail.com** 
