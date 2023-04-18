import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Load data
weather = pd.read_csv("C:/Users/achavez1/Desktop/Python/Problem Sets/pythonProject/Data/boston_weather_data.csv", parse_dates=['time'])

# User input
prompt = st.text_input("Please enter which day you would like to look at in yyyy-mm-dd format: ")

# Filter data by date range
date = pd.to_datetime(prompt)
start_date = date.date()
end_date = start_date + pd.Timedelta(days=3)  # Show next 3 days
data = weather[(weather['time'].dt.date >= start_date) & (weather['time'].dt.date <= end_date)]

# dictionaries of clothing and accessories ex: print(outfits['Summer'])
outfits = {
    'Summer': ['shorts', 't-shirt', 'tank tops', 'flip flops'],     # above 21 celsius
    'Breezy': ['jeans', 'boots', 'sweater', 'light_jacket'],        # between 15 and 21 celsius
    'Cold': ['coat', 'turtleneck', 'sweatpants'],                   # between 0 and 15 celsius
    'Winter': ['puffer jacket', 'scarf', 'gloves', 'boots', 'thermals'],    # below 0 celsius
}

# Display tavg for the day(s)
if not data.empty:
    tavg = data['tavg'].mean()
    st.write(f"The tavg for {start_date} to {end_date} is: {tavg:.1f} F")

    # Suggest outfit based on temperature range
    if tavg > 21:
        outfit_type = 'Summer'
    elif tavg >= 15:
        outfit_type = 'Breezy'
    elif tavg >= 0:
        outfit_type = 'Cold'
    else:
        outfit_type = 'Winter'
    st.write(f"Suggested outfit for the temperature range: {outfit_type}")
    st.write(f"Outfit: {', '.join(outfits[outfit_type])}")

    # Plot temperature data
    fig, ax = plt.subplots()
    ax.plot(data['time'], data['tavg'])
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperature (F)')
    ax.set_title(f'Temperature from {start_date} to {end_date}')
    st.pyplot(fig)
else:
    st.write("No data available for the selected date range.")
