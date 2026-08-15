import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mobile App Analysis", layout="wide")

# Load and clean data.
df = pd.read_csv("mobile_app_data.csv")
df.columns = df.columns.str.strip()
df = df.rename(
    columns={
        "What is your age?": "Age",
        "What is your gender?": "Gender",
        "3)Which mobile phone do you use?": "Phone Type",
        "How many hours do you use your phone daily?": "Usage Hours",
        "Which app do you use the most?": "Most-Used App",
        "Reason of using that": "Reason",
    }
)

if "Usage Hours" in df.columns:
    def parse_hours(value):
        if pd.isna(value):
            return 0.0
        value = str(value).lower()
        if "1-2" in value:
            return 1.5
        if "2-4" in value:
            return 3.0
        if "more than 4" in value:
            return 5.0
        if "less than 1" in value:
            return 0.5
        return 0.0

    df["Usage Hours Numeric"] = df["Usage Hours"].apply(parse_hours)

app_counts = pd.Series(dtype="int64")
if "Most-Used App" in df.columns:
    app_counts = (
        df["Most-Used App"]
        .dropna()
        .astype(str)
        .str.split(",")
        .explode()
        .str.strip()
        .replace("", pd.NA)
        .dropna()
        .value_counts()
    )

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Dataset Viewer", "Dashboard", "Insights", "Usage Calculator"],
)

if page == "Home":
    st.title("Mobile App Preferences Analysis")
    st.write(
        "Explore a small student survey dataset through interactive charts, "
        "comparisons, and summary metrics."
    )

elif page == "Dataset Viewer":
    st.title("Dataset Viewer")

    if "Gender" in df.columns:
        gender_filter = st.selectbox("Select Gender", ["All", *sorted(df["Gender"].dropna().unique())])
        displayed_data = df if gender_filter == "All" else df[df["Gender"] == gender_filter]
        st.dataframe(displayed_data, use_container_width=True)
    else:
        st.dataframe(df, use_container_width=True)

elif page == "Dashboard":
    st.title("Dashboard")

    first_column, second_column = st.columns(2)

    with first_column:
        if not app_counts.empty:
            st.subheader("Reported Most-Used Apps")
            st.bar_chart(app_counts)

    with second_column:
        if "Phone Type" in df.columns:
            st.subheader("Phone Type Distribution")
            st.bar_chart(df["Phone Type"].value_counts())

    if "Usage Hours" in df.columns:
        st.subheader("Daily Usage Hours")
        st.bar_chart(df["Usage Hours"].value_counts())

    if "Gender" in df.columns and "Most-Used App" in df.columns:
        st.subheader("Comparison: Gender and Reported App Preferences")
        gender_apps = (
            df[["Gender", "Most-Used App"]]
            .dropna()
            .assign(**{"Most-Used App": lambda data: data["Most-Used App"].astype(str).str.split(",")})
            .explode("Most-Used App")
        )
        gender_apps["Most-Used App"] = gender_apps["Most-Used App"].str.strip()
        gender_app = pd.crosstab(gender_apps["Gender"], gender_apps["Most-Used App"])
        st.dataframe(gender_app, use_container_width=True)

    numeric_columns = df.select_dtypes(include=["int64", "float64"])
    if len(numeric_columns.columns) > 1:
        st.subheader("Correlation Analysis")
        st.dataframe(numeric_columns.corr(), use_container_width=True)

elif page == "Insights":
    st.title("Insights")
    total_students = len(df)

    if "Phone Type" in df.columns:
        android_users = (df["Phone Type"] == "Android").sum()
        st.write(f"• {android_users} of {total_students} respondents reported using Android phones.")

    if not app_counts.empty:
        st.write(f"• The most frequently reported app is {app_counts.index[0]}.")

    if "Usage Hours Numeric" in df.columns:
        average_usage = df["Usage Hours Numeric"].mean()
        st.write(f"• Average reported daily usage is {average_usage:.2f} hours.")

elif page == "Usage Calculator":
    st.title("Mobile Usage Level Calculator")
    hours = st.slider("Select your daily usage hours", 0, 10, 2)

    if hours <= 2:
        st.success("Low usage level — a balanced range.")
    elif hours <= 4:
        st.info("Moderate usage level — consider regular breaks.")
    else:
        st.warning("High usage level — consider reducing screen time and taking regular breaks.")
