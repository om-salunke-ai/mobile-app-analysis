# Mobile App Preferences Analysis

An interactive Streamlit dashboard for exploring mobile-app usage patterns reported by students. The project demonstrates data cleaning, descriptive analysis, and visualisation with Python.

## Features

- Browse and filter the survey dataset by gender
- Visualise app, device, and daily-usage distributions
- Compare reported app preferences across gender groups
- Generate summary metrics from the dataset
- Use an interactive daily screen-time calculator

## Technology

- Python
- Streamlit
- pandas
- CSV data exported from Google Forms

## Run locally

Prerequisites: Python 3.10 or later.

```bash
git clone https://github.com/om-salunke-ai/mobile-app-analysis.git
cd mobile-app-analysis
pip install -r requirements.txt
python -m streamlit run app.py
```

The application opens at `http://localhost:8501`.

## Data and limitations

The included dataset is a small educational survey sample. Response timestamps have been removed, and findings should not be treated as representative of a wider population.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
