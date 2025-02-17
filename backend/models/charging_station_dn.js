const mongoose = require('mongoose');

const chargingStationSchema = new mongoose.Schema({
    operator: String,
    station_type: String,
    location: String,
    postal_code: String,
    latitude: Number,
    longitude: Number
});

module.exports = mongoose.model('ChargingStation', chargingStationSchema);
// Simple model made following the dataset structure in the warehouse
// Lots of info were not used bc I honestly felt overwhelmed