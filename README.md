# 🧠 System 1 vs. System 2: Intelligent LLM Router

A production-grade LLM Gateway that automatically optimizes for **cost** and **latency** by routing user queries based on intent and complexity.

## 🚀 The Core Concept
Inspired by Daniel Kahneman's "Thinking, Fast and Slow," this router acts as an orchestrator:
- **System 1 (Fast/Cheap):** Simple queries (greetings, basic facts) are routed to **Gemini 3 Flash**.
- **System 2 (Deep/Reasoning):** Complex tasks (coding, logical reasoning) are routed to **Gemini 3.1 Pro**.

## 🛠️ Technical Stack
- **Language:** Python 3.12
- **Framework:** Streamlit (UI)
- **AI SDK:** Google Gen AI Unified SDK (2026 Stable)
- **Environment:** Conda

## 📦 Installation & Setup
1. Clone the repo:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/smart-llm-router.git](https://github.com/YOUR_USERNAME/smart-llm-router.git)

2. Create environment:
   conda create -n router-env python=3.12
   conda activate router-env

3.Install dependencies:

  pip install -r requirements.txt

4. Add your .env file with GEMINI_API_KEY.

🖥️ Usage
Run the dashboard locally:

streamlit run main.py

