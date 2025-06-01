# DRCE - Digital Replica Comparison Engine

**Authors**: Roman Sitelew, Alexey Turchin, Marco Baturan

## Overview

DRCE (Digital Replica Comparison Engine) is a toolkit for evaluating and benchmarking digital replicas (sideloads) of human minds via structured Q\&A comparisons.

It supports both:

* **Manual** comparisons using a simple GUI (Arena-style Elo rating).
* **Automated** similarity scoring using top-tier LLMs (e.g., GPT-4).

The goal is to evaluate how closely a sideload mimics the original person, question-by-question.

## Features

* 🧠 Parse Q\&A from markdown
* 🤖 Compare original vs. replica answers using LLMs (semantic/style/authenticity)
* 🏆 Rate answer pairs manually with a local GUI (Elo-based)
* 📁 Generate structured evaluation output for benchmarking
* ✅ Supports fully manual workflows for custom ChatGPT sessions

---

## Folder Structure

```
drce/
├── parse_markdown.py         # Extract Q&A pairs from markdown
├── compare_with_llm.py       # Automated comparison using LLM API
├── arena_gui.py              # Manual comparison via GUI (Elo rating)
├── requirements.txt
└── README.md
```

---

## Example Markdown Input Format

```markdown
# What is your name?
Roman

# Do you like pizza?
Yes
```

You can create multiple such files:

* One for the original person
* One for each sideload version

---

## Usage

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Parse and compare via LLM

```bash
python compare_with_llm.py --a original.md --b sideload_v1.md --output results.json
```

This generates a JSON file with structured similarity scores.

### 3. Run GUI Arena Comparison

```bash
python arena_gui.py --a original.md --b sideload_v1.md --output elo_scores.json
```

This opens a window where a human rater chooses the more authentic answer. The script calculates Elo ratings per version.

---

## Notes

* The markdown format must use `#` for each question and answers directly below.
* Comparisons assume aligned Q\&A structure.
* `openai` is used as default LLM client; replace as needed (Claude, Gemini, etc.).
* For manual workflows (e.g. ChatGPT web), users can paste and save responses manually in the same markdown format.

---

## Planned Extensions

* CLI tool to combine original + sideloads into comparative markdown report
* JSON-to-Markdown converter for multi-format exports
* CLI Elo summary dashboard
* Integration with peer-review rater inputs (Friend Peer Review)

---

## License

Open-source model, MIT-style license (to be defined by authors).

**Project Initiated By**:

* Roman Sitelew
* Alexey Turchin
* Marco Baturan
