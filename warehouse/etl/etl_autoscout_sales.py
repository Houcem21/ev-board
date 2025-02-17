import pandas as pd

# Auto scout represents the sales
# Load the data
car_sales = pd.read_csv("../raw_data/autoscout24-germany-dataset.csv")

# Use only the useful data for us
# which are the electric or hybrid cars
electric_car_sales = car_sales[car_sales['fuel'].str.lower().str.contains("electric", na=False)]
# str.lower.str seems counterintuitive but it's a thing

# Standardize the make and model column names
electric_car_sales['make'] = electric_car_sales['make'].str.lower()
electric_car_sales['model'] = electric_car_sales['model'].str.lower()
# I'm done with uppercase values


# Handle missing values
# This is a lot easier than the charging data
# Data quality is important fr
electric_car_sales['make'].fillna("unknown make", inplace=True)
electric_car_sales['model'].fillna("unknown model", inplace=True)
electric_car_sales['price'].fillna(0, inplace=True)
electric_car_sales['mileage'].fillna(0, inplace=True)
# One can go about the numerical columns in many ways
# but I'm just gonna fill them with 0 for now
electric_car_sales['fuel'].fillna("unknown fuel", inplace=True)
electric_car_sales['gear'].fillna("unknown gear", inplace=True)
# Once again, this can and should go on

# Convert data types
# You will not believe it but this failed miserably
# apparently the data is not as clean as I thought
electric_car_sales['price'] = pd.to_numeric(electric_car_sales['price'], errors='coerce').fillna(0)
electric_car_sales['mileage'] = pd.to_numeric(electric_car_sales['mileage'], errors='coerce').fillna(0).astype(int)
electric_car_sales['hp'] = pd.to_numeric(electric_car_sales['hp'], errors='coerce').fillna(0).astype(int)
electric_car_sales['year'] = pd.to_numeric(electric_car_sales['year'], errors='coerce').fillna(0).astype(int)
# after failing simple astype, we're using this fancy to_numeric
# As for the columns chosen, these seem relevant enough

# Filter invalid data
car_sales = car_sales[car_sales['price'] > 0]
# again, i have not looked too long at the data
# but im sure free cars are a no no

# Remove duplicates
electric_car_sales.drop_duplicates(subset=['make', 'model', 'fuel', 'price', 'year'], inplace=True)
# idk what's wrong with a simple drop_duplicates
# but I'm sure there's a reason for this subset thing

# Save the data to processed data directory
electric_car_sales.to_csv("../processed_data/electric_car_sales.csv", index=False)
print("Data processing for raw autoscout24-germany-dataset.csv is done. The processed data is saved to processed_data/electric_car_sales.csv")