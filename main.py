from fastapi import FastAPI

app = FastAPI()

# Rule-based medical logic
def check_seriousness(symptom: str):
    symptom = symptom.lower()

    # Normal / mild issues
    normal_cases = ["mild gum pain", "cold", "sneeze", "headache", "cough", "gum going down"]
    urgent_cases = ["chest pain", "severe bleeding", "difficulty breathing", "fainting"]

    if any(s in symptom for s in urgent_cases):
        return {
            "level": "urgent",
            "message": "This might be serious. You should seek medical help quickly."
        }

    if any(s in symptom for s in normal_cases):
        return {
            "level": "not serious",
            "message": "Seems normal. Try home care first."
        }

    return {
        "level": "monitor",
        "message": "Not sure. Monitor your symptoms. If it gets worse, visit a doctor."
    }

@app.get("/check")
def check(symptom: str):
    return check_seriousness(symptom)
@app.get("/ping")
def ping():
    return {"status": "ok", "message": "Backend is running"}
