import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

weather = pd.read_csv("C:/Users/achavez1/Desktop/Python/Problem Sets/pythonProject/Data/boston_weather_data.csv", parse_dates=['time'])
# print(weather.head())

prompt = st.text_input("Please enter which day you would like to look at in yyyy-mm-dd format: ")

date = pd.to_datetime(prompt)

# Converts the chosen day into datetime
chosen_day = weather[weather['time'].dt.date == date.date()]

# dictionary of clothing and accessories ex: print(outfits['Summer'])
outfits = {
    'Summer': ['shorts', 't-shirt', 'tank tops', 'flip flops'],     # above 21 celsius
    'Breezy': ['jeans', 'boots', 'sweater', 'light_jacket'],        # between 15 and 21 celsius
    'Cold': ['coat', 'turtleneck', 'sweatpants'],                   # between 0 and 15 celsius
    'Winter': ['puffer jacket', 'scarf', 'gloves', 'boots', 'thermals'],    # below 0 celsius
}

accessory = {
    'Rain': ['umbrella', 'rain coat', 'boots'],                     # precp is greater than 35
    'Sunny': ['sunglasses', 'cap']                                  # precp is equal to 0
}

# If there is no data for the chosen date, we print an error
if chosen_day.empty:
    st.write("No data available for the chosen date.")
else:
    tavg = chosen_day['tavg'].values[0]
    precp = chosen_day['prcp'].values[0]

    # This gives us the forecast for the next three days based on the chosen_day variable
    next_three_days = pd.date_range(date + pd.Timedelta(days=1), date + pd.Timedelta(days=4), freq='D')

    days = []
    temps = []
    for day in next_three_days:
        day_data = weather[weather['time'].dt.date == day.date()]
        if day_data.empty:
            st.write(f":No data available for {day.date()}.")
        else:
            tavg = day_data['tavg'].values[0]
            st.write(f"The average temperature for {day.date()} is predicted to be {tavg:.1f} degrees Celsius")
            st.write(f"The precipitation for {day.date()} is predicted to be {precp:.2f} mm")
            days.append(day)
            temps.append(tavg)

    if precp > 35:
        accessory_list = accessory['Rain']
    else:
        accessory_list = accessory['Sunny']

    if tavg >= 21:
        outfit = outfits['Summer']
    elif tavg >= 15 and tavg < 21:
        outfit = outfits['Breezy']
    elif tavg >= 0 and tavg < 15:
        outfit = outfits['Cold']
    elif tavg < 0:
        outfit = outfits['Winter']

    st.write(f"The average temperature for {date.date()} was {tavg:.1f} degrees Celsius.")
    st.write(f"You should wear: {', '.join(outfit)}")

plt.style.use('ggplot')
plt.plot(days, temps)
plt.title('Next Three Days Forecast')
plt.xlabel('Date')
plt.ylabel('Temperature (C)')
plt.show()
