import os
import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../warehouse/processed_data/"))

def load_electric_sales():
    df = pd.read_csv(os.path.join(BASE_DIR, 'electric_car_sales.csv'))  

    # Convert year to num just in case
    df['year'] = pd.to_numeric(df['year'], errors='coerce')

    # Convert price to num, drop rows where price couldn't be converted
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df.dropna(subset=['price'], inplace=True)  # Remove rows where price couldn't be converted

    # Just making sure here
    print("Unique price values:", df['price'].unique()[:20])
    print("Unique year values:", df['year'].unique()[:20]) 

    return df


def load_charging_stations():
    df = pd.read_csv(os.path.join(BASE_DIR, 'charging_data.csv'))   
    df['commissioning_date'] = pd.to_datetime(df['commissioning_date'], errors='coerce')
    df['year'] = df['commissioning_date'].dt.year 
    return df


def load_yearly_trends():
    df = pd.read_csv(os.path.join(BASE_DIR, 'yearly_trends.csv')) 

    # Ensure 'sales' and 'stations' are numeric, filling missing values with 0
    df['electric_car_sales_count'] = pd.to_numeric(df['electric_car_sales_count'], errors='coerce').fillna(0)
    df['charging_station_count'] = pd.to_numeric(df['charging_station_count'], errors='coerce').fillna(0)

    return df
