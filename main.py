from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import json

app = FastAPI(title="Siddha AI Diagnosis API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─────────────────────────────────────────────
# SIDDHA KNOWLEDGE BASE (Rule-Based Engine)
# Replace this with ML model in production
# ─────────────────────────────────────────────

SIDDHA_RULES = {
    "vatham": {
        "symptoms": ["joint pain", "dry skin", "constipation", "anxiety", "insomnia",
                     "bloating", "muscle cramps", "cold hands", "irregular digestion", "tremors"],
        "tongue_colors": ["pale", "dry", "cracked"],
        "eye_signs": ["dry eyes", "twitching"],
        "diseases": ["Vatham Noi", "Vali Noi", "Azhal Vali"],
        "medicines": ["Nilavembu Kudineer", "Rasagandhi Mezhugu", "Vatham Kudineer"],
        "diet": ["Warm foods", "Sesame oil", "Ginger tea", "Cooked vegetables"],
        "lifestyle": ["Regular sleep", "Oil massage", "Avoid cold", "Yoga - slow movements"]
    },
    "pitham": {
        "symptoms": ["acidity", "heartburn", "fever", "inflammation", "anger",
                     "excessive sweating", "loose stools", "burning sensation", "redness", "skin rash"],
        "tongue_colors": ["red", "yellow coated", "inflamed"],
        "eye_signs": ["red eyes", "yellow tinge"],
        "diseases": ["Pitham Noi", "Azhal Noi", "Veppam"],
        "medicines": ["Nannari Syrup", "Thaleesapathri Churnam", "Chandanam Thailam"],
        "diet": ["Cool foods", "Coconut water", "Pomegranate", "Coriander water", "Avoid spicy"],
        "lifestyle": ["Avoid sun", "Cool showers", "Meditation", "Early sleep"]
    },
    "kapham": {
        "symptoms": ["cough", "cold", "obesity", "lethargy", "excess sleep",
                     "mucus", "water retention", "slow digestion", "depression", "heaviness"],
        "tongue_colors": ["white coated", "thick coating", "swollen"],
        "eye_signs": ["watery eyes", "puffiness"],
        "diseases": ["Kapham Noi", "Sembal", "Iya Noi"],
        "medicines": ["Thippili Rasayanam", "Sitopaladi Churnam", "Trikadugu Churnam"],
        "diet": ["Light foods", "Honey", "Ginger", "Turmeric milk", "Avoid dairy"],
        "lifestyle": ["Morning exercise", "Dry massage", "Fasting occasionally", "Stay active"]
    }
}

# ─────────────────────────────────────────────
# MODELS
# ─────────────────────────────────────────────

class SymptomInput(BaseModel):
    symptoms: List[str]
    tongue_color: Optional[str] = None
    eye_sign: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    duration_days: Optional[int] = None

class DiagnosisResult(BaseModel):
    naadi: str
    naadi_tamil: str
    confidence: float
    diseases: List[str]
    medicines: List[str]
    diet_advice: List[str]
    lifestyle: List[str]
    severity: str
    refer_doctor: bool
    explanation: str

# ─────────────────────────────────────────────
# DIAGNOSIS ENGINE
# ─────────────────────────────────────────────

def calculate_dosha_scores(symptoms: List[str], tongue_color: str = None, eye_sign: str = None):
    scores = {"vatham": 0, "pitham": 0, "kapham": 0}
    symptom_lower = [s.lower() for s in symptoms]

    for dosha, data in SIDDHA_RULES.items():
        for symptom in symptom_lower:
            for known in data["symptoms"]:
                if known in symptom or symptom in known:
                    scores[dosha] += 2

        if tongue_color:
            for color in data["tongue_colors"]:
                if color in tongue_color.lower():
                    scores[dosha] += 3

        if eye_sign:
            for sign in data["eye_signs"]:
                if sign in eye_sign.lower():
                    scores[dosha] += 2

    return scores

def get_severity(symptom_count: int, duration: int = 1):
    if symptom_count >= 7 or duration > 30:
        return "high"
    elif symptom_count >= 4 or duration > 7:
        return "medium"
    return "low"

# ─────────────────────────────────────────────
# ROUTES
# ─────────────────────────────────────────────

@app.get("/")
def root():
    return {"message": "Siddha AI API is running", "version": "1.0.0"}

@app.post("/diagnose", response_model=DiagnosisResult)
def diagnose(input_data: SymptomInput):
    if not input_data.symptoms:
        raise HTTPException(status_code=400, detail="At least one symptom required")

    scores = calculate_dosha_scores(
        input_data.symptoms,
        input_data.tongue_color,
        input_data.eye_sign
    )

    total = sum(scores.values()) or 1
    dominant = max(scores, key=scores.get)
    confidence = round(scores[dominant] / total, 2)

    tamil_names = {"vatham": "வாதம்", "pitham": "பித்தம்", "kapham": "கபம்"}
    data = SIDDHA_RULES[dominant]
    severity = get_severity(len(input_data.symptoms), input_data.duration_days or 1)

    return DiagnosisResult(
        naadi=dominant.capitalize(),
        naadi_tamil=tamil_names[dominant],
        confidence=confidence,
        diseases=data["diseases"],
        medicines=data["medicines"],
        diet_advice=data["diet"],
        lifestyle=data["lifestyle"],
        severity=severity,
        refer_doctor=severity == "high",
        explanation=f"Based on {len(input_data.symptoms)} symptoms analyzed using Siddha Envagai Thervu principles, "
                    f"your dominant Naadi is {dominant.capitalize()} ({tamil_names[dominant]}) "
                    f"with {int(confidence*100)}% confidence."
    )

@app.get("/symptoms/list")
def get_all_symptoms():
    all_symptoms = {}
    for dosha, data in SIDDHA_RULES.items():
        all_symptoms[dosha] = data["symptoms"]
    return all_symptoms

@app.get("/health")
def health_check():
    return {"status": "healthy"}
