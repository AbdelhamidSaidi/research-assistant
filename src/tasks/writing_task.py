import textwrap

from crewai import Task
from agents.content_writer import content_writer_agent
from tasks.analysis_task import analysis_task
from tasks.research_task import research_task


writing_task = Task(
    agent=content_writer_agent,
    description=textwrap.dedent("""
                Create a PROFESSIONAL, publication-quality report on: {topic}

                FORMATTING REQUIREMENTS:
                Use professional business report format:

                1. **TITLE PAGE SECTION**
                   - Title: [Topic] - Professional Research Report
                   - Date: [Current date]
                   - Prepared by: Research Team

                2. **EXECUTIVE SUMMARY** (2-3 paragraphs)
                   - Brief overview of key findings
                   - Main conclusions
                   - Recommendations

                3. **INTRODUCTION**
                   - Background on the topic
                   - Importance and relevance
                   - Report objectives

                4. **KEY FINDINGS** (with sources)
                   Format each finding as:
                   - **[Finding Title]**: [Detailed finding]
                     Source: [Website Name] - [URL]

                5. **STATISTICS & DATA** (with citations)
                   Format as:
                   - **[Statistic Title]**: [Data/Percentage]
                     Source: [Website Name] - [URL]

                6. **EXPERT PERSPECTIVES**
                   - **[Expert Name/Source]**: "[Quote]"
                     Reference: [URL]

                7. **RECENT DEVELOPMENTS**
                   - **[Development Title]**: [Description]
                     Source: [URL]

                8. **ANALYSIS & INSIGHTS**
                   - Implications of findings
                   - Trends and patterns
                   - Professional interpretation

                9. **CONCLUSIONS & RECOMMENDATIONS**
                   - Main conclusions
                   - Actionable recommendations
                   - Future outlook

                10. **SOURCES & REFERENCES**
                    Create a complete bibliography with:
                    - Source Name
                    - URL (clickable/full link)
                    - Access date

                STYLE REQUIREMENTS:
                - Use professional language (no casual terms)
                - Include headers and subheaders for clarity
                - Use bullet points for lists
                - Bold important findings
                - Maintain consistent formatting
                - Ensure every claim has a source citation
                """),
    expected_output="A professional research report with proper formatting, citations, and complete source references for all claims",
    context=[research_task, analysis_task],
    output_file="final_report.md"
    )