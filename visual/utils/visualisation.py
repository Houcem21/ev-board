# import matplotlib.pyplot as plt

# # This is a basic data visiualisation function
# # that plots the distribution of the quantity column
# # It will become useful when the data is populated
# def plot_quantity_distribution(df):
#     # Plot histogram of quantity distribution
#     plt.hist(df['quantity'], bins=50, color='skyblue', edgecolor='black')
#     plt.title('Quantity Distribution')
#     plt.xlabel('Quantity')
#     plt.ylabel('Frequency')
#     plt.savefig('visualisations/charts/quantity_distribution.png')
#     plt.show()

# # btw, where did the __pycache__ directory come from?
# # I've no clue, but I'll ignore it for now

import matplotlib.pyplot as plt

def plot_yearly_trends(df):
    # Plot electric car sales vs charging station count
    plt.figure(figsize=(10, 6))
    
    plt.plot(df['year'], df['electric_car_sales_count'], label='Electric Car Sales', color='blue', marker='o')
    plt.plot(df['year'], df['charging_station_count'], label='Charging Stations', color='green', marker='o')
    
    plt.title('Yearly Trends of Electric Car Sales and Charging Stations')
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.legend()
    plt.grid(True)
    plt.xticks(df['year'], rotation=45)
    
    # Show the plot
    plt.tight_layout()
    plt.show()
    plt.savefig()


# I can add a savfig to save the chart in visualisations/chart or smth
# right now i'm good though