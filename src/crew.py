from crewai import Crew

from agents.research_specialist import research_specialist_agent
from agents.data_analyst import data_analyst_agent
from agents.content_writer import content_writer_agent
from tasks.research_task import research_task
from tasks.analysis_task import analysis_task
from tasks.writing_task import writing_task


# Orchestrate three-agent research system
research_crew = Crew(
    agents=[
        research_specialist_agent,      # Step 1: Research
        data_analyst_agent,             # Step 2: Analyze
        content_writer_agent,           # Step 3: Write Report
    ],
    tasks=[
        research_task,                  # Find sources, track URLs
        analysis_task,                  # Verify, cross-reference
        writing_task,                   # Format professionally, cite sources
    ],
    verbose=True
)