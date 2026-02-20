import os
from google import genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the Client
client = genai.Client(api_key=API_KEY)

def get_smart_response(user_prompt):
    """
    The Router Logic: 
    1. Uses Gemini 3 Flash to judge if a prompt is SIMPLE or COMPLEX.
    2. Routes to Flash (System 1) for speed or 3.1 Pro (System 2) for reasoning.
    """
    
    # SYSTEM 1 CHECK (The Judge)
    judge_response = client.models.generate_content(
        model='gemini-3-flash-preview',
        contents=f"Return only 'SIMPLE' or 'COMPLEX'. Classification for: {user_prompt}"
    )
    
    classification = judge_response.text.strip().upper()
    
    # ROUTING DECISION
    if "SIMPLE" in classification:
        model_to_use = 'gemini-3-flash-preview'
        source_name = "Gemini 3 Flash (System 1)"
    else:
        model_to_use = 'gemini-3.1-pro-preview'
        source_name = "Gemini 3.1 Pro (System 2)"

    # FINAL RESPONSE GENERATION
    response = client.models.generate_content(
        model=model_to_use,
        contents=user_prompt
    )
        
    return response.text, source_name