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


def map_yr_column(cleaned_day):
    """Map values in 'yr' column."""
    return cleaned_day["yr"].replace({0: 2011, 1: 2012})


def map_season_column(cleaned_day):
    """Map values in 'season' column."""
    season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
    return cleaned_day["season"].replace(season_mapping)


def map_weathersit_column(cleaned_day):
    """Map values in 'weathersit' column."""
    weather_mapping = {
        1: "Clear/Cloudy",
        2: "Mist/Cloudy",
        3: "Light Snow/Light Rain/Cloudy",
        4: "Extreme Weather",
    }
    return cleaned_day["weathersit"].replace(weather_mapping)


def map_month_column(cleaned_day):
    """Map values in 'mnth' column."""
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
    return cleaned_day["mnth"].replace(month_mapping)


def map_weekday_column(cleaned_day):
    """Map values in 'weekday' column."""
    weekday_mapping = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
    }
    return cleaned_day["weekday"].replace(weekday_mapping)


def main():
    """Main function."""
    st.title("Data Dashboard")

    # Map columns
    cleaned_day["yr"] = map_yr_column(cleaned_day)
    cleaned_day["season"] = map_season_column(cleaned_day)
    cleaned_day["weathersit"] = map_weathersit_column(cleaned_day)
    cleaned_day["mnth"] = map_month_column(cleaned_day)
    cleaned_day["weekday"] = map_weekday_column(cleaned_day)

    # Filter data for holiday and workingday
    holiday = cleaned_day[
        (cleaned_day["workingday"] == 0) | (cleaned_day["holiday"] == 1)
    ]["cnt"]
    workingday = cleaned_day[(cleaned_day["workingday"] == 1)]["cnt"]

    # Display cleaned data
    st.header("Cleaned Data")
    st.write(cleaned_day)

    # Descriptive statistics for holiday
    st.header("Descriptive Statistics for Holiday")
    st.write(holiday.describe())

    # Descriptive statistics for workingday
    st.header("Descriptive Statistics for Workingday")
    st.write(workingday.describe())

    # Plot bar for mean bike rental count by day type
    st.header("Visualisasi Bar Plot Rata-rata Peminjaman Sepeda Menurut Tipe Hari")
    st.write(workingday.describe())
    plt.figure(figsize=(8, 6))
    sns.barplot(x=["Holiday", "Workingday"], y=[holiday.mean(), workingday.mean()])
    st.set_option("deprecation.showPyplotGlobalUse", False)
    plt.xlabel("Day Type")
    plt.ylabel("Mean")
    plt.title("Mean Bike Rental Count by Day Type")
    st.pyplot()


if __name__ == "__main__":
    main()
