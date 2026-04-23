# 🛡️ The Sentinel Chemist
### AI-Powered Antibiotic Safety & "Safety Bias" Detection

**The Sentinel Chemist** is a pharmacovigilance tool designed to audit antibiotic production and prescriptions for hidden safety risks. It specifically targets "Safety Bias"—risks that are often overlooked in general clinical trials but impact specific patient demographics (Pediatric, Geriatric, Renal Impairment).

## ✨ Key Features
* **Biochemical Interaction Audit:** Cross-references antibiotics with chemical additives using PubChem data.
* **Demographic Bias Detection:** Identifies if a drug combination is uniquely dangerous for underrepresented patient profiles.
* **Patient Zero Simulator:** Generates high-fidelity clinical scenarios to predict adverse outcomes.
* **Scientific Justification:** Provides peer-level technical warnings for biomedical scientists.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **AI Engine:** Google Gemini 2.5 Flash lite
* **Data Retrieval:** PubChem PUG REST API
* **Interface:** Streamlit

## 🚀 Quick Start
1. **Clone the repo:** `git clone https://github.com/your-username/SentinelChemist.git`
2. **Setup Venv:** `python -m venv venv` and `source venv/bin/activate`
3. **Install Deps:** `pip install -r requirements.txt`
4. **Environment:** Create a `.env` file and add your `GEMINI_API_KEY`.
5. **Run:** `streamlit run app.py`

## ⚖️ Disclaimer
This tool is a prototype for research purposes and is not a substitute for professional medical advice or toxicological testing.