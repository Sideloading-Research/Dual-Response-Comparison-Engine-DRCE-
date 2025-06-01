
# 🧠 Dual Response Comparison Engine (DRCE)

Toolset for evaluating how closely a sideloaded LLM with a *mindfile* replicates the personality and answers of a reference human.

Designed to support both **manual input** (e.g., via ChatGPT interface) and **automated testing pipelines**, with two core comparison modes: **LLM-based similarity scoring** and **Arena-style Elo ranking**.
Please, read the abstract.md file.

---

## 📌 Use Cases

- Evaluate alignment between a digital personality and its original.
- Track quality evolution across versions of a mindfile.
- Use human feedback or LLM judgment to score fidelity.
- Establish a repeatable benchmark for digital twin quality.

---

## 🧱 File Structure

```

drce/
├── responses/
│   ├── roman.md               # Human answers
│   ├── roman\_v1\_gpt4.md       # Mindfile v1 (GPT-4)
│   └── roman\_v2\_claude.md     # Mindfile v2 (Claude)
├── questions.txt              # Input question list
├── comparison.md              # Final Markdown output
├── comparison\_scores.json     # LLM-based scoring output
├── elo\_scores.json            # Arena-based scoring output
├── compare\_with\_llm.py        # Script for LLM comparisons
├── arena\_gui.py               # GUI for Elo comparisons
├── parse\_markdown.py          # Markdown parser utility
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation

````

---

## ⚙️ Installation

```bash
git clone https://github.com/Sideloading-Research/Dual-Response-Comparison-Engine-DRCE-.git
cd Dual-Response-Comparison-Engine-DRCE-
pip install -r requirements.txt
````

---

## 📝 1. Input Preparation

### `questions.txt`

Plain text list of questions, one per line:

```
What is your name?
Do you like pizza?
...
```

### `responses/*.md`

Markdown-style answer files:

```markdown
# What is your name?
Roman

# Do you like pizza?
Yes
```

Use one file per version (e.g., `roman.md`, `roman_v1_gpt4.md`, etc).

---

## 🚀 2. Run Comparisons

### 🧠 A. Automatic LLM Comparison

```bash
python compare_with_llm.py \
  --a responses/roman.md \
  --b responses/roman_v1_gpt4.md \
  --model gpt-4 \
  --output comparison_scores.json
```

* Uses an external LLM to score each Q-A pair by:

  * Semantic similarity
  * Stylistic fidelity
  * Human-likeness
* Outputs scores and a `comparison.md` file.

---

### 🧑‍⚖️ B. Arena-Style Elo Comparison (Manual GUI)

```bash
python arena_gui.py \
  --a responses/roman.md \
  --b responses/roman_v1_gpt4.md
```

* Presents Q and two anonymized answers (A vs. B).
* User selects the more "authentic" one.
* Elo score is updated accordingly.
* Results saved to `elo_scores.json`.

---

## 📄 3. Output Artifacts

### `comparison.md`

```markdown
## What is your name?

- 🧍 Original: Roman  
- 🤖 Mindfile-v1-GPT4: My name is Roman.

LLM Similarity Score: 9.5
```

### `comparison_scores.json`

```json
{
  "What is your name?": {
    "original": "Roman",
    "mindfile": "My name is Roman.",
    "similarity": 9.5
  },
  ...
}
```

### `elo_scores.json`

```json
{
  "roman.md": 1540,
  "roman_v1_gpt4.md": 1460
}
```

---

## 🔧 Configuration Options

Both comparison scripts accept:

* `--a`, `--b`: Markdown files to compare.
* `--model`: LLM to use (`gpt-4`, `claude-3-opus`, etc.).
* `--output`: JSON output path.
* `--system_prompt`: (Optional) Context to inject before comparison.

---

## 🔬 Evaluation Strategies

| Mode           | Requires LLM | Human Judgment | Quantitative |
| -------------- | ------------ | -------------- | ------------ |
| LLM Similarity | ✅            | ❌              | ✅            |
| Arena Elo      | ❌            | ✅              | ✅            |

| Method         | Output                   | Manual | Objective |
| -------------- | ------------------------ | ------ | --------- |
| LLM similarity | `comparison_scores.json` | ❌      | ✅         |
| Arena GUI      | `elo_scores.json`        | ✅      | ✅         |


Both modes are complementary.

## ✅ Summary of Supported Workflows
| Task                              | Manual | Automated |
| --------------------------------- | ------ | --------- |
| Human answer collection           | ✅      | ❌         |
| Sideloaded LLM answer collection  | ✅      | ✅         |
| Answer comparison via LLM         | ❌      | ✅         |
| Answer comparison via Arena (GUI) | ✅      | ✅         |
| Markdown report generation        | ✅      | ✅         |

---

## 🛠️ Future Work

* Web dashboard for batch comparisons.
* Support for sentence-transformer metrics (BERTScore, cosine).
* CSV export of Q-A-Similarity tables.
* API endpoint for continuous evaluation.
* Friend Peer Review (FPR) integration.

---

## 📜 License

MIT License (customize as needed)

---

## 🙋 Contribution

Feel free to fork, adapt, and improve. Open issues or PRs are welcome.


