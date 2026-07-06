from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from coach.memory import get_user, update_user
from coach.llm_engine import generate_reply

app = FastAPI(title="Running AI Coach Web Chat")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
def chat(data: dict):
    user_id = data.get("user_id", "default")
    message = data.get("message", "")

    user_state = get_user(user_id)

    if "hr" in data or "fatigue" in data:
        update_user(user_id, data)
        user_state = get_user(user_id)

    reply = generate_reply(user_state, message)

    return {
        "user_state": user_state,
        "reply": reply
    }
