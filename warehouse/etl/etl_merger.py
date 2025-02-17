import pandas as pd

# This is gonna be painful
# Load datasets
charging_data = pd.read_csv("../processed_data/charging_data.csv")
car_sales_data = pd.read_csv("../processed_data/electric_car_sales.csv")

# What we need to do is to find the yearly trends
# of electric car sales and charging stations
# and compare them side by side
# So we'll extract the year from the commissioning date in charging_data
# and group by year next to the electric car sales data
# and then merge them together 
# easy peasy; i have no clue what I'm doing

# Step 1: Process charging_data.csv
charging_data['commissioning_year'] = pd.to_datetime(charging_data['commissioning_date']).dt.year

charging_summary = charging_data.groupby('commissioning_year').agg({
    'id': 'count',  # Number of charging stations
    'num_charging_points': 'sum',  # Total charging points
    'connection_power': 'sum'  # Total connection power
}).rename(columns={
    'id': 'charging_station_count',
    'num_charging_points': 'total_charging_points',
    'connection_power': 'total_connection_power'
}).reset_index()
# This is the data we need for the comparison
# The kind of data to warehouse

# Step 2: Process car_sales.csv
# Filter for electric cars only
electric_cars = car_sales_data[car_sales_data['fuel'].str.contains('Electric', case=False)]
# We already did this but you never know

car_sales_summary = electric_cars.groupby('year').agg({
    'model': 'count'  # Number of electric cars sold
}).rename(columns={
    'model': 'electric_car_sales_count'
}).reset_index()

# Step 3: Merge datasets by year
merged_summary = pd.merge(
    car_sales_summary,
    charging_summary,
    left_on='year',
    right_on='commissioning_year',
    how='inner'
)
# This is sensitive stuff right here, modify with caution

# Save merged data for analysis
merged_summary.to_csv("../processed_data/yearly_trends.csv", index=False)

print("Yearly trends saved to processed_data/yearly_trends.csv")
print("\nKey Insights (Yearly Comparison):")
print(merged_summary.sort_values(by='year', ascending=True))
# Printing it out just makes it easier to view from the terminal
# I just saw it. THIS IS CLEANNN