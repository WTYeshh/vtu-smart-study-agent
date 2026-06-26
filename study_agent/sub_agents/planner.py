"""
Planner Agent.

Creates personalized study schedules and revision
plans based on the student's available time.
"""

from google.adk.agents import Agent
from study_agent.tools.pdf_reader import read_syllabus

planner_agent = Agent(
    name="planner_agent",
    model="gemini-2.5-flash",
    description="Creates VTU study plans.",
    instruction="""
You are a VTU Study Planner.

Always use the read_syllabus tool first.

Create realistic study plans based on the syllabus.

Distribute topics across the available days.

Include revision on the last day whenever possible.
""",
    tools=[read_syllabus],
)