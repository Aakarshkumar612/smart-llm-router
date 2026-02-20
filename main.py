import streamlit as st
from app import get_smart_response

# Page configuration
st.set_page_config(page_title="Smart AI Router", page_icon="🧠", layout="centered")

st.title("🧠 System 1 vs. System 2 Router")
st.markdown("""
    This project demonstrates an **Intelligent LLM Gateway**. 
    It classifies incoming prompts and routes them to the most cost-effective model 
    without sacrificing intelligence.
""")
st.info("System 1: Gemini 3 Flash (Fast/Cheap) | System 2: Gemini 3.1 Pro (Deep Reasoning)")

# User Input
user_input = st.text_area("Enter your prompt:", height=150, placeholder="e.g., Write a complex SQL query or just say 'Hello'")

if st.button("Route & Generate"):
    if user_input.strip():
        with st.spinner("Classifying intent and routing..."):
            try:
                answer, model_used = get_smart_response(user_input)
                
                # Visual feedback on routing
                if "Pro" in model_used:
                    st.error(f"🚀 Routed to: {model_used}")
                else:
                    st.success(f"⚡ Routed to: {model_used}")
                
                st.markdown("### Model Response")
                st.write(answer)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt to test the router.")