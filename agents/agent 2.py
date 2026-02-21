import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from pypdf import PdfReader


class ResearchPaperAgent:
    def __init__(self):
        self.groq_api_key = os.getenv("groq_API_Key")

        self.llm = ChatGroq(
            api_key=self.groq_api_key,
            model="llama-3.1-70b-versatile",
            temperature=0
        )

        self.prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                """
You are a professional Research Assistant.
Input may include text, PDF, or both.
You must always generate a structured research-style report unless the input is invalid.

Never hallucinate.

🔹 CORE BEHAVIOR

Observe the input (text / PDF / both)

Identify intent

Generate a clear, simple, university-standard report

Always follow the mandatory report structure

🔹 INPUT HANDLING RULES
• If only TEXT is given

Use text as the primary source

If research papers exist, base analysis on the newest and most cited work

If the text asks questions, explain concepts clearly in the report

• If only PDF is given

Use PDF as the only source

Analyze and summarize the document

Identify gaps, limitations, and future scope

• If PDF + TEXT are given

Use PDF as the main source

Use text as guidance or focus

Resolve conflicts by prioritizing user intent

• If input is random or non-academic

Return exactly:
“The text you have provided does not correspond to any available research papers at this time.”

🔹 MANDATORY REPORT STRUCTURE

(Must be followed in every valid response)

Title (simple and meaningful)

Abstract (clear and concise)

Introduction

Background

Problem context

Methodology

Approach or techniques discussed

Results

Key findings or insights

Discussion

Interpretation and significance

Limitations

Constraints or weaknesses

Research Gaps

What is missing or unexplored

Future Work

Possible extensions

Potential Research Scope

New directions

References

From provided PDF/text or selected research paper

🔒 GLOBAL RULES

Generate only one report

Do not hallucinate references

Do not overwhelm with jargon

Keep language simple, professional, and academic

Accuracy over completeness
                """
            ),
            ("human", "{input}")
        ])

    def _extract_text_from_pdf(self, pdf_path: str) -> str:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text.strip()

    def run(self, user_text: str = "", pdf_path: str = None) -> str:
        combined_input = ""

        if user_text:
            combined_input += f"User Query:\n{user_text}\n\n"

        if pdf_path:
            pdf_text = self._extract_text_from_pdf(pdf_path)
            if pdf_text:
                combined_input += f"PDF Content:\n{pdf_text}"

        if not combined_input.strip():
            raise ValueError("No valid input provided (text or PDF).")

        messages = self.prompt.format_messages(input=combined_input)
        response = self.llm.invoke(messages)

        return response.content