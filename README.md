# Prompt Evaluation EDA & Dashboard

This repository contains a comprehensive Exploratory Data Analysis (EDA) and an interactive Streamlit Dashboard for evaluating prompt quality. It analyzes key metrics such as **quality score**, **hallucination risk**, **clarity**, **specificity**, and **structure** to help identify patterns in successful AI prompting.

## 📊 Features

1. **Jupyter Notebook EDA (`EDA copy.ipynb`)**
   - Detailed data cleaning and feature engineering.
   - Normalization of rating features to derive a 100-point custom scoring system.
   - Statistical visualizations (histograms, box plots, pie charts) analyzing the distribution of various task types and their correlation to hallucination risks.
   - *Tip:* The notebook includes inline charts and comprehensive markdown explanations for easy readability.

2. **Interactive Streamlit Dashboard (`dashboard.py`)**
   - A modern, light-toned, professional interface to filter and interact with the dataset.
   - Dynamic filtering by **Task Type** and **Grade**.
   - Real-time key metrics display (Avg Quality Score, Avg Hallucination Risk, etc.).
   - Visualizes distributions and gives users the ability to download filtered datasets straight to an Excel file.

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed along with the required packages:
```bash
pip install pandas plotly seaborn matplotlib streamlit openpyxl nbformat
```

### Running the Dashboard
To start the interactive Streamlit dashboard, open your terminal, navigate to the project directory, and run:
```bash
streamlit run dashboard.py
```
This will automatically open the dashboard in your default web browser!

---

## 📸 Adding Images and Videos to this README

Yes! You can definitely add images and videos directly into this `README.md` file.

**For Images:**
You can use standard Markdown syntax to display an image (like screenshots of your dashboard or graphs). 
If you have an image called `dashboard_screenshot.png` in the same folder, you display it like this:
```markdown
![Dashboard Screenshot](dashboard_screenshot.png)
```

**For Videos:**
GitHub's markdown viewer allows you to embed video files (like `.mp4` or `.mov`). The easiest way to add a video to a GitHub README is to simply **drag and drop** the video file directly into the GitHub text editor when editing the file on the website. GitHub will automatically upload it and generate the code for you!

If you are hosting a video on YouTube or another platform, you can link it with an image thumbnail like this:
```markdown
[![Watch the video](thumbnail.png)](https://youtu.be/your_video_id_here)
```
