# LinkedIn AI Agent (Hugging Face Version)

## 📌 Overview
This project is an AI Agent that generates LinkedIn posts based on topic classification.

## ⚙️ Workflow
1. User inputs topic
2. Classifier categorizes it (Tech / General)
3. Routed to:
   - Tech Writer OR
   - General Writer
4. Final post is generated

## 🧠 Model Used
- google/flan-t5-base (Hugging Face)

## 🚀 How to Run
```bash
pip install -r requirements.txt
python main.py
