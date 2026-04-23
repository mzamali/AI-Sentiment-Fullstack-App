from fastapi import FastAPI
from database import get_db_connection
from textblob import TextBlob
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/analyze")
def analyze_text(text: str):
    blob = TextBlob(text)
    score = blob.sentiment.polarity
    mood = 'Positive' if score > 0 else 'Negative' if score < 0 else 'Neutral'

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO sentiment_results (user_text, mood, score) VALUES (%s, %s, %s)"
        cursor.execute(query, (text, mood, score))
        cursor.close()
        conn.close()
        db_status = "Saved to ai_sentiment_db"
    else:
        db_status = "Database Connection Failed"

    return {
        "text": text,
        "mood": mood,
        "score": score,
        "db_status": db_status
    }