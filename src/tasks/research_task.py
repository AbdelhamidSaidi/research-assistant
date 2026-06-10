import textwrap

from crewai import Task
from agents.research_specialist import research_specialist_agent


research_task = Task(
    agent=research_specialist_agent,
    description=textwrap.dedent("""
                Conduct professional, comprehensive research on: {topic}

                CRITICAL REQUIREMENTS - SOURCE TRACKING:
                1. Use the search tool to find information from multiple trusted sources
                2. For EACH piece of information found, record:
                   - The finding/statistic
                   - The source website name
                   - The full URL where it was found
                3. Search multiple times with different keywords to find diverse perspectives
                4. Prioritize authoritative sources (government, academic, established publications)
                5. Include recent information and current developments

                SEARCH STRATEGY:
                Search for:
                1. "{topic}" (general overview)
                2. "{topic} statistics" (data and numbers)
                3. "{topic} expert" or "{topic} research" (expert opinions)
                4. "{topic} 2024" or "{topic} recent" (current developments)
                5. "{topic} key facts" (important information)

                FORMATTING YOUR FINDINGS:
                For every finding, use this format EXACTLY:

                **[Finding Title]**: [Description of finding]
                - Source: [Website Name]
                - URL: [Complete URL with https://]

                Examples:
                **Market Growth**: The global market is growing at 23% annually
                - Source: McKinsey & Company
                - URL: https://www.mckinsey.com/...

                **Expert Opinion**: "This field is revolutionizing..." - Dr. Jane Smith
                - Source: Harvard Business Review
                - URL: https://www.hbr.org/...

                CRITICAL INSTRUCTION:
                ⚠️ DO NOT make up URLs or sources
                ⚠️ ONLY report what you actually find in your searches
                ⚠️ Include the FULL URL for every source
                ⚠️ If a source doesn't have a URL, do not include it
                """),
    expected_output="Professional research summary with key findings, statistics, expert opinions, and recent developments. EACH finding must include the source website name and complete URL.",
    output_file="research_findings.md"
    )