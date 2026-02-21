import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


class ResearchPaperAgent:
    def __init__(self):
        # Load API key
        self.groq_api_key = os.getenv("groq_API_Key")

        # Initialize LLM once (important for performance)
        self.llm = ChatGroq(
            api_key=self.groq_api_key,
            model="llama-3.1-70b-versatile",
            temperature=0
        )

        # System + Human prompt
        self.prompt_template = ChatPromptTemplate.from_messages([
            (
                "system",
                """
You are a Research Paper Finder Agent.

Your task is to analyze user-provided text and determine whether it corresponds
to existing academic research papers.

You must always follow exactly ONE of the two cases below.

CASE 1 — Research Papers Exist:
- Search trusted academic sources only (Google Scholar, Semantic Scholar, IEEE, arXiv, Springer, ACM).
- From all relevant papers:
  1) Select the most recent publication.
  2) If multiple recent papers exist, select the one with the highest citation count.
- Return ONLY ONE research paper.

Output format (STRICT):

Research Paper Title:
<Exact title>

Authors:
<Author 1>, <Author 2>, ...

Publication Year:
<Year>

Journal / Conference:
<Name>

Research Paper Link:
<Direct DOI / arXiv / publisher URL>

Reference Link:
<Google Scholar or Semantic Scholar link>

Reason for Selection:
Selected because it is the most recent publication with the highest citation count among relevant research papers.

CASE 2 — No Research Papers Exist:
If the text is random, non-academic, unclear, or no matching research papers are found,
respond with exactly ONE line:

The text you have provided does not correspond to any available research papers at this time.

Global Rules:
- Do not hallucinate paper titles, authors, or links.
- Do not return multiple papers.
- Do not add explanations outside the specified format.
- If unsure, follow CASE 2.
                """
            ),
            ("human", "{input}")
        ])

    def run(self, user_input: str) -> str:
        # Format messages
        messages = self.prompt.format_messages(input=user_input)

        # Call model
        response = self.llm.invoke(messages)

        # Return clean output
        return response.content