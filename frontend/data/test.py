print("test")

# Just a helper function to test the data loading functions

import os
import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../warehouse/processed_data/"))

def load_electric_sales():
    df = pd.read_csv(os.path.join(BASE_DIR, 'electric_car_sales.csv'))  

    print("Unique price values:", df['price'].unique()[:20])
    print("Unique year values:", df['year'].unique()[:20]) 

    return df