import os

# Optional OpenAI LLM integration
# If no API key, fallback to rule-based coach

def generate_reply(user_state: dict, message: str):
    api_key = os.getenv("OPENAI_API_KEY")

    hr = user_state.get("hr", 150)
    fatigue = user_state.get("fatigue", 0.3)

    # fallback mode (no LLM)
    if not api_key:
        if "能跑" in message or "今天跑不跑" in message:
            if fatigue > 0.8:
                return "今天建议恢复跑或休息，疲劳偏高。"
            if hr < 140:
                return "可以轻松跑（Z2），30-60分钟。"
            return "可以跑，但控制在节奏以下。"
        return "（无LLM模式）告诉我你的心率/配速/目标，我帮你制定训练。"

    # LLM mode
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)

        prompt = f"""
你是专业跑步教练AI。
用户状态：心率{hr}，疲劳{fatigue}
用户问题：{message}
请给出训练建议（简洁专业）。
"""

        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "你是跑步训练专家"},
                {"role": "user", "content": prompt}
            ]
        )

        return resp.choices[0].message.content

    except Exception as e:
        return f"LLM调用失败，已切换基础模式：{str(e)}"