import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style="dark")


def load_data(file_path):
    """Load the data from a CSV file."""
    data = pd.read_csv(file_path)
    return data


def clean_data(data):
    """Clean the data."""
    data["yr"] = data["yr"].replace({0: 2011, 1: 2012})

    season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
    data["season"] = data["season"].replace(season_mapping)

    weather_mapping = {
        1: "Clear/Cloudy",
        2: "Mist/Cloudy",
        3: "Light Snow/Light Rain/Cloudy",
        4: "Extreme Weather",
    }
    data["weathersit"] = data["weathersit"].replace(weather_mapping)

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
    data["mnth"] = data["mnth"].replace(month_mapping)

    weekday_mapping = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
    }
    data["weekday"] = data["weekday"].replace(weekday_mapping)

    return data


def display_data(data):
    """Display the DataFrame."""
    st.write(data)


def main():
    """Main function."""
    st.title("Data Dashboard")

    # Load data
    file_path = (
        r"C:\Users\rafii\Documents\Bangkit\Assesment\Analisis Data\dashboard\day.csv"
    )
    data = load_data(file_path)

    # Clean data
    cleaned_data = clean_data(data)

    # Display cleaned data
    st.header("Cleaned Data")
    display_data(cleaned_data)


if __name__ == "__main__":
    main()
