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

st.write(cleaned_day)
