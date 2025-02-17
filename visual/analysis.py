# from config.db import get_db
# from utils.data_processing import fetch_products
# from utils.visualisation import plot_quantity_distribution

# # Get db connection
# # I called the dataset products bc
# # at this point I haven't decided on
# # what data to collect yet
# db = get_db()
# products = db.products

# # Convert data to pandas DataFrame
# df = fetch_products(products)
# print(df.head()) # Small preview

# # Plot quantity distribution
# plot_quantity_distribution(df)

from config.db import get_db
from utils.data_processing import fetch_yearly_trends
from utils.visualisation import plot_yearly_trends

# Get DB connection
db = get_db()

# Fetch yearly trends data
yearly_trends = db.yearlytrends.find()  # assuming the collection name is 'yearlytrends'
df = fetch_yearly_trends(yearly_trends)

# Print data preview
print(df.head())
# No purpose, I just like to console log

# Generate the visualization
plot_yearly_trends(df)
