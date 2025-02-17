# Dev note
just run these commands in order :

-- cd backend --

-- node server.js -- 

-- cd frontend --

-- python3 app.py --

# Project Overview
The Electric Car Sales & Charging Station Trends Analysis project is designed to help visualize and understand the trends in electric vehicle adoption and the growth of supporting charging infrastructure. By analyzing data from 2011 to 2021, 

The goal of the project is to offer insights into how electric vehicle adoption correlates with the expansion of charging stations.

# Project Structure:
This project is organized into the following key folders and components:

backend/:

Contains the server and logic for importing, storing, and handling the data. It connects to a MongoDB database and provides an interface for data storage.
models/: Defines the data schema (e.g., for YearlyTrends)
importing/: A script for importing the CSV data (yearly_trends.csv) into MongoDB.
config/: Contains configuration files (e.g., for connecting to the database).

visual/:

Python scripts used for data visualization and analysis.
config/: A file that contains database connection settings and data handling configurations.
utils/: Helper functions for data processing and visualization.
visualisations/: Includes the actual visualizations generated from the data, such as charts and reports.

warehouse/:

Contains the raw, processed and etl data files (e.g., CSVs) used for analysis and visualization.

# Project Steps
The project is divided into several phases to ensure proper data management :


## Main Implemented Phases in the Database
1. Data Gathering & Import
CSV File: Data was gathered from a CSV file (yearly_trends.csv) that contains information on electric car sales, commissioning years, charging stations, charging points, and connection power from 2011 to 2021.

2. Data Preparation (ETL)
The CSV data was cleaned, parsed, and transformed (ETL) to match the structure of the MongoDB database.
Using the csv-parser library, the CSV rows were read and stored as documents in the YearlyTrends csv

3. Data Storage & Modeling
The database schema was designed with a focus on storing time-series data (e.g., year, electric car sales, charging stations)
insertMany method was used to insert bulk data into the backend db

4. Data Analysis & Visualization
Libraries like matplotlib, was used for data visualization.
The main chart plotted the relationship between electric car sales and charging stations over the years, helping to understand the correlation between these two metrics.
Visuals were saved and displayed for further reporting and presentation.

## Problems Solved:

Data Importing: One of the challenges was properly importing and transforming the CSV data into the desired format for MongoDB, especially handling potential parsing errors and ensuring data consistency.

Visualization: Generating clear and insightful visualizations of the data required proper data cleaning and filtering.

Possible Enhancements:
Enhanced Visualizations: Future enhancements could include more detailed interactive charts using more libraries

# Data sources
Thank you Kagglehub
you can find the links in the warehouse/raw_data/data.py file
Copilot was a major help to this project

# Use cases
This project has successfully enabled the import, analysis, and visualization of trends related to electric car sales and charging infrastructure.

## Credits
Chatgpt has earned my loyalty. I'm probably moving to Deepseek still but I'll always have you in my heart chat.