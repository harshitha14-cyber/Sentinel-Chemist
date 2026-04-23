import os
import requests  # FIX 1: was missing entirely
import google.generativeai as genai
from google.generativeai.client import configure
from google.generativeai.generative_models import GenerativeModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure the SDK
configure(api_key=api_key)

class SentinelEngine:
    def __init__(self):
        self.model = GenerativeModel(model_name="models/gemini-2.5-flash-lite")

    def get_pubchem_data(self, drug_name):
        """Fetches free chemical metadata from NIH PubChem API."""
        try:
            url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{drug_name}/JSON"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                # FIX 2: Extract only the useful summary fields instead of
                # dumping the entire raw dict as an ugly string
                props = (
                    data.get("PC_Compounds", [{}])[0]
                    .get("props", [])
                )
                summary = {
                    p["urn"]["label"]: p["value"].get("sval") or p["value"].get("fval")
                    for p in props
                    if "label" in p.get("urn", {}) and "value" in p
                }
                return summary if summary else "No structured properties found."
            return "No specific chemical structure found in public records."
        except Exception as e:  # FIX 3: bare `except:` hid all errors
            return f"Data retrieval error: {e}"

    def generate_audit(self, antibiotic, additive, patient_profile):
        # 1. Get raw chemical data
        chem_context = self.get_pubchem_data(antibiotic)

        # FIX 4: Format chem_context cleanly before embedding in the prompt
        chem_context_str = str(chem_context)[:1500]

        # 2. Build the "Sentinel" Prompt
        prompt = f"""
        ACT AS: An Expert Pharmacovigilance AI (The Sentinel Chemist).

        CONTEXT:
        - Antibiotic: {antibiotic}
        - Chemical Additive: {additive}
        - Patient Profile: {patient_profile}
        - Data Context: {chem_context_str}

        TASK: Conduct a safety audit for this production/prescription combination.

        FORMAT YOUR RESPONSE WITH THESE HEADINGS:

        ## 🛡️ SAFETY RISK LEVEL
        [State GREEN, YELLOW, or RED clearly]

        ## 🔬 BIOCHEMICAL ANALYSIS
        [Explain the molecular or metabolic interaction. Why is this specific additive a problem with this antibiotic?]

        ## ⚖️ BIAS & DEMOGRAPHIC ALERT
        [Explain if the risk is higher for the selected Patient Profile. Is this a 'Hidden Flaw' that common tests might miss?]

        ## 🧪 PATIENT ZERO SIMULATION
        [Describe a hypothetical scenario of a patient with {patient_profile} taking this. What symptoms appear in 48 hours?]

        ## ✅ SUGGESTED MITIGATION
        [Provide a safer chemical alternative or a dosage adjustment.]
        """

        # FIX 5: Wrap API call in try/except so errors surface clearly
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Gemini API error: {e}"


# FIX 6: Added a runnable example so you can test immediately
if __name__ == "__main__":
    engine = SentinelEngine()
    result = engine.generate_audit(
        antibiotic="Amoxicillin",
        additive="Tartrazine (Yellow Dye No. 5)",
        patient_profile="Adult with G6PD deficiency"
    )
    print(result)