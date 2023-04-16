import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

weather = pd.read_csv("C:/Users/achavez1/Desktop/Python/Problem Sets/pythonProject/Data/boston_weather_data.csv", parse_dates=['time'])
# print(weather.head())

prompt = input("Please enter which day you would like to look at in yyyy-mm-dd format: ")

date = pd.to_datetime(prompt)

# Converts the chosen day into datetime
chosen_day = weather[weather['time'].dt.date == date.date()]

# dictionary of clothing ex: print(outfits['Summer'])
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
"""
for value in chosen_day:
    if value[1]:
        avg_t = value[1] * 9/5 + 32
    elif value[2]:
        min_t = value[2] * 9/5 + 32
    elif value[3]:
        max_t = value[3] * 9/5 + 32
    elif value[4]:
        precp = value[4] / 25.4
    elif value[6]:
        wind_spd = value[6] / 1.609
"""

if chosen_day.empty:
    print("No data available for the chosen date.")
else:
    tavg = chosen_day['tavg'].values[0]

    if tavg >= 21:
        outfit = outfits['Summer']
    elif tavg >= 15 and tavg < 21:
        outfit = outfits['Breezy']
    elif tavg >= 0 and tavg < 15:
        outfit = outfits['Cold']
    elif tavg < 0:
        outfit = outfits['Winter']
    print(f"The average temperature for {date.date()} was {tavg:.1f} degrees Celsius.")
    print(f"You should wear: {', '.join(outfit)}")
