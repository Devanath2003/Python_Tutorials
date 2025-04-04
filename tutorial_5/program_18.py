import pandas as pd
import matplotlib.pyplot as plt
import io

weather_csv_data = """date,temperature,humidity,windSpeed,precipitationType,place,weather
2023-01-01,25,80,10,Rain,Mumbai,Rainy
2023-01-02,27,75,8,None,Mumbai,Cloudy
2023-01-03,30,60,12,None,Delhi,Sunny
2023-01-04,22,85,15,Rain,Delhi,Rainy
2023-01-05,28,70,10,None,Chennai,Cloudy
"""
csv_filename = "weather.csv"
with open(csv_filename, 'w') as f:
    f.write(weather_csv_data)
print(f"Dummy file '{csv_filename}' created.")

try:
    df_weather = pd.read_csv(csv_filename)
    df_weather['date'] = pd.to_datetime(df_weather['date'])
    print("\nWeather Data:")
    print(df_weather)

    print("\n1) First 10 rows:")
    print(df_weather.head(10))

    max_temp = df_weather['temperature'].max()
    min_temp = df_weather['temperature'].min()
    print(f"\n2) Maximum Temperature: {max_temp}°C")
    print(f"   Minimum Temperature: {min_temp}°C")

    places_temp_lt_28 = df_weather[df_weather['temperature'] < 28]['place'].unique()
    print("\n3) Places with temperature < 28°C:")
    print(list(places_temp_lt_28))

    places_cloudy = df_weather[df_weather['weather'] == 'Cloudy']['place'].unique()
    print("\n4) Places with 'Cloudy' weather:")
    print(list(places_cloudy))

    weather_frequency = df_weather['weather'].value_counts().sort_index()
    print("\n5) Frequency of each weather type (sorted alphabetically):")
    print(weather_frequency)

    plt.figure(figsize=(12, 6))
    date_labels = df_weather['date'].dt.strftime('%Y-%m-%d')
    plt.bar(date_labels, df_weather['temperature'], color='lightblue')
    plt.title('Temperature Each Day')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--')
    print("\n6) Displaying Bar Plot for Temperature per Day...")
    plt.show()

except FileNotFoundError:
    print(f"Error: The file '{csv_filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")