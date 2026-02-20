# 🧠 System 1 vs. System 2: Intelligent LLM Router

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://smart-llm-router-mubgpbzoznrghlfrw4rfjs.streamlit.app/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/Aakarshkumar612/smart-llm-router)

---

## 🔗 Project Links
* **Live Application:** [Smart LLM Router Demo](https://smart-llm-router-mubgpbzoznrghlfrw4rfjs.streamlit.app/)
* **Source Code:** [GitHub Repository](https://github.com/Aakarshkumar612/smart-llm-router)

---

## 🚀 The Core Concept
This project is inspired by the cognitive psychology framework of **Thinking, Fast and Slow**. In modern AI production, costs and latency are major bottlenecks. This **Intelligent Router** acts as a traffic controller to optimize these variables:

* **System 1 (Fast/Efficient):** Simple queries like greetings, basic facts, or routine formatting are automatically routed to **Gemini 3 Flash**.
* **System 2 (Deep Reasoning):** Complex tasks requiring logical deduction, multi-step coding, or nuanced analysis are routed to **Gemini 3.1 Pro**.

### Key Benefits
* **Cost Optimization:** Reduces API spend by preventing "overkill" (using a Pro model for a Simple task).
* **Latency Reduction:** Improves user experience by delivering instant responses for simple interactions.
* **Intelligence Maintenance:** Ensures that high-complexity requests always receive the depth of a reasoning model.

---

## 🛠️ Technical Stack
* **Core Logic:** Python 3.12
* **Frontend UI:** Streamlit
* **LLM Orchestration:** Google Gen AI Unified SDK (2026 Stable)
* **Environment Management:** Conda

---

## 📦 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Aakarshkumar612/smart-llm-router.git](https://github.com/Aakarshkumar612/smart-llm-router.git)
    cd smart-llm-router
    ```

2.  **Initialize the environment:**
    ```bash
    conda create -n router-env python=3.12
    conda activate router-env
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the root directory:
    ```text
    GEMINI_API_KEY=your_actual_api_key_here
    ```

---

## 🖥️ Local Usage
To launch the interactive dashboard on your local machine, run:
```bash
streamlit run main.py

📄 License
Distributed under the MIT License. See LICENSE for more information.

👤 Contact
Aakarsh Kumar : https://github.com/Aakarshkumar612