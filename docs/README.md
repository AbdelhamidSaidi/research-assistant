# Research Assistant - Professional Research Engine

A sophisticated multi-agent research system that conducts web searches, analyzes findings, and generates professional reports with complete source attribution and URLs.

## 🎯 Quick Start

```bash
# Generate professional research report
python main.py "Your Topic"

# Interactive mode (type topic when prompted)
python main.py

# Without saving to file
python main.py "Topic" --no-save

# Show help
python main.py --help
```

## 📊 What This Does

This research assistant generates **professional, publication-quality reports** with:
- ✅ Web searches from trusted sources (Serper API)
- ✅ Multiple targeted searches per topic
- ✅ Complete source URLs for every finding
- ✅ Professional business report formatting
- ✅ Executive summaries
- ✅ Statistics with proper citations
- ✅ Expert opinions with attribution
- ✅ Recent developments with source links
- ✅ Complete bibliography

## 📁 Project Structure

```
my-research-assistant/
├── main.py                           ← Entry point (use this to run)
├── crew.py                           ← Orchestrates all agents
│
├── agents/                           ← AI Agents
│   ├── research_specialist.py        ← Web search agent (Serper)
│   ├── data_analyst.py               ← Analysis agent
│   └── content_writer.py             ← Report writing agent
│
├── tasks/                            ← Task definitions
│   ├── research_task.py              ← Search strategy & source tracking
│   ├── analysis_task.py              ← Data analysis with source preservation
│   └── writing_task.py               ← Professional report formatting
│
├── reports/                          ← Generated reports saved here
│   └── report_[topic]_[timestamp].md
│
├── .env                              ← API Keys (Groq, Serper)
│
├── README.md                         ← This file
├── QUICK_REFERENCE.md                ← Quick usage guide
└── PROFESSIONAL_RESEARCH_CONFIG.md   ← Detailed configuration
```

## 🤖 Agent System

### 1. **Senior Research Specialist** (`agents/research_specialist.py`)
**Role**: Conducts web searches and finds sources
- Uses Serper API to search trusted websites
- Performs 5 targeted searches per topic
- Tracks source URLs for every finding
- Prioritizes authoritative sources

**Searches Performed**:
1. General overview
2. Statistics and data
3. Expert opinions and research
4. Recent developments (2024+)
5. Key facts

### 2. **Data Analyst** (`agents/data_analyst.py`)
**Role**: Analyzes research findings
- Identifies patterns and trends
- Cross-verifies findings across sources
- Preserves source URLs throughout analysis
- Provides expert interpretation

### 3. **Content Writer** (`agents/content_writer.py`)
**Role**: Creates professional reports
- Formats findings professionally
- Includes complete citations
- Creates business-ready documents
- Generates comprehensive bibliography

## 📋 Task Workflow

```
research_task → analysis_task → writing_task
    ↓              ↓                ↓
  Search        Analyze          Format
  Sources       Findings         Report
  & Track       & Verify         & Cite
  URLs          Sources          Sources
```

### Research Task (`tasks/research_task.py`)
- Executes 5 searches per topic
- Formats: **Finding** - Source: [URL]
- Only uses real sources (no made-up URLs)
- Cross-references information

### Analysis Task (`tasks/analysis_task.py`)
- Analyzes across sources
- Verifies information reliability
- Preserves all source URLs
- Identifies key insights

### Writing Task (`tasks/writing_task.py`)
- Creates professional report structure
- Includes Executive Summary
- Documents all findings with sources
- Generates complete bibliography

## 📄 Report Format

```markdown
# [Topic] - Professional Research Report
Generated: [Date]

## Executive Summary
[2-3 paragraph overview of key findings]

## Introduction
[Background and context]

## Key Findings
**Finding Title**: Description
- Source: Website Name
- URL: https://complete-url.com

## Statistics & Data
**Statistic Title**: Data value
- Source: Source Name
- URL: https://complete-url.com

## Expert Perspectives
**Expert Name**: "[Relevant quote]"
- Reference: Website Name
- URL: https://complete-url.com

## Recent Developments
**Development Title**: Description
- Source: Website Name
- URL: https://complete-url.com

## Analysis & Insights
[Professional analysis of findings]

## Conclusions & Recommendations
[Key conclusions and actionable recommendations]

## Sources & References
1. **Source Name** - URL
2. **Publication Name** - URL
3. **Website Name** - URL
```

## 🔧 Configuration

### API Keys (`.env`)
```
GROQ_API_KEY=your_groq_key           # LLM for analysis
SERPER_API_KEY=your_serper_key       # Web search API
```

### Models
- **LLM**: Groq (llama-3.3-70b-versatile)
- **Search**: Serper API
- **Framework**: CrewAI

## 📊 How It Works

1. **You run**: `python main.py "Cloud Computing"`

2. **Senior Research Specialist searches**:
   - Finds information from trusted sources
   - Records website names and URLs
   - Compiles initial findings

3. **Data Analyst reviews**:
   - Identifies patterns across sources
   - Verifies information reliability
   - Preserves all source citations

4. **Content Writer formats**:
   - Creates professional report
   - Includes all sources with URLs
   - Generates bibliography
   - Saves to `/reports/` directory

5. **You receive**: Professional research report ready to share

## ⏱️ Rate Limits

**Groq Free Tier:**
- ⏱️ Daily: 100,000 tokens/day
- ⏱️ Hourly: 12,000 tokens/minute

**If rate limit hit:**
```
Error: "Rate limit reached... Please try again in 12m"
Solution: 
  - Wait 24 hours for daily reset, OR
  - Upgrade to Groq Dev Tier, OR
  - Space out requests
```

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| **README.md** (this file) | Overview and architecture |
| **QUICK_REFERENCE.md** | Quick start and common commands |
| **PROFESSIONAL_RESEARCH_CONFIG.md** | Detailed configuration guide |

## 🚀 Usage Examples

### Basic Research
```bash
python main.py "Artificial Intelligence"
```

### Interactive Mode
```bash
python main.py
# When prompted: Enter the topic you want to research: Machine Learning
```

### Without Saving
```bash
python main.py "Blockchain" --no-save
```

### Check Generated Reports
```bash
ls -lh reports/
cat reports/report_*.md
```

## 📂 Output Locations

```
reports/
├── report_Artificial_Intelligence_20260610_190640.md
├── report_Machine_Learning_20260610_185655.md
└── report_Cloud_Computing_20260610_185428.md
```

## ✅ Features

- ✅ Multi-agent AI system (research, analysis, writing)
- ✅ Web search integration (Serper API)
- ✅ Source tracking with complete URLs
- ✅ Professional report formatting
- ✅ Automatic report generation
- ✅ Timestamped outputs
- ✅ Complete citations and bibliography
- ✅ Executive summaries
- ✅ Trend analysis
- ✅ Expert perspectives

## 🔗 Agent Connections

```
┌─────────────────────┐
│   main.py           │ ← Entry point
└──────────┬──────────┘
           │
           ▼
    ┌─────────────┐
    │  crew.py    │ ← Orchestrator
    └──────┬──────┘
           │
    ┌──────┴────────┬─────────────┐
    ▼               ▼             ▼
┌──────────┐  ┌──────────┐  ┌──────────┐
│Research  │  │Analysis  │  │  Writer  │
│Specialist│  │ Analyst  │  │  Agent   │
└──────────┘  └──────────┘  └──────────┘
     │             │             │
     ▼             ▼             ▼
 Serper API  Cross-verify  Professional
  Search      Sources       Report
```

## 🎯 Data Flow

```
Input: "Your Topic"
    ↓
Research Task (web search via Serper)
    ↓ (findings + URLs)
Analysis Task (verify & analyze)
    ↓ (insights + sources)
Writing Task (format professionally)
    ↓ (formatted report)
Output: /reports/report_[topic]_[timestamp].md
```

## 🆘 Troubleshooting

**Rate limit error:**
```
Error: "Rate limit reached for model"
Solution: Wait 24 hours or upgrade Groq tier
```

**Serper API error:**
```
Error: "403 Client Error: Forbidden"
Solution: Check SERPER_API_KEY in .env file
```

**No reports saved:**
```
Solution: Check /reports/ directory
```

## 📈 Report Quality

Quality factors:
- ✅ Multiple source searches
- ✅ Cross-source verification
- ✅ Recent information (includes 2024 data)
- ✅ Professional formatting
- ✅ Complete citations
- ✅ Expert analysis included

## 🔐 API Keys

Get your API keys:
1. **Groq API**: https://console.groq.com
2. **Serper API**: https://serper.dev

Add them to `.env`:
```
GROQ_API_KEY=your_key_here
SERPER_API_KEY=your_key_here
```

## 📝 Example Output

```
# Quantum Computing - Professional Research Report
Generated: 2026-06-10

## Executive Summary
Quantum computing represents a paradigm shift in computational power...

## Key Findings
**Quantum Advantage Achieved**: IBM demonstrates quantum advantage
- Source: IBM Research Blog
- URL: https://www.ibm.com/quantum/blog/quantum-advantage

**Market Growth**: Expected to reach $1.3B by 2030
- Source: McKinsey & Company
- URL: https://www.mckinsey.com/quantum-computing-report

## Sources & References
1. IBM Research - https://www.ibm.com/quantum
2. Nature Quantum - https://www.nature.com/nature-quantum
```

## 🎉 Ready to Use!

Everything is configured and linked. Just run:

```bash
python main.py "Your Research Topic"
```

Reports will be generated with complete sources, URLs, and professional formatting!

---

**For more details:**
- 📖 See `QUICK_REFERENCE.md` for common commands
- 📖 See `PROFESSIONAL_RESEARCH_CONFIG.md` for detailed configuration

**Last Updated**: 2026-06-10
