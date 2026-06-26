"""
Root manager agent for the VTU Smart Study Assistant.

Routes user requests to specialized sub-agents:
- Study Agent
- Quiz Agent
- Planner Agent
"""

import os
from dotenv import load_dotenv

load_dotenv()
print("Loaded API Key:", os.getenv("GOOGLE_API_KEY")[:15], "...")

from google.adk.agents import Agent

from study_agent.sub_agents.study import study_agent
from study_agent.sub_agents.quiz import quiz_agent
from study_agent.sub_agents.planner import planner_agent


root_agent = Agent(
    name="vtu_manager_agent",
    model="gemini-2.5-flash",
    description="Manager Agent for the VTU Smart Study Assistant.",
    instruction="""
You are the Manager Agent.

You never specialize yourself.

Instead:

- Send study questions to the Study Agent.
- Send quiz requests to the Quiz Agent.
- Send planning requests to the Planner Agent.

Choose the correct agent based on the user's request.
""",
    sub_agents=[
        study_agent,
        quiz_agent,
        planner_agent,
    ],
)