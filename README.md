# Enhanced Prompt Engineering for GPT-based Topic Modeling in Finance

This repository contains the code and notebooks used in a master’s thesis project on **prompt engineering for GPT-based topic modeling** on financial documents (SEC 10‑K HTML filings). The workflow covers:

- Downloading SEC filings (EDGAR) as HTML
- Loading + chunking documents
- Generating topic labels/keywords with LLM prompts:
  - **Zero‑shot baseline**
  - **Prompt‑space factorisation (default)**
  - **Ablation design** (Role / Rubric+Constraints / Exemplars / Delimiter)
- Evaluating topic quality (coherence, distinctness, LLM-as-judge clarity)
- Visualising results

---

## Project structure

```
.
├─ Getting_Data.ipynb                  # Download SEC filings (HTML) via EDGAR
├─ Zeroshot(Baseline).ipynb            # Zero-shot + minimal-template baselines
├─ Prompt-space Factorisation.ipynb    # Factorised prompt pipeline
├─ Ablation Design.ipynb               # Prompt component ablations (2^4 variants)
├─ Evaluation.ipynb                    # Metrics: NPMI / C_V / distinctness / judge
├─ Visualize.ipynb                     # Figures (e.g., ablation design matrix)
│
├─ Load_Data.py                        # HTML loader -> LangChain Documents
├─ Chunking.py                         # Recursive chunking (LangChain splitters)
├─ LLM_setting.py                      # Groq + LangChain ChatGroq settings
│
├─ data/
│  └─ raw_filings/                     # Downloaded filings (HTML)
├─ outputs/                            # JSON outputs (runs + evaluation)
└─ Figures/Python-charts/              # Saved plots
```

> Note: Some notebooks expect certain output files (e.g., `outputs/*.json`) to exist from previous steps.

---

## Requirements

### System
- Python **3.10+**
- macOS / Linux / Windows

### Python packages
Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## Setup

### 1) Create & activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate  # Windows PowerShell
```

### 2) Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3) Configure environment variables

Create a `.env` file in the project root (or export env vars in your shell).

Minimal required:

```bash
GROQ_API_KEY=your_key_here
```

You can start from `.env.example`.

### 4) Download NLTK resources (needed for coherence tokenisation)

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

---

## How to run (recommended order)

### Step 1 — Download filings
Open and run: **`Getting_Data.ipynb`**

- Downloads SEC filings to `data/raw_filings/`
- The notebook uses a `HEADERS['User-Agent']` string. SEC requires a valid user agent.
  Replace it with your own email/identifier if needed.

### Step 2 — Baselines
Run: **`Zeroshot(Baseline).ipynb`**

- Loads HTML (via `Load_Data.py`)
- Chunks content (via `Chunking.py`)
- Queries the LLM using:
  - zero-shot instruction
  - minimal template baseline
- Saves outputs to `outputs/` (JSON)

### Step 3 — Prompt-space factorisation (default)
Run: **`Prompt-space Factorisation.ipynb`**

- Uses the factorised prompt components
- Produces consolidated final topics (JSON)

### Step 4 — Ablation variants
Run: **`Ablation Design.ipynb`**

- Runs 2^4 prompt variants toggling: Role / Rubric+Constraints / Exemplars / Delimiter
- Writes each run to: `outputs/ablation_runs/`

### Step 5 — Evaluation
Run: **`Evaluation.ipynb`**

Computes:
- **NPMI** and **C_V** coherence (Gensim)
- **Distinctness ratio** (unique keywords / total keyword slots)
- Optional: **LLM-as-judge clarity** scoring (if enabled in notebook)

### Step 6 — Visualisation
Run: **`Visualize.ipynb`**

- Generates plots (e.g., ablation design matrix)
- Saves to `Figures/Python-charts/`

---

## Notes on configuration

### Groq / LLM settings
`LLM_setting.py` creates a `ChatGroq` model using `GROQ_API_KEY`.
Adjust model name and temperature in notebooks where `LLMSetting(...)` is instantiated.

### Data loading
`Load_Data.py` uses `UnstructuredHTMLLoader` from `langchain_community`.
If the HTML parsing fails, try:
- ensuring the file path exists
- updating `unstructured` dependencies (already included via LangChain extras in many installs)

---

## Reproducibility tips

- Keep raw run outputs in `outputs/` and avoid overwriting filenames.
- Save a copy of:
  - prompt text
  - model name + temperature
  - chunking settings (chunk size/overlap)
  - date/time of run

---

## Citation
If you reuse this code, please cite the associated thesis (add your final bibliographic reference here).

---

## License
Add a license if you plan to share this repository publicly (e.g., MIT).

