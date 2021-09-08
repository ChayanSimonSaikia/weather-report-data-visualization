import csv
from datetime import date, datetime

filename = "data/sitka_weather_2018_simple.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Fetching high and low temperature and dates from the file
    highs, lows, dates = [], [], []
    for row in reader:
        high = int(row[5])
        low = int(row[6])
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        highs.append(high)
        lows.append(low)
        dates.append(current_date)
