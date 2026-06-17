import streamlit as st
import pandas as pd

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Mobile App Analysis", layout="wide")

# ------------------ LOAD DATA ------------------
df = pd.read_csv("mobile_app_data.csv")

# Clean column names (remove extra spaces)
df.columns = df.columns.str.strip()

# Rename Google Form columns to simple names
df.rename(columns={
    "What is your age?": "Age",
    "What is your gender?": "Gender",
    "Which mobile phone do you use?": "Phone Type",
    "How many hours do you use your phone daily?": "Usage Hours",
    "Which app do you use the most?": "Most-Used App",
    "Reason of using that": "Reason"
}, inplace=True)

if "Usage Hours" in df.columns:
    def parse_hours(val):
        if pd.isna(val): return 0.0
        val_str = str(val).lower()
        if "1-2" in val_str: return 1.5
        elif "2-4" in val_str: return 3.0
        elif "more than 4" in val_str: return 5.0
        elif "less than 1" in val_str: return 0.5
        return 0.0
    df["Usage Hours Numeric"] = df["Usage Hours"].apply(parse_hours)

# ------------------ SIDEBAR ------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Dataset Viewer", "Dashboard", "Insights", "Usage Calculator"]
)

# ------------------ HOME PAGE ------------------
if page == "Home":
    st.title("Mobile App Preferences Analysis")
    st.write("""
    This project analyzes mobile app usage patterns among students.
    It includes data visualization, comparison analysis, correlation analysis,
    and an interactive usage level calculator.
    """)

# ------------------ DATASET VIEWER ------------------
elif page == "Dataset Viewer":
    st.title("Dataset Viewer")

    if "Gender" in df.columns:
        gender_filter = st.selectbox(
            "Select Gender",
            ["All"] + list(df["Gender"].unique())
        )

        if gender_filter != "All":
            filtered_df = df[df["Gender"] == gender_filter]
            st.write(filtered_df)
        else:
            st.write(df)
    else:
        st.write(df)

# ------------------ DASHBOARD ------------------
elif page == "Dashboard":
    st.title("Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        if "Most-Used App" in df.columns:
            st.subheader("Most Used Apps")
            st.bar_chart(df["Most-Used App"].value_counts())

    with col2:
        if "Phone Type" in df.columns:
            st.subheader("Phone Type Distribution")
            st.bar_chart(df["Phone Type"].value_counts())

    if "Usage Hours" in df.columns:
        st.subheader("Daily Usage Hours")
        st.bar_chart(df["Usage Hours"].value_counts())

    # Gender vs App Comparison
    if "Gender" in df.columns and "Most-Used App" in df.columns:
        st.subheader("Comparison: Gender vs Most Used App")
        gender_app = pd.crosstab(df["Gender"], df["Most-Used App"])
        st.write(gender_app)
        st.bar_chart(gender_app)

    # Correlation Analysis
    numeric_columns = df.select_dtypes(include=['int64', 'float64'])

    if len(numeric_columns.columns) > 1:
        st.subheader("Correlation Analysis")
        correlation = numeric_columns.corr()
        st.write(correlation)

# ------------------ INSIGHTS ------------------
elif page == "Insights":
    st.title("Insights")

    total_students = len(df)

    if "Phone Type" in df.columns:
        android_users = df[df["Phone Type"] == "Android"].shape[0]
        st.write(f"• {android_users} out of {total_students} students use Android phones.")

    if "Most-Used App" in df.columns:
        top_app = df["Most-Used App"].value_counts().idxmax()
        st.write(f"• The most used app is {top_app}.")

    if "Usage Hours Numeric" in df.columns:
        avg_usage = df["Usage Hours Numeric"].mean()
        st.write(f"• Average daily usage is {round(avg_usage, 2)} hours.")

    st.write("• Students mainly use apps for communication and entertainment.")

# ------------------ USAGE CALCULATOR ------------------
elif page == "Usage Calculator":
    st.title("Mobile Usage Level Calculator")

    hours = st.slider("Select your daily usage hours", 0, 10, 2)

    if hours <= 2:
        st.success("Low Usage Level  Healthy balance.")
    elif hours <= 4:
        st.info("Moderate Usage  Acceptable level.")
    else:
        st.warning("High Usage  Try to reduce screen time.")

        # to run python -m streamlit run app.py
