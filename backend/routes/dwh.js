// My head hurts
// This file will be used to populate mongodb
// with the yearly trends data so we
// can set up a data warehouse so we
// can use it in the frontend and
// do visulaizations and stuff
// The data is in warehouse/processed/yearly_trends.csv
// The db is somewhere
// I'm not sure where

const express = require('express');
const router = express.Router();
const YearlyTrends = require('../models/yearly_trends_fact');
const ChargingStation = require('../models/charging_station_dn');
const ElectricCarSales = require('../models/electric_car_sales_dn');
const Year = require('../models/year_dn');

// This is the endpoint to populate the yearly trends fact table
router.post('/populate-dwh', async (req, res) => {
    const yearlyTrendsData = req.body; // Expecting an array of data in the format you generated
    
    try {
        // First, insert the year dimension records
        for (let trend of yearlyTrendsData) {
            const yearExists = await Year.findOne({ year: trend.year });
            if (!yearExists) {
                const yearDoc = new Year({ year: trend.year });
                await yearDoc.save();
            }

            // Insert the charging station dimension data
            const stationExists = await ChargingStation.findOne({ location: trend.location });
            if (!stationExists) {
                const stationDoc = new ChargingStation({
                    operator: trend.operator,
                    station_type: trend.station_type,
                    location: trend.location,
                    postal_code: trend.postal_code,
                    latitude: trend.latitude,
                    longitude: trend.longitude
                });
                await stationDoc.save();
            }

            // Insert the electric car sales dimension data
            const carExists = await ElectricCarSales.findOne({ make: trend.make, model: trend.model, year: trend.year });
            if (!carExists) {
                const carDoc = new ElectricCarSales({
                    make: trend.make,
                    model: trend.model,
                    fuel: trend.fuel,
                    gear: trend.gear,
                    offerType: trend.offerType,
                    price: trend.price,
                    hp: trend.hp,
                    year: trend.year
                });
                await carDoc.save();
            }

            // Now insert the fact table entry
            const yearlyTrendDoc = new YearlyTrends({
                year: trend.year,
                electric_car_sales_count: trend.electric_car_sales_count,
                charging_station_count: trend.charging_station_count,
                total_charging_points: trend.total_charging_points,
                total_connection_power: trend.total_connection_power
            });
            await yearlyTrendDoc.save();
        }

        res.status(200).send('Data successfully populated in DWH');
    } catch (err) {
        res.status(500).send('Error populating DWH: ' + err.message);
    }
});

// Route to get data from YearlyTrends 
// I think I should populate it beforehand
// happy to have a warehouse folder :)
router.get('/get-yearly-trends', async (req, res) => {
    try {
        const trends = await YearlyTrends.find();
        res.json(trends);
    } catch (err) {
        res.status(500).send('Error fetching trends: ' + err.message);
    }
});


module.exports = router;

