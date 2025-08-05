import pandas as pd

# Function to clean and transform the weather data
def clean_weather_data(df):
    try:
        # Handle missing values safely
        df_cleaned = df.dropna().copy()
        
        # Convert the 'Time' column to datetime format
        df_cleaned['Time'] = pd.to_datetime(df_cleaned['Time'])
        
        # Temperature categories
        df_cleaned['Temp_Category'] = pd.cut(
            df_cleaned['Temperature (°C)'],
            bins=[-float('inf'), 0, 15, 25, 35, float('inf')],
            labels=['❄️ Freezing', '🧊 Cold', '😊 Pleasant', '🔥 Warm', '🥵 Hot']
        )
        
        # Wind categories
        df_cleaned['Wind_Category'] = pd.cut(
            df_cleaned['Wind Speed (m/s)'],
            bins=[0, 0.5, 3, 6, float('inf')],
            labels=['🍃 Calm', '🌬️ Breeze', '💨 Windy', '🌪️ Strong']
        )
        
        # Pressure conversion from hPa to kPa
        df_cleaned['Pressure (kPa)'] = round(df_cleaned['Pressure (hPa)'] / 10, 1)
        
        return df_cleaned
    
    except Exception as e:
        print(f"Error cleaning data: {str(e)}")
        return df

# Clean the extracted weather data
if not weather_df.empty:
    cleaned_weather_df = clean_weather_data(weather_df)
    print("\nTransformed Weather Data:")
    print(cleaned_weather_df.to_string(index=False))
else:
    print("No data to clean")
