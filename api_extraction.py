import requests
import datetime
import pandas as pd

# Function to extract weather data from OpenWeather API
def extract_weather_data(cities):
    base_url = "http://************"
    api_key = "*************"  # Your API key
    weather_data = []
    
    for city in cities:
        complete_url =f"{base_url}q={city}&appid={api_key}&units=metric"
        try:
            response = requests.get(complete_url, timeout=10)
            data = response.json()
            
            if data["cod"] != "404":
                weather_data.append({
                    "City": city,
                    "Temperature (°C)": data["main"]["temp"],
                    "Humidity (%)": data["main"]["humidity"],
                    "Pressure (hPa)": data["main"]["pressure"],
                    "Wind Speed (m/s)": data["wind"]["speed"],
                    "Weather": data["weather"][0]["main"],
                    "Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
        except Exception as e:
            print(f"Error fetching data for {city}: {str(e)}")
    
    return pd.DataFrame(weather_data)

# Example cities for weather data extraction
cities = ["Lahore", "Karachi", "Islamabad", "Peshawar", "Quetta"]
print("Fetching weather data...")
weather_df = extract_weather_data(cities)

# Display the fetched data
if not weather_df.empty:
    print("\nCurrent Weather Data:")
    print(weather_df.to_string(index=False))
else:
    print("No weather data retrieved")
