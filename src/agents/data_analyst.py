import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from crewai_tools import FileReadTool

load_dotenv(override=True)

model = os.getenv("ANALYST_AGENT_LLM")
temperature = float(os.getenv("ANALYST_AGENT_TEMPERATURE"))

llm = LLM(
    model=model,
    temperature=temperature
)

data_analyst_agent = Agent(
    role="Data Analyst",
    goal="Analyze gathered information to extract key insights, patterns, and conclusions",
    backstory = (
                "You are a skilled data analyst with expertise in synthesizing complex "
                "information into actionable insights. You excel at identifying patterns, trends, "
                "and key findings from research data."
            ),
    llm=llm,
    tools=[FileReadTool()],
    verbose=True,
)