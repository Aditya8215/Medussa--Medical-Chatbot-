# Medussa - Medical Chatbot

Medussa is an AI-powered **RAG-based chatbot application** designed to assist users with health-related queries, specifically leveraging domain knowledge from books on **pulmonary diseases**. It combines advanced retrieval and reasoning techniques to provide accurate, context-aware, and reliable responses.

## Current Capabilities

* **Domain-Specific Conversational AI**: Trained on pulmonary disease books for precise and trusted responses.
* **Hallucination Control**: Identifies and informs when data is *not* present in the knowledge base.
* **Scalable Architecture**: Deployed on AWS with a robust backend.

## Tech Stack

* **LangChain + RAG** for retrieval-augmented generation
* **Weaviate** as the vector database
* **Gemini 2.5 Pro** as the LLM
* **Flask** for backend
* **AWS** for deployment

## Planned Enhancements

1. Implementation of **Advanced RAG techniques**
2. Expanding to **more datasets and medical topics**
3. Building a **Knowledge Graph** to improve reasoning and relationships
4. Integrating a **Disease Checker Module**

## Getting Started

### Prerequisites

* Python 3.7 or higher
* Required Python libraries (see \[requirements.txt])
* (Optional) API keys for external medical data sources

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Aditya8215/Medussa--Medical-Chatbot-.git
   cd Medussa--Medical-Chatbot-
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**

   ```bash
   python app.py
   ```

---

Medussa is a step forward in **AI for Healthcare**, combining **retrieval-augmented generation, domain-specific knowledge, and scalable deployment**. Contributions and collaborations are welcome! 🚀
