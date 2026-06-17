# mobile-app-analysis
Mobile app usage analysis among students using Python and Streamlit


# Mobile App Preferences Analysis

A data analysis web app I built using Python and Streamlit that 
explores mobile app usage patterns among students.

The data was collected via Google Forms from real students, then 
cleaned and visualized through an interactive multi-page dashboard.

---

## What it does

The app has 5 pages:

- **Home** — project overview
- **Dataset Viewer** — browse the raw data, filter by gender
- **Dashboard** — bar charts for most-used apps, phone types, 
  usage hours, and a gender vs app comparison table
- **Insights** — auto-generated text findings from the dataset 
  (top app, average usage, Android vs iPhone split)
- **Usage Calculator** — enter your daily screen time and get 
  a health-level rating (Low / Moderate / High)

---

## Built with

- **Python** + **Streamlit** — app structure and UI
- **Pandas** — data cleaning and analysis
- **Google Forms** — data collection from students
- **CSV file** — dataset storage

---

## Run it locally

```bash
git clone https://github.com/om-salunke-ai/mobile-app-analysis.git
cd mobile-app-analysis
pip install streamlit pandas
python -m streamlit run app.py
```

Opens at `http://localhost:8501`

---

---

## Key findings

- Most students use Android phones
- Instagram and YouTube dominate as most-used apps
- Average daily usage is around 3 hours
- Main reasons for app usage are communication and entertainment

---

## About

Made by **Om Salunke** — CS student at Vishwakarma University, Pune.  
This was a second Python project where I worked with real survey 
data instead of dummy data — cleaning messy Google Form responses 
and turning them into actual charts was the main challenge.

GitHub: [@om-salunke-ai](https://github.com/om-salunke-ai)
