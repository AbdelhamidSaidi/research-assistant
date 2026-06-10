import os
from pathlib import Path
from dotenv import load_dotenv
from crewai import Agent, LLM
from crewai_tools import FileWriterTool

load_dotenv(override=True)

model = os.getenv("WRITER_AGENT_LLM")
temperature = float(os.getenv("WRITER_AGENT_TEMPERATURE"))

llm = LLM(
    model=model,
    temperature=temperature
)

# Ensure reports directory exists
reports_dir = Path(__file__).parent.parent / "reports"
reports_dir.mkdir(exist_ok=True)

content_writer_agent = Agent(
    role="Content Writer",
    goal="Create comprehensive, well-structured reports and summaries to be saved in the reports directory",
    backstory = (
                "You are a professional content writer with expertise in creating "
                "clear, engaging, and well-structured documents. You can transform complex "
                "information into accessible and compelling content."
            ),
    llm=llm,
    tools=[FileWriterTool()],
    verbose=True,
)