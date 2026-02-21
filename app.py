import os
import streamlit as st
import tempfile

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from pypdf import PdfReader

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4


# ---------------------------
# Agent 1: Research Paper Finder (TEXT ONLY)
# ---------------------------
class ResearchPaperFinderAgent:
    def __init__(self):
        self.llm = ChatGroq(
            api_key=st.secrets["GROQ_API_KEY"],
            model="llama-3.1-8b-instant",
            temperature=0
        )

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """
You are a Research Paper Finder Agent.

CASE 1 — Research Papers Exist:
- Select the most recent paper.
- If multiple, choose highest citation count.
- Return ONLY ONE paper.

STRICT FORMAT:

Research Paper Title:
Authors:
Publication Year:
Journal / Conference:
Research Paper Link:
Reference Link:
Reason for Selection:

CASE 2 — No Research Papers Exist:
Return exactly:
The text you have provided does not correspond to any available research papers at this time.

Rules:
- Do not hallucinate
- Do not add extra text
- If unsure → CASE 2
            """),
            ("human", "{input}")
        ])

    def run(self, text: str) -> str:
        messages = self.prompt.format_messages(input=text)
        response = self.llm.invoke(messages)
        return response.content


# ---------------------------
# Agent 2: Research Report Generator (TEXT + PDF)
# ---------------------------
class ResearchReportAgent:
    def __init__(self):
        self.llm = ChatGroq(
            api_key=st.secrets["GROQ_API_KEY"],
            model="llama-3.1-8b-instant",
            temperature=0
        )

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """
You are a professional Research Assistant.

Input may include TEXT, PDF, or both.
Always generate a structured academic report.

MANDATORY STRUCTURE:
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

Rules:
- No hallucination
- Simple, professional language
- One report only
            """),
            ("human", "{input}")
        ])

    def extract_pdf_text(self, uploaded_pdf) -> str:
        reader = PdfReader(uploaded_pdf)
        text = ""
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
        return text.strip()

    def generate_pdf(self, report_text: str) -> str:
        styles = getSampleStyleSheet()
        story = []

        for line in report_text.split("\n"):
            story.append(Paragraph(line if line.strip() else "<br/>", styles["Normal"]))

        tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        pdf = SimpleDocTemplate(
            tmp_file.name,
            pagesize=A4,
            rightMargin=40,
            leftMargin=40,
            topMargin=40,
            bottomMargin=40
        )
        pdf.build(story)
        return tmp_file.name

    def run(self, user_text="", uploaded_pdf=None) -> str:
        combined_input = ""

        if user_text:
            combined_input += f"User Text:\n{user_text}\n\n"

        if uploaded_pdf:
            pdf_text = self.extract_pdf_text(uploaded_pdf)
            combined_input += f"PDF Content:\n{pdf_text}"

        if not combined_input.strip():
            raise ValueError("No valid input provided")

        messages = self.prompt.format_messages(input=combined_input)
        response = self.llm.invoke(messages)

        return self.generate_pdf(response.content)


## -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Research Assistant",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Custom CSS (Neutral Academic Theme)
# -----------------------------
st.markdown(
    """
    <style>
        /* App background */
        .stApp {
            background-color: #f7f3ea;
            color: #000000  ;
            font-family: "Segoe UI", sans-serif;
        }

        /* Sidebar styling */
        section[data-testid="stSidebar"] {
            background-color: #efe8d8;
            padding: 2rem 1.5rem;
        }

        section[data-testid="stSidebar"] * {
            color: #2f2f2f !important;
        }

        /* Headings */
        h1, h2, h3 {
            color: #000000;
            
        }

        /* Text area & input */
        textarea, input[type="text"] {
            background-color: #fffdf8 !important;
            color: #000000 !important;
            border: 1px solid #c5c1b6 !important;
            border-radius: 8px !important;
        }

        /* File uploader */
        div[data-testid="stFileUploader"] {
            background-color: #fffdf8;
            color: #000000;
            border-radius: 8px;
            padding: 0.75rem;
            border: 1px dashed #b7b2a3;
        }

        /* Buttons */
        .stButton > button {
            background-color: #6b705c;
            color: #000000;
            
            border-radius: 8px;
            padding: 0.6rem 1.5rem;
            font-weight: 500;
            border: none;
        }

        .stButton > button:hover {
            background-color: #5a5f4b;
        }

        /* Result box */
        .result-box {
            background-color: #ffffff;
            color: #000000;
            padding: 1.2rem;
            border-radius: 10px;
            border-left: 4px solid #6b705c;
            margin-top: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.markdown("## Research Assistant")
    st.markdown(
        """
        An AI-powered academic assistant designed to support university-level
        research workflows.

        **Capabilities**
        - Identify relevant research papers
        - Generate structured academic reports
        """
    )

    st.markdown("### Select Function")
    mode = st.radio(
        "",
        ["Research Paper Finder", "Research Report Generator"],
        key="mode_selector"
    )

    st.markdown("---")
    st.caption("Designed for academic, examination, and research use.")

# -----------------------------
# Main Content
# -----------------------------
if mode == "Research Paper Finder":
    st.markdown("## Research Paper Finder")
    st.markdown(
        "Enter a research topic or academic statement. "
        "Optionally, upload a PDF to provide additional context."
    )

    user_text = st.text_area(
        "Research topic or statement",
        height=220,
        key="finder_text"
    )

    uploaded_pdf = st.file_uploader(
        "Upload reference PDF (optional)",
        type=["pdf"],
        key="finder_pdf"
    )

    if st.button("Find Research Paper", key="finder_button"):
        if not user_text.strip() and not uploaded_pdf:
            st.warning("Please provide text input or upload a PDF.")
        else:
            if st.button("Find Research Paper", key="finder_button"):
    if not user_text.strip() and not uploaded_pdf:
        st.warning("Please provide text input or upload a PDF.")
    else:
        try:
            result = finder_agent.run(user_text)
            st.markdown(
                f"""
                <div class="result-box">
                    <strong>Result</strong><br><br>
                    {result}
                </div>
                """,
                unsafe_allow_html=True
            )
        except Exception as e:
            st.error(f"Error: {e}")


            st.markdown(
                f"""
                <div class="result-box">
                    <strong>Result</strong><br><br>
                    {result}
                </div>
                """,
                unsafe_allow_html=True
            )

# -----------------------------
# Research Report Generator
# -----------------------------
else:
    st.markdown("## Research Report Generator")
    st.markdown(
        "Provide a topic or upload a research paper PDF. "
        "The system will generate a structured academic report."
    )

    user_text = st.text_area(
        "Research topic (optional)",
        height=200,
        key="report_text"
    )

    uploaded_pdf = st.file_uploader(
        "Upload research paper PDF",
        type=["pdf"],
        key="report_pdf"
    )

    if st.button("Generate Research Report", key="report_button"):
        if not user_text.strip() and not uploaded_pdf:
            st.warning("Please provide a topic or upload a PDF.")
        else:
            if st.button("Generate Research Report", key="report_button"):
    if not user_text.strip() and not uploaded_pdf:
        st.warning("Please provide a topic or upload a PDF.")
    else:
        try:
            pdf_path = report_agent.run(user_text, uploaded_pdf)
            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="Download Research Report (PDF)",
                    data=f,
                    file_name="research_report.pdf",
                    mime="application/pdf",
                    key="download_report"
                )
        except Exception as e:
            st.error(f"Error: {e}")


            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="Download Research Report (PDF)",
                    data=f,
                    file_name="research_report.pdf",
                    mime="application/pdf",
                    key="download_report"
                )
# Initialize agents
finder_agent = ResearchPaperFinderAgent()
report_agent = ResearchReportAgent()



        st.error(str(e))
