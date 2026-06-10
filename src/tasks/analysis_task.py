import textwrap

from crewai import Task
from agents.data_analyst import data_analyst_agent
from tasks.research_task import research_task


analysis_task = Task(
    agent=data_analyst_agent,
    description=textwrap.dedent("""
                Analyze the research findings for: {topic}

                IMPORTANT: Preserve all source information as you analyze

                Your analysis tasks:
                1. Review all research findings and their sources from the previous task
                2. Identify patterns, trends, and key insights
                3. Cross-reference findings across multiple sources for verification
                4. Analyze the implications and significance
                5. Provide expert interpretation of the data
                6. Highlight the most important conclusions

                WHEN PRESENTING FINDINGS:
                - Always include the source URL with each finding
                - Format: **Finding**: [Description] (Source: [URL])
                - Note which findings appear across multiple sources (indicates reliability)
                - Flag any conflicting information from different sources

                Your analysis should include:
                1. **Key Insights & Patterns** (with source URLs)
                   - What patterns emerge across multiple sources?
                   - What are the most important findings?

                2. **Trend Analysis** (with source URLs)
                   - What trends are evident?
                   - Are these trends supported by multiple sources?

                3. **Verification Notes**
                   - Which findings appear in multiple sources?
                   - Any conflicting information?

                4. **Implications & Significance** (with source URLs)
                   - What does this mean?
                   - Who is affected?

                5. **Expert Interpretation**
                   - Professional analysis of what this means

                6. **Actionable Conclusions**
                   - Key takeaways
                   - Recommendations based on findings

                CRITICAL: Every claim must retain its source URL
                """),
    expected_output="A detailed analysis report with insights, patterns, conclusions, and all source URLs preserved",
    context=[research_task],
    output_file="analysis_report.md"
    )