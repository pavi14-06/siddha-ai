# 🪔 Siddha AI — Ancient Wisdom, Modern Intelligence

> **சித்த மருத்துவம் × செயற்கை நுண்ணறிவு**
> *5000 years of Tamil healing wisdom, powered by modern machine intelligence.*

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green?style=flat-square&logo=fastapi)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)]()

---

## 👩‍💻 About This Project

Hi, I'm **Pavithra V** — a CS graduate and Data Analyst from Chennai with hands-on experience in Python, ML, and ERP automation. During my internship at **Data Patterns India Ltd**, I built real-time KPI dashboards and automated data pipelines for aerospace/defense systems using Python and SQL. That experience showed me the power of combining structured knowledge with intelligent automation.

This project, **Siddha AI**, applies that same mindset to something deeply rooted in Tamil culture. I built this to digitize and intelligently automate the diagnostic process of **Siddha medicine** — an ancient Tamil healing system that has never had an AI layer built natively for it. Every existing health AI is either Allopathic or Ayurveda-adapted. Siddha deserved its own system.

I designed and built this entirely myself — backend, frontend, knowledge base, and scoring engine — as a solo project.

---

## 🌍 What Makes This a World First

No AI system has ever been built **natively on Siddha medicine**. This project:

- Implements **Envagai Thervu** (Siddha's 8-fold diagnostic framework) in software for the first time
- Maps classical Siddha texts directly into a structured, queryable knowledge base
- Delivers diagnosis output in **Tamil and English** natively
- Is designed to assist real Siddha practitioners — not replace them

---

## 📁 Project Structure

```
siddha-ai/
├── backend/
│   ├── main.py              # FastAPI server + Siddha diagnosis engine
│   └── requirements.txt     # Python dependencies
├── frontend/
│   └── index.html           # Bilingual Tamil-English UI (zero framework)
├── data/
│   └── siddha_kb.json       # Full Siddha knowledge base
└── README.md
```

---

## ⚡ Quick Start

### Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open `http://localhost:8000/docs` — auto Swagger UI is live.

### Frontend

```bash
cd frontend
# Simply open index.html in any browser
# Or serve locally:
python -m http.server 3000
```

---

## 🧠 How I Built the AI Engine

### The Siddha Diagnosis Logic

I studied the **Envagai Thervu** — Siddha's classical 8-fold patient examination — and mapped each parameter into a weighted scoring system:

| Parameter | Tamil | Implemented As |
|-----------|-------|----------------|
| Naadi | நாடி | Dominant Naadi detection via symptom scoring |
| Naa | நா | Tongue color dropdown → dosha weight |
| Vizhi | விழி | Eye sign dropdown → dosha weight |
| Malam | மலம் | Stool symptom inputs |
| Moothiram | மூத்திரம் | Urine symptom inputs |
| Sparism | சீர்மை | Skin symptom inputs |
| Niram | நிரம் | Color/appearance inputs |
| Mozhi | மொழி | Voice/speech symptoms |

### Weighted Scoring Algorithm

```python
score[dosha] += 2   # per matched symptom
score[dosha] += 3   # tongue color match (primary indicator)
score[dosha] += 2   # eye sign match

confidence = score[dominant] / total_score
severity   = "high" if symptoms >= 7 else "medium" if symptoms >= 4 else "low"
```

### The 3 Naadi Types

| Naadi | Tamil | Nature |
|-------|-------|--------|
| Vatham | வாதம் | Air + Space — dry, cold, irregular |
| Pitham | பித்தம் | Fire + Water — hot, sharp, intense |
| Kapham | கபம் | Earth + Water — heavy, slow, stable |

---

## 🔌 API Reference

### `POST /diagnose`

**Request:**
```json
{
  "symptoms": ["joint pain", "dry skin", "constipation"],
  "tongue_color": "pale dry cracked",
  "eye_sign": "dry eyes",
  "age": 28,
  "gender": "female",
  "duration_days": 10
}
```

**Response:**
```json
{
  "naadi": "Vatham",
  "naadi_tamil": "வாதம்",
  "confidence": 0.78,
  "diseases": ["Vatham Noi", "Vali Noi"],
  "medicines": ["Nilavembu Kudineer", "Rasagandhi Mezhugu"],
  "diet_advice": ["Warm foods", "Sesame oil", "Ginger tea"],
  "lifestyle": ["Regular sleep", "Oil massage", "Gentle Yoga"],
  "severity": "medium",
  "refer_doctor": false,
  "explanation": "Based on 3 symptoms analyzed using Siddha Envagai Thervu..."
}
```

### `GET /symptoms/list`
Returns all known symptoms organized by Naadi type.

### `GET /health`
Health check endpoint.

---

## 🏗️ System Architecture

```
┌──────────────────────────────────────────────────────┐
│                  SIDDHA AI SYSTEM                    │
├──────────────┬──────────────────┬───────────────────┤
│    INPUT     │    AI ENGINE     │     OUTPUT        │
│              │                  │                   │
│ • Symptom    │ • Weighted       │ • Naadi Type      │
│   Selection  │   Scoring        │   (Tamil + Eng)   │
│ • Tongue     │   Algorithm      │ • Disease Names   │
│   Color      │                  │ • Siddha Medicines│
│ • Eye Sign   │ • Rule-Based     │ • Diet Advice     │
│ • Duration   │   Siddha Logic   │ • Lifestyle Tips  │
│              │                  │ • Doctor Referral │
│              │ • Confidence     │                   │
│              │   Score          │                   │
└──────────────┴──────────────────┴───────────────────┘
        ↑                                ↓
   FastAPI Backend                 HTML + Vanilla JS
   Python 3.10+                    Tamil-English UI
```

---

## 🗺️ Roadmap

### ✅ v1.0 — Current Build
- [x] Rule-based Siddha diagnosis engine (Envagai Thervu)
- [x] FastAPI REST API with Swagger docs
- [x] Tamil-English bilingual frontend
- [x] Tongue + eye sign weighted analysis
- [x] Severity detection + doctor referral flag
- [x] Full Siddha knowledge base (3 Naadi types, medicines, diet, lifestyle)

### 🔜 v2.0 — Planned
- [ ] Fine-tune IndicBERT on Tamil Siddha classical texts
- [ ] Tongue image CNN classifier (computer vision)
- [ ] Siddha disease knowledge graph using Neo4j
- [ ] React Native mobile app
- [ ] Patient history tracking

### 🚀 v3.0 — Future Vision
- [ ] IoT wearable pulse sensor for Naadi detection
- [ ] Tamil voice input for elderly users
- [ ] Hospital integration dashboard
- [ ] Real-time clinical validation with Siddha doctors

---

## 🚀 Deployment

**Backend → [Render.com](https://render.com)** (free tier)
```
Start command: uvicorn main:app --host 0.0.0.0 --port $PORT
```

**Frontend → [Vercel](https://vercel.com)** (free tier)
```
Point to frontend/ folder → auto-deploy on every push
```

---

## 📜 Classical Texts Referenced

| Text | Used For |
|------|----------|
| Theraiyar Vagadam | Pulse (Naadi) diagnosis methodology |
| Agasthiyar 2000 | Disease classification system |
| Yugi Vaidhya Chinthamani | Symptom-to-medicine mapping |
| Bogar 7000 | Pharmacology and drug formulations |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, FastAPI, Pydantic |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| AI Engine | Rule-based weighted scoring (v1), IndicBERT planned (v2) |
| Knowledge Base | Structured JSON, classical Siddha texts |
| Deployment | Render (backend), Vercel (frontend) |

---

## ⚠️ Disclaimer

This system is for **decision support only**. It is designed to assist Siddha physicians, not replace them. All outputs must be confirmed by a licensed Siddha practitioner. This tool does not constitute medical advice.

---

## 👤 Author

**Pavithra V**  
Data Analyst & Software Engineer | Python · SQL · Power BI · ML  
📧 pavisumi1408@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/pavithra-v-56bb87280)  
🌐 [Portfolio](https://pavithra-v-portfolio.netlify.app)  
💻 [GitHub](https://github.com/pavi14-06)  
📍 Chennai, India

---

*"உடல் நலமே உலக செல்வம்" — Good health is the world's greatest wealth*
