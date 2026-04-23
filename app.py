import streamlit as st
from engine import SentinelEngine

# Page Config
st.set_page_config(page_title="Sentinel Chemist", page_icon="💊", layout="wide")
engine = SentinelEngine()

# Custom CSS for a professional look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ The Sentinel Chemist")
st.markdown("### AI-Powered Antibiotic Safety & Bias Detection")

# Sidebar for Inputs
with st.sidebar:
    st.header("🔬 Input Parameters")
    antibiotic = st.text_input("Main Antibiotic", value="Amoxicillin")
    additive = st.text_input("Chemical Additive / Co-drug", value="Allopurinol")
    profile = st.selectbox("Target Patient Profile", 
                          ["Healthy Adult", "Pediatric", "Geriatric", "Renal Impairment", "Pregnancy"])
    
    run_button = st.button("🚀 RUN SAFETY AUDIT")

# Main Display Area
if run_button:
    with st.spinner("Analyzing biochemical pathways and historical data..."):
        try:
            report = engine.generate_audit(antibiotic, additive, profile)
            
            # Displaying Result
            st.success("Audit Complete")
            st.markdown("---")
            st.markdown(report)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
else:
    st.info("👈 Enter the antibiotic and chemical details in the sidebar to begin the audit.")

# Footer
st.markdown("---")
st.caption("Disclaimer: This is an AI prototype for research purposes. Always consult a licensed medical professional or toxicologist.")