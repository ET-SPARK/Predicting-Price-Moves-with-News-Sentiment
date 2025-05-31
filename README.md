# Predicting Stock Price Movements with News Sentiment

This repository contains the codebase for analyzing the relationship between news sentiment and stock price movements. The project is divided into three main tasks:

- **Task 1**: Git and GitHub with Exploratory Data Analysis (EDA)
- **Task 2**: Quantitative Analysis using PyNance and TA-Lib
- **Task 3**: Correlation Analysis between News Sentiment and Stock Movements

---

## 📑 Table of Contents

- [Project Overview](#project-overview)
- [Key Findings](#-key-findings)
- [Folder Structure](#folder-structure)
- [Setup Instructions](#setup-instructions)
- [Task 1: Git and GitHub with EDA](#task-1-git-and-github-with-eda)
- [Task 2: Quantitative Analysis](#task-2-quantitative-analysis)
- [Task 3: News-Stock Correlation](#task-3-news-stock-correlation)
- [Git Workflow](#git-workflow)
- [Key Performance Indicators (KPIs)](#key-performance-indicators-kpis)
- [Contributing](#contributing)
- [License](#license)

---

## 🚀 Project Overview

This project aims to predict stock price movements by combining news sentiment analysis with technical indicators.

- **Task 1**: Setting up a Python environment and performing EDA on news data
- **Task 2**: Calculating technical indicators using TA-Lib and financial metrics
- **Task 3**: Analyzing correlation between news sentiment and stock price movements

---

## 📁 Folder Structure

```
├── .vscode/
│   └── settings.json            # VS Code settings for the project
├── .github/
│   └── workflows/
│       └── unittests.yml       # GitHub Actions workflow for running unit tests
├── .gitignore                  # Files and folders to ignore in Git
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation (this file)
├── src/
│   ├── __init__.py             # Source code package initialization
│   └── ...                     # Python scripts for data processing and analysis
├── notebooks/
│   ├── __init__.py             # Notebooks package initialization
│   ├── README.md               # Documentation for Jupyter notebooks
│   └── ...                     # Jupyter notebooks for EDA
├── tests/
│   ├── __init__.py             # Tests package initialization
│   └── ...                     # Unit tests for the codebase
├── scripts/
│   ├── __init__.py             # Scripts package initialization
│   ├── README.md               # Documentation for utility scripts
│   └── ...                     # Utility scripts for automation or data processing
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ET-SPARK/Predicting-Price-Moves-with-News-Sentiment.git
cd Predicting-Price-Moves-with-News-Sentiment
```

### 2. Set Up Python Environment

Ensure Python 3.8+ is installed.

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install TA-Lib

Follow the TA-Lib installation guide for your OS. Then install the Python wrapper:

```bash
pip install TA-Lib
```

### 5. Run Notebooks or Scripts

- Open Jupyter notebooks in the `notebooks/` folder for EDA.
- Run scripts in the `scripts/` folder for automated tasks.

---

## 🧪 Task 1: Git and GitHub with EDA

### Objectives

- Set up Python and Git environment.
- Perform EDA on news data:
  - Headline length, article counts per publisher, publication date trends
  - Topic modeling for common phrases
  - Time series analysis on publication frequency
  - Publisher activity insights

### Implementation

- Created branch `task-1` for EDA.
- Minimum of 3 commits/day with messages like "Added headline length analysis".
- Used pandas, NLTK, scikit-learn in Jupyter notebooks for analysis.
- Identified publication and sentiment trends.

---

## 📉 Task 2: Quantitative Analysis

### Objectives

- Load stock data (OHLCV format).
- Calculate indicators: SMA, EMA, RSI, MACD via TA-Lib.
- Use PyNance for returns, volatility.
- Visualize using matplotlib and seaborn.

### Implementation

- Merged `task-1` into `main` via PR.
- Created `task-2` branch.
- Computed indicators and financial metrics.
- Visualized results with candlestick charts and overlays.

---

## 📉 Task 3: News-Stock Correlation

### Objectives

- Align news dates with trading days
- Perform sentiment analysis using TextBlob
- Calculate daily stock returns
- Measure correlation between:
- News sentiment scores
- Next-day price movements

### Implementation

- Created task-3 branch
- Developed date alignment algorithm
- Implemented sentiment scoring (-1 to +1)
- Generated correlation visualizations:

---

## 🔁 Git Workflow

- **Repo**: `ET-SPARK/Predicting-Price-Moves-with-News-Sentiment`
- **Branches**:
  - `main`: Stable codebase
  - `task-1`: EDA
  - `task-2`: Quantitative Analysis
- **Commits**: Minimum 3/day with descriptive messages
- **CI/CD**: GitHub Actions with `unittests.yml`
- **PRs**: For merging feature branches

---

## 📊 Key Performance Indicators (KPIs)

### Task 1

- Python + Git setup verified
- CI/CD pipeline operational
- Comprehensive EDA on news data

### Task 2

- Learned and applied TA-Lib and PyNance
- Accurate technical indicator calculations
- Complete visualization of analysis results

---

### Task 3 Correlation Results

| Symbol | Correlation | P-Value | Observations |
| ------ | ----------- | ------- | ------------ |
| AAPL   | -0.003      | 0.876   | 2,228        |
| AMZN   | -0.014      | 0.502   | 2,228        |
| GOOG   | +0.014      | 0.521   | 2,228        |
| META   | -0.004      | 0.877   | 1,847        |
| MSFT   | -0.012      | 0.586   | 2,228        |
| NVDA   | +0.011      | 0.616   | 2,228        |
| TSLA   | +0.026      | 0.217   | 2,228        |

**Interpretation**:

- All correlations are near-zero (-0.014 to +0.026)
- High p-values (>0.05) indicate no statistically significant relationship
- News sentiment alone doesn't reliably predict daily stock movements
- TSLA shows the strongest (but still weak) positive correlation

---

## 🤝 Contributing

Contributions welcome!

1. Fork this repository.
2. Create a branch: `git checkout -b feature-branch`.
3. Commit changes: `git commit -m "Add feature"`.
4. Push: `git push origin feature-branch`.
5. Submit a Pull Request.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
