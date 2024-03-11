import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style="dark")

day = pd.read_csv(
    r"C:\Users\rafii\Documents\Bangkit\Assesment\Analisis Data\dashboard\day.csv"
)
day.head()

cleaned_day = day.drop(
    labels=["instant", "windspeed", "temp", "atemp", "hum", "casual"], axis=1
)

cleaned_day["yr"] = cleaned_day["yr"].replace({0: 2011, 1: 2012})

season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
cleaned_day["season"] = cleaned_day["season"].replace(season_mapping)

weather_mapping = {
    1: "Clear/Cloudy",
    2: "Mist/Cloudy",
    3: "Light Snow/Light Rain/Cloudy",
    4: "Extreme Weather",
}
cleaned_day["weathersit"] = cleaned_day["weathersit"].replace(weather_mapping)

month_mapping = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}
cleaned_day["mnth"] = cleaned_day["mnth"].replace(month_mapping)

weekday_mapping = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
}
cleaned_day["weekday"] = cleaned_day["weekday"].replace(weekday_mapping)

holiday = cleaned_day[(cleaned_day["workingday"] == 0) | (cleaned_day["holiday"] == 1)][
    "cnt"
]
workingday = cleaned_day[(cleaned_day["workingday"] == 1)]["cnt"]

# Menampilkan deskripsi statistik untuk hari libur
st.write("Deskripsi Statistik untuk Hari Libur:")
st.write(holiday.describe())

# Menampilkan deskripsi statistik untuk hari kerja
st.write("Deskripsi Statistik untuk Hari Kerja:")
st.write(workingday.describe())


st.write(cleaned_day)
