const mongoose = require('mongoose');

const yearlyTrendsSchema = new mongoose.Schema({
    year: { type: Number, required: true },
    electric_car_sales_count: { type: Number, required: true },
    charging_station_count: { type: Number, required: true },
    total_charging_points: { type: Number, required: true },
    total_connection_power: { type: Number, required: true }
});

// This corresponds to the yearly trends fact table
// i keep reminding myself that this is a fact table
// anyways, the csv is in warehouse/processed

module.exports = mongoose.model('YearlyTrends', yearlyTrendsSchema);