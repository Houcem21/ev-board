const fs = require('fs');
const csv = require('csv-parser');
const mongoose = require('mongoose');
const YearlyTrends = require('../models/yearly_trends_fact'); // Make sure the model path is correct
const path = require('path');
const dbConfig = require('../config/db.config.js');

// Path to the CSV file
const csvFilePath = path.resolve(__dirname, '../../warehouse/processed_data/yearly_trends.csv');

// Connect to the MongoDB database
mongoose.Promise = global.Promise;
// I still don't understand how this async function works exactly

mongoose.connect(dbConfig.url, {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => {
    console.log('Successfully connected to the database');
}).catch(err => {
    console.log('Could not connect to the database. Exiting now...', err);
    process.exit();
});

// Function to import CSV data into MongoDB
const importCsvData = () => {
    const results = [];

    // Read the CSV file and parse it
    fs.createReadStream(csvFilePath)
        .pipe(csv())
        .on('data', (row) => {
            // Push each row into the results array
            // Every line converts the data to its proper type
            // they happen to be all numbers
            // ofc I know how to handle other types
            results.push({
                year: parseInt(row.year),
                electric_car_sales_count: parseInt(row.electric_car_sales_count),
                commissioning_year: parseInt(row.commissioning_year),
                charging_station_count: parseInt(row.charging_station_count),
                total_charging_points: parseInt(row.total_charging_points),
                total_connection_power: parseFloat(row.total_connection_power)
            });
        })
        .on('end', async () => {
            try {
                if (results.length > 0) {
                    // Insert the data into MongoDB using insertMany
                    // mongo may not be the ideal db technology for this but
                    // it's all i know
                    await YearlyTrends.insertMany(results);
                    console.log('CSV data successfully imported into Backend database (i should rename it)');
                }
            } catch (err) {
                console.error('Error during data insertion in the importCsv file:', err);
            } finally {
                // Close the MongoDB connection
                mongoose.disconnect();
            }
        })
        .on('error', (err) => {
            console.error('Error reading CSV file:', err);
            mongoose.disconnect();
        });
};

// Call the function to import the CSV data
importCsvData();
