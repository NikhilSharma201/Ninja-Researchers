import os
import tempfile
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from pypdf import PdfReader
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4


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
Always generate a structured research report.

Follow this structure:
Title
Abstract
Introduction
Methodology
Results
Discussion
Limitations
Research Gaps
Future Work
Potential Research Scope
References

Keep it academic, simple, and professional.
Do not hallucinate.
                """
            ),
            ("human", "{input}")
        ])

    def _extract_text_from_pdf(self, pdf_file) -> str:
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
        return text.strip()

    def _generate_pdf(self, report_text: str, output_path: str):
        styles = getSampleStyleSheet()
        story = []

        for line in report_text.split("\n"):
            if line.strip():
                story.append(Paragraph(line, styles["Normal"]))
            else:
                story.append(Paragraph("<br/>", styles["Normal"]))

        pdf = SimpleDocTemplate(
            output_path,
            pagesize=A4,
            rightMargin=40,
            leftMargin=40,
            topMargin=40,
            bottomMargin=40
        )
        pdf.build(story)

    def run(self, user_text: str = "", uploaded_pdf=None) -> str:
        combined_input = ""

        if user_text:
            combined_input += f"User Text:\n{user_text}\n\n"

        if uploaded_pdf:
            pdf_text = self._extract_text_from_pdf(uploaded_pdf)
            if pdf_text:
                combined_input += f"PDF Content:\n{pdf_text}"

        if not combined_input.strip():
            raise ValueError("No valid input provided.")

        messages = self.prompt.format_messages(input=combined_input)
        response = self.llm.invoke(messages)

        report_text = response.content

        output_pdf = "research_report.pdf"
        self._generate_pdf(report_text, output_pdf)

        return output_pdf