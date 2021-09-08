import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = "data/sitka_weather_2018_simple.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Fetching high and low temperature and dates from the file
    highs, lows, dates = [], [], []
    for row in reader:
        high = int(row[5])
        low = int(row[6])
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        highs.append(high)
        lows.append(low)
        dates.append(current_date)
    
    # Visualization 
    plt.style.use('seaborn')
    fig, ax = plt.subplots()

    ax.plot(dates, highs, c="red", alpha=0.5)
    ax.plot(dates, lows, c="green", alpha=0.5)

    fig.autofmt_xdate()
    ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
    ax.set_title("Low and high temperatures in 2018", fontsize=24)
    ax.set_xlabel("Dates", fontsize=14)
    ax.set_ylabel("Temperature (F)", fontsize=14)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
    

