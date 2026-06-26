"""
Quiz Agent.

Generates multiple-choice questions and evaluates
student knowledge based on the syllabus.
"""

from google.adk.agents import Agent
from study_agent.tools.pdf_reader import read_syllabus

quiz_agent = Agent(
    name="quiz_agent",
    model="gemini-2.5-flash",
    description="Creates quizzes for VTU students.",
    instruction="""
You are a VTU Quiz Agent.

Always use the read_syllabus tool before creating questions.

Generate MCQs, short questions, or practice tests only from the syllabus PDFs.

Do not invent topics that are not in the PDFs.
""",
    tools=[read_syllabus],
)