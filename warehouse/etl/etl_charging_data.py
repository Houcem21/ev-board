import pandas as pd

# Load the data
charging_data = pd.read_csv("../raw_data/charging_data.csv")
# Istg I misspelt charging as chargin like 3 times now

# rename the columns since some
# of them are in german lauchen 🇩🇪 lauchen 
charging_data.columns = [
    "id", "operator", "station_type", "num_charging_points", "connection_power", 
    "connector_type1", "connector_type2", "connector_type3", "connector_type4", 
    "p1_kw", "p2_kw", "p3_kw", "p4_kw", "district_city", "location", "postal_code", 
    "street", "house_number", "address_addition", "commissioning_date", 
    "latitude", "longitude"
]

# Let's handle missing values
charging_data["operator"].fillna("Unknown Operator", inplace=True)
charging_data["station_type"].fillna("Unknown Station Type", inplace=True)
charging_data["num_charging_points"].fillna(0, inplace=True)
charging_data["connection_power"].fillna(0, inplace=True)
charging_data["postal_code"].fillna("Unknown Postal Code", inplace=True)

# There are too many columns and idk which to use later on so
# I'll just comment this out. the list goes on though
# charging_data["street"].fillna("Unknown Street", inplace=True)
# charging_data["house_number"].fillna("Unknown House Number", inplace=True)
# charging_data["address_addition"].fillna("Unknown Address Addition", inplace=True)
# charging_data["commissioning_date"].fillna("Unknown Commissioning Date", inplace=True)
# etc etc

charging_data["latitude"].fillna(0, inplace=True)
charging_data["longitude"].fillna(0, inplace=True)
# idk about longitude and latitude being valid geographically 
# but I'm leaving this as is

# You would think there's a mapping function for this
# about which, idk

# Convert data types
charging_data["num_charging_points"] = charging_data["num_charging_points"].astype(int)
charging_data["connection_power"] = charging_data["connection_power"].astype(float)
# This should allow for calculations later on

# Handle dates
charging_data["commissioning_date"] = pd.to_datetime(charging_data["commissioning_date"], format="%Y-%m-%d", errors="coerce")
# if this works hallelujah

# Remove duplicates
charging_data.drop_duplicates(inplace=True)
# this dataset seemed clean enough so I'm not sure if this is necessary
# meh

# Save the data to processed data directory
charging_data.to_csv("../processed_data/charging_data.csv", index=False)
print("Data processing for raw charging_data.csv is done. The processed data is saved to processed_data/charging_data.csv")

# I just saw the processed data
# this is lacking... a lot