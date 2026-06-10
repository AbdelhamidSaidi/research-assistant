# Project Structure

## 📁 Organized Directory Layout

```
my-research-assistant/
│
├── 📄 main.py                    ← Entry point (forwards to src/main.py)
├── 📄 .env                       ← API keys (GROQ_API_KEY, SERPER_API_KEY)
├── 📄 PROJECT_STRUCTURE.md       ← This file
│
├── 📂 src/                       ← Source code (application logic)
│   ├── 📄 main.py               ← CLI interface & orchestration
│   ├── 📄 crew.py               ← Three-agent coordinator
│   │
│   ├── 📂 agents/               ← AI Agents
│   │   ├── 📄 research_specialist.py    ← Web search agent (Serper)
│   │   ├── 📄 data_analyst.py           ← Analysis agent
│   │   └── 📄 content_writer.py         ← Report writing agent
│   │
│   └── 📂 tasks/                ← Task definitions
│       ├── 📄 research_task.py         ← Search strategy & source tracking
│       ├── 📄 analysis_task.py         ← Data analysis & verification
│       └── 📄 writing_task.py          ← Professional report formatting
│
├── 📂 docs/                      ← Documentation
│   ├── 📄 README.md                    ← Main documentation & architecture
│   ├── 📄 QUICK_REFERENCE.md           ← Quick start guide
│   ├── 📄 PROFESSIONAL_RESEARCH_CONFIG.md  ← Configuration details
│   ├── 📄 SYSTEM_ARCHITECTURE.md       ← Complete system diagram
│   └── 📄 REPORTS_SETUP.md             ← Reports directory setup
│
└── 📂 reports/                   ← Generated research reports
    ├── report_Topic_20260610_190640.md
    └── report_*.md
```

## 📊 File Organization Guide

### **Root Level**
- `main.py` - Entry point (forwards to src/main.py)
- `.env` - API configuration
- `PROJECT_STRUCTURE.md` - This file

### **src/ - Application Code**

**src/main.py**
- CLI argument parsing
- Entry point for the application
- Report file saving logic

**src/crew.py**
- Orchestrates three-agent system
- Manages task workflow
- Coordinates agents

**src/agents/ - AI Agents**
- `research_specialist.py` - Web search via Serper
- `data_analyst.py` - Analysis & verification
- `content_writer.py` - Report generation

**src/tasks/ - Task Definitions**
- `research_task.py` - Search strategy & source tracking
- `analysis_task.py` - Data analysis workflow
- `writing_task.py` - Professional formatting

### **docs/ - Documentation**

- `README.md` - System overview, architecture, usage
- `QUICK_REFERENCE.md` - Quick start commands
- `PROFESSIONAL_RESEARCH_CONFIG.md` - Configuration guide
- `SYSTEM_ARCHITECTURE.md` - Complete linking diagram
- `REPORTS_SETUP.md` - Reports directory documentation

### **reports/ - Generated Output**

- `report_[topic]_[timestamp].md` - Generated research reports
- All reports include: sources, URLs, citations, professional formatting

## 🚀 How to Use

### From Root Directory
```bash
# Everything runs from root - main.py forwards to src/main.py
python main.py "Cloud Computing"
python main.py
python main.py --help
```

### Running from src/ (Alternative)
```bash
cd src
python main.py "Your Topic"
```

## 🔄 Import Structure

### From Root (Recommended)
```python
# main.py at root automatically handles imports
python main.py "Topic"
```

### From src/
```python
# Files in src/ import each other directly
from crew import research_crew        # crew.py imports from agents/ & tasks/
from agents.research_specialist import research_specialist_agent
```

## 📖 Documentation Files

| File | Location | Purpose |
|------|----------|---------|
| README.md | docs/ | Main documentation & system overview |
| QUICK_REFERENCE.md | docs/ | Quick start & common commands |
| PROFESSIONAL_RESEARCH_CONFIG.md | docs/ | Configuration & setup guide |
| SYSTEM_ARCHITECTURE.md | docs/ | Complete system diagram & flow |
| REPORTS_SETUP.md | docs/ | Reports directory setup |
| PROJECT_STRUCTURE.md | root | This file - explains file organization |

## 🔗 Component Links

```
root/main.py
    ↓ (forwards to)
src/main.py
    ↓ (imports)
src/crew.py
    ↓ (manages)
src/agents/ + src/tasks/
    ↓ (generates)
reports/
```

## 📁 Key Benefits of This Structure

✅ **Separation of Concerns**
- `src/` - Application logic
- `docs/` - Documentation
- `reports/` - Output files

✅ **Easy Navigation**
- Documentation centralized in `docs/`
- Source code organized in `src/`
- Clear purpose for each directory

✅ **Simple Usage**
- Users run `python main.py` from root
- No need to navigate to `src/` directory
- Automatic path forwarding

✅ **Professional Layout**
- Follows Python project conventions
- Easy to understand for new users
- Scalable for future additions

## 🔄 Adding New Features

### Add New Agent
```
src/agents/new_agent.py
├── Import in: src/crew.py
└── Create corresponding task
```

### Add New Task
```
src/tasks/new_task.py
├── Import in: src/crew.py
└── Link to agent
```

### Add Documentation
```
docs/new_doc.md
├── Reference in: docs/README.md
└── Link in: PROJECT_STRUCTURE.md
```

## 🧪 Testing from Different Locations

### From Root
```bash
python main.py "Test Topic"          # ✅ Works
```

### From src/
```bash
cd src
python main.py "Test Topic"          # ✅ Works
```

### From any subdirectory
```bash
cd some/other/path
python /path/to/my-research-assistant/main.py "Test"  # ✅ Works
```

## 📊 Project Statistics

- **Source files**: 5 (main, crew, 3 agents, 3 tasks)
- **Documentation files**: 5 guides
- **Total directories**: 3 (src, docs, reports)
- **Configuration files**: 1 (.env)
- **Entry points**: 1 (main.py at root)

## ✅ Verification Checklist

- ✅ `main.py` at root forwards to `src/main.py`
- ✅ All source code in `src/` directory
- ✅ All documentation in `docs/` directory
- ✅ Reports generate to `reports/` directory
- ✅ `.env` at root with API keys
- ✅ Import paths correct within `src/`
- ✅ All agents and tasks properly organized
- ✅ Documentation updated with new structure

## 🎯 Next Steps

1. **Review Structure**
   ```bash
   tree -L 2 .
   ```

2. **Read Documentation**
   ```bash
   cat docs/README.md
   ```

3. **Try It Out**
   ```bash
   python main.py "Your Topic"
   ```

4. **Check Reports**
   ```bash
   ls -lh reports/
   ```

---

**Status**: ✅ Project reorganized and fully functional!

**Last Updated**: 2026-06-10
