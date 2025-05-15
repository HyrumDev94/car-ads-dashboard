import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title & intro
st.title("🚗 Car Ads Dashboard")
st.write("Explore vehicle listings by type, fuel, and price. Use the dropdown to filter by vehicle type and analyze trends.")

# Load data
df = pd.read_csv("vehicles_us.csv")

# Dropdown filter
car_type = st.selectbox("Choose a vehicle type:", df['type'].unique())
filtered_df = df[df['type'] == car_type]

# Data table
st.header("📊 Data Table")
st.write("Filtered data by type:")
st.dataframe(filtered_df.head())

# Histogram
st.header("📉 Price Distribution Histogram")
fig, ax = plt.subplots()
filtered_df['price'].hist(bins=30, ax=ax)
st.pyplot(fig)

# Boxplot
st.header("📈 Boxplot of Price by Fuel Type")
fig2, ax2 = plt.subplots()
sns.boxplot(x='fuel', y='price', data=filtered_df, ax=ax2)
st.pyplot(fig2)
