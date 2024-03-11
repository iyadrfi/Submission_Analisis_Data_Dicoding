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
    st.title("Proyek Akhir Dicoding : Belajar Analisis Data Dengan Python")
    st.write("- Nama: [Rafi Iyad Madani Chaidir]")
    st.write("- Email: [rafiiyad2004@gmail.com]")
    st.write("- [rafi_iyad]")

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
    st.header("Menentukan Pertanyaan Bisnis")
    st.write(
        "- Apakah ada perbedaan dalam rata-rata peminjaman sepeda pada hari libur dibandingkan dengan hari biasa ?"
    )
    st.write(
        "- Apakah terdapat perbedaan dalam pola peminjaman sepeda antara musim-musim tertentu?"
    )
    st.write("-  Bagaimana cuaca memengaruhi jumlah peminjaman sepeda?")

    # Display cleaned data
    st.header("Import Data")
    st.write(day)

    # Display cleaned data
    st.header("Cleaned Data")
    st.write(cleaned_day)

    # Descriptive statistics for holiday
    st.header("Descriptive Statistics for Holiday")
    st.write(holiday.describe())

    # Descriptive statistics for workingday
    st.header("Descriptive Statistics for Workingday")
    st.write(workingday.describe())

    st.header("Pertanyaan 1 : Rata-rata Peminjaman Sepeda Menurut Tipe Hari")
    st.write(
        "Dari hasil analisis, terlihat bahwa rata-rata peminjaman sepeda pada hari biasa (non-holiday) lebih tinggi dibandingkan dengan hari libur (holiday). Hal ini menunjukkan bahwa mayoritas peminjaman sepeda terjadi pada hari-hari biasa, yang mungkin disebabkan oleh aktivitas sehari-hari seperti pergi ke tempat kerja atau sekolah. Oleh karena itu, dapat disimpulkan bahwa hari biasa cenderung menjadi periode di mana peminjaman sepeda paling banyak terjadi"
    )
    plt.figure(figsize=(8, 6))
    sns.barplot(
        x=["Hari Libur", "Hari Kerja/Biasa"], y=[holiday.mean(), workingday.mean()]
    )
    plt.xlabel("Tipe Hari")
    plt.ylabel("Mean")
    plt.title("Jumlah Rata-rata Peminjaman Sepeda Berdasarkan Tipe Hari")
    st.pyplot()

    st.header(
        "Pertanyaan 2 : Perbedaan Dalam Pola Peminjaman Sepeda Antara Musim-Musim Tertentu?"
    )
    st.write(
        "Hasil Analisis mengatakan bahwa musim memiliki pengaruh signifikan terhadap jumlah peminjaman sepeda. Musim gugur menunjukkan rata-rata peminjaman sepeda tertinggi, diikuti oleh musim panas, musim dingin, dan musim semi secara berurutan. Hal ini menunjukkan bahwa perubahan musim memengaruhi minat masyarakat dalam menggunakan sepeda, dengan tingkat peminjaman yang lebih tinggi terjadi pada musim yang lebih hangat dan cerah. Dengan demikian, kesimpulan ini memberitahu pentingnya faktor cuaca dan musim dalam memprediksi pola peminjaman sepeda."
    )

    plt.figure(figsize=(10, 6))
    sns.barplot(x="season", y="cnt", data=cleaned_day, estimator="mean")
    plt.title("Jumlah Rata-rata Peminjaman Sepeda Berdasarkan Musim")
    plt.xlabel("Musim")
    plt.ylabel("Mean")
    plt.xticks([0, 1, 2, 3], ["Spring", "Summer", "Fall", "Winter"])
    st.pyplot()

    st.header("Pertanyaan 3 : Bagaimana cuaca memengaruhi jumlah peminjaman sepeda?")
    st.write(
        "Dengan analisis yang telah dilakukan menunjukkan bahwa kondisi cuaca memiliki pengaruh yang signifikan terhadap jumlah total peminjaman sepeda. Kondisi cuaca yang baik, seperti cuaca cerah dan bersih, cenderung meningkatkan jumlah peminjaman sepeda, sedangkan kondisi cuaca buruk, seperti hujan atau salju, cenderung mengurangi jumlah peminjaman sepeda bahkan tidak terjadi sama sekali peminjaman sepeda. Hal ini menunjukkan bahwa keputusan untuk meminjam sepeda dipengaruhi oleh kondisi cuaca saat itu."
    )

    plt.figure(figsize=(10, 6))
    sns.pointplot(x="weathersit", y="cnt", data=cleaned_day, errorbar=None)
    plt.xlabel("Weather Situation")
    plt.ylabel("Average Bike Rental Count")
    plt.title("Average Bike Rental Count by Weather Situation")
    plt.xticks(
        [0, 1, 2, 3],
        ["Clear/Cloudy", "Mist/Cloudy", "Light Snow/Rain", "Heavy Rain/Snow"],
    )
    st.pyplot()


if __name__ == "__main__":
    main()
