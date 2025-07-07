# FastAPI backend for Money-Fi simulation engine
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import openai
import os

app = FastAPI()

# Allow CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = os.getenv("OPENAI_API_KEY")

class StrategyRequest(BaseModel):
    amount: float
    duration: int
    target: float
    risk: str

@app.post("/llm-strategy")
def get_strategy(request: StrategyRequest):
    prompt = f"""
You are a financial advisor. Based on the following user input, provide three different investment strategies in structured JSON:

User Input:
- Monthly Investment: ₹{request.amount}
- Investment Duration: {request.duration} years
- Target Amount: ₹{request.target}
- Risk Appetite: {request.risk}

Respond in this exact JSON array format:
[
  {{
    "title": "Conservative Plan",
    "summary": "...",
    "expected_return": "...",
    "allocation": [
      {{"type": "Bond", "name": "...", "percentage": 60, "reason": "..."}},
      {{"type": "Mutual Fund", "name": "...", "percentage": 40, "reason": "..."}}
    ],
    "risk_note": "..."
  }},
  {{
    "title": "Balanced Plan",
    "summary": "...",
    "expected_return": "...",
    "allocation": [...],
    "risk_note": "..."
  }},
  {{
    "title": "Aggressive Plan",
    "summary": "...",
    "expected_return": "...",
    "allocation": [...],
    "risk_note": "..."
  }}
]
"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a financial advisor."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return {"strategy": response['choices'][0]['message']['content']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "Money-Fi backend is running"}
