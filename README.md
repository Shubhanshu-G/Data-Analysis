# 📊 Data Analysis Portfolio — Shubhanshu-G

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=flat&logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=flat)

A collection of end-to-end data analysis projects — from raw data exploration to deployed interactive dashboards. Each project tackles a real-world problem using Python, machine learning, and Streamlit.

---

## 🗂️ Projects

### ⚡ 1. Net Load Forecasting & Renewable Penetration
> *How does growing renewable energy make power grids harder to manage — and can we still forecast accurately?*

Analyses **PJM RTO** electricity grid data (2014–2025) to study the impact of increasing solar and wind generation on net load forecasting. Builds and evaluates an **XGBoost** model across different renewable penetration regimes, and demonstrates the deepening **"duck curve"** effect over a decade.

| | |
|---|---|
| 📁 Folder | [`Forecasting data analyis/`](./Forecasting%20data%20analyis/) |
| 🔗 Live App | [pjmrtoanalysis.streamlit.app](https://pjmrtoanalysis.streamlit.app) |
| 📓 Notebook | `Netload_Forecasting_Local.ipynb` |

**Key findings:**
- Net load volatility and ramp requirements grow significantly with renewable penetration
- XGBoost outperforms SARIMA under high-RP conditions
- Short-term lags (Lag 1, Lag 24) dominate feature importance — net load is strongly autoregressive

**Dashboard tabs:**

| Tab | What it shows |
|---|---|
| Exploratory Data Analysis | Load/solar/wind trends, duck curve, hourly profiles |
| Renewable Trends | Annual RP growth, regime segmentation |
| Forecasting Insights | Actual vs Predicted, NRMSE, feature importance, DM test |
| Dataset | Preview + download the full preprocessed dataset |

---

### 🤖 2. Prompt Evaluation EDA & Dashboard
> *What separates a high-quality AI prompt from a poor one?*

Explores a large-scale AI prompt quality dataset to uncover patterns in **quality scores**, **hallucination risk**, **clarity**, **specificity**, and **task type distributions**. Includes a full EDA notebook and an interactive Streamlit dashboard with dynamic filters and CSV export.

| | |
|---|---|
| 📁 Folder | [`Prompt evaluation/`](./Prompt%20evaluation/) |
| 🔗 Live App | [promptevaluation.streamlit.app](https://promptevaluation.streamlit.app) |
| 📓 Notebook | `EDA.ipynb` |
| 🖥️ Dashboard | `app1.py` |

**Dashboard features:**
- Filter by **Task Type** and **Grade** via sidebar
- Visualizations: quality score histogram, hallucination risk violin plot, task type donut chart, quality-by-task box plot
- Export filtered results as CSV

---

## 🛠️ Tech Stack

| Tool | Used For |
|---|---|
| Python 3.10+ | Core language |
| Streamlit | Interactive web dashboards |
| Pandas / NumPy | Data wrangling & processing |
| Matplotlib / Seaborn | Statistical visualizations |
| Plotly | Interactive charts |
| XGBoost | Time-series forecasting model |
| Jupyter Notebook | Exploratory analysis |
| Streamlit Cloud | Deployment |

---

## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/Shubhanshu-G/Data-Analysis.git
cd Data-Analysis

# Install dependencies
pip install -r requirements.txt

# Run Net Load Forecasting dashboard
streamlit run "Forecasting data analyis/app.py"

# Run Prompt Evaluation dashboard
streamlit run "Prompt evaluation/app1.py"
```

---

## 📁 Repository Structure

```
Data-Analysis/
│
├── Forecasting data analyis/        # ⚡ Net Load Forecasting project
│   ├── app.py                       # Streamlit dashboard
│   ├── stream_utils.py              # Data & plot utilities
│   ├── combined_preprocessed_dataset.csv
│   ├── Plots/                       # Pre-generated figures
│   ├── Netload_Forecasting_Local.ipynb
│   └── README.md
│
├── Prompt evaluation/               # 🤖 Prompt Quality EDA project
│   ├── app1.py                      # Streamlit dashboard
│   ├── eda_utils.py                 # Plotly visualization utilities
│   ├── EDA.ipynb                    # Exploratory analysis notebook
│   ├── Cleaned_dataset.csv
│   └── README.md
│
├── requirements.txt                 # Shared Python dependencies
└── README.md                        # This file
```

---

## 👤 Author

**Shubhanshu G**
- GitHub: [@Shubhanshu-G](https://github.com/Shubhanshu-G)
