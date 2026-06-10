# Quick Reference Guide

## 🚀 Quick Start

```bash
# Research any topic - Professional report with sources
python main.py "Topic Name"

# Interactive mode
python main.py

# Without saving report
python main.py "Topic" --no-save

# Help
python main.py --help
```

## 📊 What You Get

✅ Professional research reports with:
- Web search from trusted sources (via Serper)
- Complete source URLs for every finding
- Executive summary
- Key findings with citations
- Statistics with sources
- Expert opinions with attribution
- Recent developments with links
- Professional formatting
- Complete bibliography

## 📁 Output Structure

```
my-research-assistant/
├── reports/
│   ├── report_Topic_Name_20260610_190640.md  ← Your main report
│   └── ...
├── main.py
└── agents/
```

## 🔍 How Reports are Researched

1. **5 Targeted Searches**
   - General overview
   - Statistics & data
   - Expert opinions
   - Recent developments (2024+)
   - Key facts

2. **Source Tracking**
   - Website name recorded
   - Full URL included
   - Only real sources used
   - Cross-verified where possible

3. **Professional Analysis**
   - Patterns identified
   - Trends analyzed
   - Sources verified
   - Implications noted

4. **Professional Writing**
   - Business report format
   - Complete citations
   - Clean formatting
   - Ready for sharing

## 📄 Report Format Example

```
# [Topic] - Professional Research Report
Generated: [Date]

## Executive Summary
[2-3 paragraph overview]

## Key Findings
**Finding Title**: [Description]
- Source: [Website]
- URL: [Full URL]

## Statistics & Data
**Statistic Title**: [Data]
- Source: [Website]
- URL: [Full URL]

## Expert Perspectives
**Expert Name**: "[Quote]"
- Source: [Website]
- URL: [Full URL]

## Recent Developments
**Development Title**: [Description]
- Source: [Website]
- URL: [Full URL]

## Sources & References
1. **Website Name** - URL
2. **Publication Name** - URL
```

## ⚙️ Configuration

**LLM Model**: Groq (llama-3.3-70b-versatile)
**Search Tool**: Serper API
**Reports Location**: `/reports` directory
**Output Format**: Markdown (.md)

## 🔑 API Keys

Already configured in `.env`:
- ✅ GROQ_API_KEY
- ✅ SERPER_API_KEY

## ⏱️ Rate Limits

**Groq Free Tier:**
- Daily limit: 100,000 tokens
- Hourly limit: 12,000 tokens/minute

**If you hit a rate limit:**
- Wait 24 hours for daily reset
- Upgrade to Groq Dev Tier
- Or space out your requests

## 📈 Typical Report Time

- Small topic: 2-3 minutes
- Medium topic: 5-8 minutes
- Large topic: 10-15 minutes

## 🎯 Best Practices

1. **Be specific** with topic names
   ✅ Good: "Machine Learning in Healthcare 2024"
   ❌ Bad: "AI"

2. **Check the report** when complete
   - Files save automatically to `/reports`

3. **Share reports** directly
   - Professional format ready for stakeholders

4. **Include sources** when citing
   - URLs included for verification

## 🔗 File Locations

| File | Purpose |
|------|---------|
| `main.py` | Entry point, handles CLI input |
| `agents/research_specialist.py` | Web search agent |
| `agents/data_analyst.py` | Analysis agent |
| `agents/content_writer.py` | Report writing agent |
| `tasks/research_task.py` | Search strategy |
| `tasks/analysis_task.py` | Data analysis |
| `tasks/writing_task.py` | Report formatting |
| `reports/` | All generated reports |
| `.env` | API keys |

## 🆘 Troubleshooting

**"Rate limit exceeded" error:**
- Wait 24 hours or upgrade Groq tier

**"No reports generated" error:**
- Check `/reports` directory
- View any `.md` files there

**"Serper API error" error:**
- Verify SERPER_API_KEY in .env
- Check Serper account has credits

---

**Ready to generate professional research reports!** 🎉
