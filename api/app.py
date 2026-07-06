from fastapi import FastAPI

app = FastAPI(title="Running AI Coach")

@app.post("/coach")
def coach(data: dict):
    hr = data.get("hr")
    pace = data.get("pace")
    fatigue = data.get("fatigue", 0.3)

    # simple rule engine
    if fatigue > 0.8:
        rec = {
            "type": "Recovery Run",
            "zone": "Z1-Z2",
            "instruction": "必须恢复，轻松慢跑20-40分钟"
        }
    elif hr < 140:
        rec = {
            "type": "Easy Run",
            "zone": "Z2",
            "instruction": "有氧基础训练 30-60分钟"
        }
    elif hr < 165:
        rec = {
            "type": "Tempo Run",
            "zone": "Z3-Z4",
            "instruction": "节奏跑，提高乳酸阈"
        }
    else:
        rec = {
            "type": "Interval",
            "zone": "Z4-Z5",
            "instruction": "高强度间歇训练"
        }

    return {
        "input": data,
        "recommendation": rec
    }