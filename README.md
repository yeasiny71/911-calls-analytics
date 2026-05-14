# 911 Calls Analytics Project

## Project Overview

This project analyzes emergency 911 call data to identify patterns,
trends, and emergency distributions using exploratory data analysis
and time series visualization techniques.

The project focuses on:
- Data cleaning
- Feature engineering
- Time series analysis
- Heatmaps and visualizations
- Emergency category analysis

## Dataset

The dataset contains emergency 911 call records including:
- timestamp
- township
- zip code
- emergency title
- latitude and longitude

Dataset Source:
https://www.kaggle.com/mchirico/montcoalert

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Project Structure

```text
911-calls-analytics/
│
├── data/
│   ├── raw/
│   
│
├── notebooks/
│
├── src/
│
├── outputs/
│   ├── figures/
│   
│
├── dashboard/
│
├── README.md
├── requirements.txt
```
## Key Analysis Performed

### Feature Engineering
- Extracted Hour, Month, and Day of Week from timestamps
- Extracted emergency categories from title column

### Exploratory Data Analysis
- Emergency call distribution analysis
- Monthly and daily trend analysis
- Category-specific time series analysis

### Visualization
- Count plots
- Time series plots
- Heatmaps
## Installation

Clone the repository:

```bash
https://github.com/yeasiny71/911-calls-analytics.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```