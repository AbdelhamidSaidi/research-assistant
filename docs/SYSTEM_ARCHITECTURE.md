# System Architecture - Complete Linked System

## 🏗️ Complete Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        ENTRY POINT                                      │
│                       main.py                                           │
│  (CLI input handling + report file management)                          │
│  📖 See: README.md, QUICK_REFERENCE.md                                  │
└──────────────────────┬──────────────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    CREW ORCHESTRATOR                                    │
│                      crew.py                                            │
│  (Coordinates three-agent research system)                              │
│  📖 See: PROFESSIONAL_RESEARCH_CONFIG.md                                │
└──────────────────────┬──────────────────────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼

┌──────────────────┐ ┌────────────────────┐ ┌─────────────────┐
│  AGENT 1         │ │  AGENT 2           │ │  AGENT 3        │
│                  │ │                    │ │                 │
│ Research         │ │ Data               │ │ Content         │
│ Specialist       │ │ Analyst            │ │ Writer          │
│                  │ │                    │ │                 │
│ File:            │ │ File:              │ │ File:           │
│ agents/research_ │ │ agents/data_       │ │ agents/content_ │
│ specialist.py    │ │ analyst.py         │ │ writer.py       │
└────────┬─────────┘ └────────┬───────────┘ └────────┬────────┘
         │                    │                     │
         ▼                    ▼                     ▼

┌──────────────────┐ ┌────────────────────┐ ┌─────────────────┐
│  TASK 1          │ │  TASK 2            │ │  TASK 3         │
│                  │ │                    │ │                 │
│ Research Task    │ │ Analysis Task      │ │ Writing Task    │
│                  │ │                    │ │                 │
│ • Web search     │ │ • Cross-verify     │ │ • Professional  │
│   via Serper     │ │   sources          │ │   formatting    │
│ • Track URLs     │ │ • Identify         │ │ • Complete      │
│ • Multiple       │ │   patterns         │ │   citations     │
│   searches       │ │ • Preserve URLs    │ │ • Bibliography  │
│                  │ │ • Analyze data     │ │                 │
│ File:            │ │                    │ │ File:           │
│ tasks/research_  │ │ File:              │ │ tasks/writing_  │
│ task.py          │ │ tasks/analysis_    │ │ task.py         │
│                  │ │ task.py            │ │                 │
└────────┬─────────┘ └────────┬───────────┘ └────────┬────────┘
         │                    │                     │
         ▼                    ▼                     ▼

        TASK 1              TASK 2              TASK 3
     (Search)           (Analyze)            (Write)
        │                   │                    │
        └───────────────────┴────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                  OUTPUT REPORT                              │
│            /reports/report_[topic]_[timestamp].md           │
│                                                              │
│  ✓ Executive Summary                                         │
│  ✓ Key Findings with URLs                                   │
│  ✓ Statistics & Data (cited)                               │
│  ✓ Expert Perspectives                                      │
│  ✓ Recent Developments                                      │
│  ✓ Analysis & Insights                                      │
│  ✓ Conclusions & Recommendations                            │
│  ✓ Complete Sources & References                            │
└─────────────────────────────────────────────────────────────┘
```

## 📊 Data Flow Diagram

```
USER INPUT
    │
    │ "Cloud Computing"
    │
    ▼
┌──────────────────────┐
│  main.py             │
│  • Parse arguments   │
│  • Initialize        │
│  • Handle file I/O   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────────────────┐
│  crew.py                         │
│  • Orchestrate agents            │
│  • Manage task flow              │
│  • Aggregate results             │
└──────────┬───────────────────────┘
           │
    ┌──────┴──────┬──────────┐
    │             │          │
    ▼             ▼          ▼
 TASK 1       TASK 2     TASK 3
 RESEARCH    ANALYZE    WRITE

┌─────────────────────────────────────┐
│ Task 1: Research                    │
│                                     │
│ Input: {topic: "Cloud Computing"}   │
│                                     │
│ Searches:                           │
│ 1. "Cloud Computing"                │
│ 2. "Cloud Computing statistics"     │
│ 3. "Cloud Computing expert"         │
│ 4. "Cloud Computing 2024"           │
│ 5. "Cloud Computing key facts"      │
│                                     │
│ Output: Research findings with:     │
│ - Findings                          │
│ - Source websites                   │
│ - URLs                              │
│ - Statistics                        │
│ - Expert opinions                   │
└──────────┬────────────────────────┘
           │
           ▼
┌─────────────────────────────────────┐
│ Task 2: Analyze                     │
│                                     │
│ Input: Research findings + URLs     │
│                                     │
│ Operations:                         │
│ - Cross-verify sources              │
│ - Identify patterns                 │
│ - Verify reliability                │
│ - Extract insights                  │
│ - Preserve URLs                     │
│                                     │
│ Output: Analyzed findings with:     │
│ - Key insights                      │
│ - Trends                            │
│ - Verified sources                  │
│ - Source URLs preserved             │
└──────────┬────────────────────────┘
           │
           ▼
┌─────────────────────────────────────┐
│ Task 3: Write Report                │
│                                     │
│ Input: Analysis + URLs              │
│                                     │
│ Formatting:                         │
│ - Executive Summary                 │
│ - Key Findings (+ URLs)             │
│ - Statistics (+ citations)          │
│ - Expert Perspectives               │
│ - Recent Developments               │
│ - Analysis                          │
│ - Conclusions                       │
│ - Bibliography                      │
│                                     │
│ Output: Professional Report         │
└──────────┬────────────────────────┘
           │
           ▼
┌─────────────────────────────────────┐
│ File Management (main.py)           │
│                                     │
│ - Create /reports/ directory        │
│ - Generate filename with timestamp  │
│ - Save report as .md file           │
│ - Display success message           │
│                                     │
│ Output Location:                    │
│ reports/report_Cloud_Computing_     │
│ 20260610_190640.md                  │
└─────────────────────────────────────┘
```

## 🔗 File Linking Overview

### Entry Point Links
```
main.py
├── imports: crew.py
├── imports: research_crew
├── references: README.md (in docstring)
├── references: QUICK_REFERENCE.md
└── references: PROFESSIONAL_RESEARCH_CONFIG.md
```

### Crew Orchestration Links
```
crew.py
├── imports: agents/research_specialist.py
├── imports: agents/data_analyst.py
├── imports: agents/content_writer.py
├── imports: tasks/research_task.py
├── imports: tasks/analysis_task.py
├── imports: tasks/writing_task.py
├── creates: research_crew (Crew object)
└── references: System Architecture (in docstring)
```

### Agent Links
```
agents/research_specialist.py
├── imports: SerperDevTool
├── uses: Groq LLM (llama-3.3-70b-versatile)
└── performs: research_task

agents/data_analyst.py
├── uses: Groq LLM
└── performs: analysis_task

agents/content_writer.py
├── imports: FileWriterTool
├── uses: Groq LLM
└── performs: writing_task
```

### Task Links
```
tasks/research_task.py
├── agent: research_specialist_agent
├── API: Serper (web search)
└── output: research_findings.md

tasks/analysis_task.py
├── agent: data_analyst_agent
├── input: research_task (context)
└── output: analysis_report.md

tasks/writing_task.py
├── agent: content_writer_agent
├── inputs: research_task + analysis_task (context)
└── output: final_report.md → /reports/
```

### External APIs
```
APIs Used:
├── Groq API
│   └── Model: llama-3.3-70b-versatile
│   └── Configured in: .env (GROQ_API_KEY)
│
└── Serper API
    └── Web search engine
    └── Configured in: .env (SERPER_API_KEY)
```

## 📋 Complete File Manifest

| File | Type | Purpose | Links To |
|------|------|---------|----------|
| `main.py` | Entry Point | CLI & orchestration | crew.py |
| `crew.py` | Orchestrator | Agent coordination | agents/*, tasks/* |
| `agents/research_specialist.py` | Agent | Web search | tasks/research_task.py |
| `agents/data_analyst.py` | Agent | Analysis | tasks/analysis_task.py |
| `agents/content_writer.py` | Agent | Report writing | tasks/writing_task.py |
| `tasks/research_task.py` | Task | Search strategy | agents/research_specialist.py |
| `tasks/analysis_task.py` | Task | Data analysis | agents/data_analyst.py, tasks/research_task.py |
| `tasks/writing_task.py` | Task | Report format | agents/content_writer.py, tasks/research_task.py, tasks/analysis_task.py |
| `.env` | Config | API keys | All agents |
| `README.md` | Documentation | System overview | All components |
| `QUICK_REFERENCE.md` | Documentation | Quick start | main.py usage |
| `PROFESSIONAL_RESEARCH_CONFIG.md` | Documentation | Configuration | System setup |
| `SYSTEM_ARCHITECTURE.md` | Documentation | This file | Complete system |

## 🔄 Request Processing Flow

```
1. USER COMMAND
   python main.py "Cloud Computing"
        │
        ▼
2. PARSE ARGUMENTS
   • Topic: "Cloud Computing"
   • Save report: True (default)
        │
        ▼
3. LOAD ENV VARIABLES
   • GROQ_API_KEY
   • SERPER_API_KEY
        │
        ▼
4. INITIALIZE CREW
   • Load 3 agents
   • Load 3 tasks
        │
        ▼
5. RUN CREW.KICKOFF()
   • Task 1: Research with Serper
   • Task 2: Analyze findings
   • Task 3: Write professional report
        │
        ▼
6. POST-PROCESS
   • Create /reports/ directory
   • Save report with timestamp
   • Display success message
        │
        ▼
7. OUTPUT
   reports/report_Cloud_Computing_20260610_190640.md
```

## 🎯 Agent Specialization

### Research Specialist
- **Responsibility**: Web search and source discovery
- **Tools**: Serper API
- **Inputs**: Topic name
- **Outputs**: Findings with URLs
- **Metrics**: Number of sources, URL completeness

### Data Analyst
- **Responsibility**: Verification and pattern recognition
- **Tools**: Analysis logic
- **Inputs**: Research findings from specialist
- **Outputs**: Verified insights with sources
- **Metrics**: Source verification rate, pattern identification

### Content Writer
- **Responsibility**: Professional formatting and presentation
- **Tools**: FileWriterTool
- **Inputs**: Research + Analysis
- **Outputs**: Formatted report
- **Metrics**: Format compliance, citation completeness

## 📚 Documentation Linkage

```
README.md (Main Documentation)
├── References: QUICK_REFERENCE.md
├── References: PROFESSIONAL_RESEARCH_CONFIG.md
├── References: SYSTEM_ARCHITECTURE.md
├── Links to: main.py (entry point)
├── Links to: agents/ (component details)
└── Links to: tasks/ (workflow details)

QUICK_REFERENCE.md (Quick Start)
├── Links to: README.md (for more details)
└── Links to: main.py (code examples)

PROFESSIONAL_RESEARCH_CONFIG.md (Configuration)
├── Links to: README.md (for overview)
├── Links to: agents/ (detailed configuration)
└── Links to: .env (API setup)

SYSTEM_ARCHITECTURE.md (Architecture)
├── Links to: All components
└── Shows: Complete system flow
```

## ✅ System Verification Checklist

- ✅ main.py → crew.py (linked via import)
- ✅ crew.py → agents (linked via imports)
- ✅ crew.py → tasks (linked via imports)
- ✅ agents → tasks (linked via agent-task association)
- ✅ tasks → agents (linked via agent-task association)
- ✅ All documentation references components
- ✅ All components have documented purpose
- ✅ API keys configured in .env
- ✅ Report output directory configured (/reports/)
- ✅ Complete workflow documented

---

**System Status**: ✅ FULLY LINKED AND OPERATIONAL

All components are interconnected and documented. The system is ready to generate professional research reports with complete source attribution and URLs.
