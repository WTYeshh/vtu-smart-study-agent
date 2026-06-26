"""
Study Agent.

Responsible for explaining VTU syllabus topics
using the syllabus PDF reader tool.
"""

from google.adk.agents import Agent
from study_agent.tools.pdf_reader import read_syllabus

study_agent = Agent(
    name="study_agent",
    model="gemini-2.5-flash",
    description="Answers study-related questions using VTU PDFs.",
    instruction="""
You are a VTU Study Agent.

Always use the read_syllabus tool before answering.

Answer clearly and simply.

If the answer is not found in the PDFs,
say that politely.
""",
    tools=[read_syllabus],
)