# 🔬 Research Assistant

Multi-agent AI system that conducts thorough web research, analyzes findings, and generates professional reports with complete source attribution and URLs.

## ✨ Features

- 🔍 **Web Search Integration** - Uses Serper API for trusted website searches
- 📊 **Source Tracking** - Every finding includes source website name and complete URL
- 📄 **Professional Reports** - Publication-quality formatting with proper citations
- 🤖 **Multi-Agent System** - Three specialized AI agents working together
- 📈 **Cross-Verification** - Information verified across multiple sources
- 💼 **Business Ready** - Executive summaries, statistics, expert opinions, recommendations
- ⚡ **Fast & Efficient** - Generates comprehensive reports in minutes
- 📚 **Well Documented** - Extensive guides and examples included

## 🚀 Quick Start

### 1. **Installation**

```bash
# Clone or navigate to project
cd my-research-assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your API keys:
# GROQ_API_KEY=your_key_here
# SERPER_API_KEY=your_key_here
```

### 2. **Generate Research Report**

```bash
# Generate professional research report
python main.py "Cloud Computing"

# Interactive mode
python main.py

# Show help
python main.py --help
```

### 3. **Find Your Report**

```bash
# Reports saved automatically to /reports/
ls -lh reports/

# View the report
cat reports/report_Cloud_Computing_*.md
```

## 📊 What You Get

Each report includes:

✅ **Executive Summary** - Key findings at a glance
✅ **Key Findings** - With source URLs
✅ **Statistics & Data** - With proper citations
✅ **Expert Perspectives** - Attributed quotes
✅ **Recent Developments** - Current information
✅ **Analysis & Insights** - Professional interpretation
✅ **Conclusions & Recommendations** - Actionable takeaways
✅ **Complete Bibliography** - All sources with links

## 🏗️ Project Structure

```
my-research-assistant/
├── main.py                 ← Entry point
├── .env                    ← API configuration
├── requirements.txt        ← Python dependencies
│
├── src/                    ← Source Code
│   ├── main.py            ← CLI & file handling
│   ├── crew.py            ← Agent orchestrator
│   ├── agents/            ← AI Agents
│   │   ├── research_specialist.py
│   │   ├── data_analyst.py
│   │   └── content_writer.py
│   └── tasks/             ← Task definitions
│       ├── research_task.py
│       ├── analysis_task.py
│       └── writing_task.py
│
├── docs/                   ← Documentation
│   ├── README.md
│   ├── QUICK_REFERENCE.md
│   ├── PROFESSIONAL_RESEARCH_CONFIG.md
│   └── SYSTEM_ARCHITECTURE.md
│
└── reports/                ← Generated Reports
    └── report_*.md
```

## 🤖 How It Works

### Three-Agent System

```
┌─────────────────────┐
│  Senior Research    │
│     Specialist      │  ← Searches web via Serper API
│                     │     Tracks sources & URLs
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Data Analyst      │
│                     │  ← Analyzes findings
└──────────┬──────────┘     Cross-verifies sources
           │
           ▼
┌─────────────────────┐
│  Content Writer     │
│                     │  ← Creates professional report
└──────────┬──────────┘     Formats with citations
           │
           ▼
    📄 Research Report
   (with sources & URLs)
```

### Workflow

1. **Research Phase** - Conducts 5 targeted searches per topic
   - General overview search
   - Statistics & data search
   - Expert opinions search
   - Recent developments search
   - Key facts search

2. **Analysis Phase** - Evaluates and verifies findings
   - Cross-references sources
   - Identifies patterns and trends
   - Verifies information reliability
   - Preserves all source citations

3. **Writing Phase** - Creates professional report
   - Formats findings professionally
   - Includes complete citations
   - Generates bibliography
   - Saves to `/reports/` directory

## 📖 Documentation

| Document | Purpose |
|----------|---------|
| **README.md** (this file) | Project overview & quick start |
| **docs/README.md** | Detailed system documentation |
| **docs/QUICK_REFERENCE.md** | Common commands & examples |
| **docs/PROFESSIONAL_RESEARCH_CONFIG.md** | Configuration guide |
| **docs/SYSTEM_ARCHITECTURE.md** | Complete system diagram |
| **PROJECT_STRUCTURE.md** | File organization guide |
| **GITIGNORE_GUIDE.md** | Git & version control setup |

## ⚙️ Configuration

### Required APIs

**Groq API** (Free LLM)
```
Sign up: https://console.groq.com
Model: llama-3.3-70b-versatile
```

**Serper API** (Web Search)
```
Sign up: https://serper.dev
Free tier: 100 searches/month
```

### Environment Setup

Create `.env` file:
```bash
GROQ_API_KEY=your_groq_api_key_here
SERPER_API_KEY=your_serper_api_key_here
RESEARCH_AGENT_LLM=groq/llama-3.3-70b-versatile
ANALYST_AGENT_LLM=groq/llama-3.3-70b-versatile
WRITER_AGENT_LLM=groq/llama-3.3-70b-versatile
RESEARCH_AGENT_TEMPERATURE=0.1
ANALYST_AGENT_TEMPERATURE=0.2
WRITER_AGENT_TEMPERATURE=0.3
QA_AGENT_TEMPERATURE=0.4
```

## 💻 Usage Examples

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

### View Generated Report
```bash
# List all reports
ls -lh reports/

# View specific report
cat reports/report_*.md

# Open in editor
code reports/report_*.md
```

## 📊 Report Example

```markdown
# Artificial Intelligence - Professional Research Report
Generated: 2026-06-10

## Executive Summary
Artificial intelligence is rapidly transforming industries...

## Key Findings

**Market Growth**: The global AI market is projected to reach $1.8 trillion by 2030
- Source: McKinsey & Company
- URL: https://www.mckinsey.com/capabilities/quantumblack/our-insights/ai-report

**Healthcare Applications**: AI is improving diagnostic accuracy to 95%
- Source: Nature Medicine Journal
- URL: https://www.nature.com/articles/nature-medicine-ai

## Sources & References
1. McKinsey & Company - https://www.mckinsey.com/...
2. Nature Medicine - https://www.nature.com/...
```

## 🎯 Use Cases

- 📚 **Research Papers** - Gather background information
- 💼 **Business Reports** - Market analysis and trends
- 📰 **News Briefings** - Current developments
- 🎓 **Academic Research** - Literature review
- 🔬 **Industry Analysis** - Competitive intelligence
- 📊 **Market Research** - Trend analysis
- 🌍 **Trend Monitoring** - Stay updated on topics

## ⏱️ Performance

| Task | Time |
|------|------|
| Small topic | 2-3 minutes |
| Medium topic | 5-8 minutes |
| Large topic | 10-15 minutes |
| Multiple searches | Depends on results |

## 🔗 API Rate Limits

**Groq Free Tier:**
- Daily: 100,000 tokens/day
- Hourly: 12,000 tokens/minute

**Solutions if rate limited:**
- Wait 24 hours for daily reset
- Upgrade to Groq Dev Tier
- Space out requests

## 🆘 Troubleshooting

### "Rate limit exceeded" error
```
Solution: Wait 24 hours or upgrade Groq tier
```

### "Serper API error" error
```
Solution: Verify SERPER_API_KEY in .env file
         Check Serper account has credits
```

### "No reports generated" error
```
Solution: Check /reports/ directory
         View any .md files there
```

### Module not found errors
```
Solution: pip install -r requirements.txt
         Ensure virtual environment activated
```

## 🔐 Security

✅ **Protected**
- API keys in `.env` (never committed)
- `.claude/` directory ignored
- `__pycache__/` ignored

✅ **Best Practices**
- Never commit `.env` file
- Use `.env.example` for template
- Rotate API keys regularly
- Keep dependencies updated

## 📦 Dependencies

```
crewai              # Multi-agent framework
python-dotenv       # Environment variables
groq                # Groq API
serper              # Web search API
litellm             # LLM wrapper
```

See `requirements.txt` for complete list.

## 🚀 Advanced Features

### Custom Topics
```bash
python main.py "Advanced Topic Name with Details"
```

### Parallel Research
```bash
# Run multiple researches
python main.py "Topic 1"
python main.py "Topic 2"
python main.py "Topic 3"
```

### Report Customization
Edit `src/tasks/writing_task.py` to customize report format

### Add New Agents
Add new agent to `src/agents/` and register in `src/crew.py`

## 🤝 Contributing

To improve this project:

1. Create a new branch: `git checkout -b feature/improvement`
2. Make changes and test
3. Commit: `git commit -m "Add improvement"`
4. Push: `git push origin feature/improvement`
5. Create Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 🙋 Support

### Documentation
- Read `docs/README.md` for detailed documentation
- Check `docs/QUICK_REFERENCE.md` for common commands
- Review `docs/SYSTEM_ARCHITECTURE.md` for system design

### Troubleshooting
- See `docs/PROFESSIONAL_RESEARCH_CONFIG.md` for configuration help
- Check error messages and relevant documentation section

### Questions?
Refer to the documentation files in the `docs/` directory or check the project's GitHub issues.

## 🎉 Getting Started Now

```bash
# 1. Setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env

# 2. Configure
# Edit .env with your API keys

# 3. Research
python main.py "Your Topic"

# 4. Review
cat reports/report_*.md
```

## 📊 System Requirements

- Python 3.8+
- 2GB RAM minimum
- Internet connection (for API calls)
- API keys from Groq and Serper

## 🌟 Key Highlights

✨ **Multi-Agent AI** - Three specialized agents working in harmony
✨ **Professional Reports** - Publication-quality output
✨ **Source Tracking** - Every claim has a verifiable source
✨ **Fast & Efficient** - Comprehensive reports in minutes
✨ **Well Organized** - Clean project structure
✨ **Extensively Documented** - Multiple guides included
✨ **Easy to Use** - Simple CLI interface
✨ **Scalable** - Ready for expansion

## 🚀 Next Steps

1. **Install** - Follow Installation section above
2. **Configure** - Set up API keys in `.env`
3. **Try It** - Run `python main.py "Your Topic"`
4. **Explore** - Check reports in `/reports/` directory
5. **Learn** - Read documentation in `docs/` folder
6. **Customize** - Modify for your specific needs

---

**Made with ❤️ using CrewAI, Groq, and Serper**
