from coach.memory import user_memory


def compute_summary(user_id="default"):
    """
    简单训练数据分析（MVP版）
    """
    user = user_memory.get(user_id, {})

    hr = user.get("hr", 150)
    fatigue = user.get("fatigue", 0.3)
    goal = user.get("goal", "10K")

    # mock metrics (can be replaced by Strava/Garmin later)
    weekly_load = 40 + (hr - 140) * 0.2

    return {
        "user": user_id,
        "heart_rate": hr,
        "fatigue": fatigue,
        "goal": goal,
        "weekly_load_estimate": round(weekly_load, 2),
        "recommendation": (
            "增加恢复跑" if fatigue > 0.7 else "保持当前训练节奏"
        ),
        "status": "optimal" if fatigue < 0.6 else "fatigued"
    }