# Ninja-Researchers
**📌 Overview**

Researchers spend 40–60% of their time reading and cross‑referencing papers. Existing tools summarize but fail to reason across sources, leaving contradictions unresolved and research gaps unnoticed.

Ninja Researchers is an autonomous agent framework that:

Retrieves academic papers from trusted sources (arXiv, Semantic Scholar, PubMed).

Summarizes key claims.

Detects contradictions and highlights unexplored gaps.

Generates a structured research report with citations.

(Bonus) Includes a Devil’s Advocate sub‑agent to challenge claims for robustness.

**🚀 Features**

Autonomous Retrieval: Smart query refinement and database search.

Summarization Layer: Condenses abstracts into concise claims.

Reasoning Layer: Detects contradictions, assigns confidence scores, identifies gaps.

Report Generation: Produces structured Markdown/PDF reports.

Explainability: Agents can explain papers and highlight research scope.

**⚙️ Tech Stack**

LangChain – Agent orchestration

Python – Core implementation

Streamlit – Web interface

ChromaDB / FAISS – Vector database for semantic search

Sentence Transformers – Embedding models

APIs – arXiv, PubMed, Semantic Scholar

**📂 Project Structure**

Ninja-Researchers/
│── research_companion.py   # Streamlit app
│── agents/                 # Agent definitions
│── utils/                  # Helper functions
│── requirements.txt        # Dependencies
│── README.md               # Documentation
