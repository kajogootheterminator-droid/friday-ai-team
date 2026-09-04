from fastapi import FastAPI

app = FastAPI(title="FRIDAY AI Team")

@app.get("/")
def home():
    return {
        "system": "FRIDAY AI Team",
        "status": "online",
        "agents": [
            "JARVIS",
            "ULTRON",
            "FRIDAY",
            "KAREN",
            "EDITH"
        ]
    }
