const mongoose = require('mongoose');

const electricCarSalesSchema = new mongoose.Schema({
    make: String,
    model: String,
    fuel: String,
    gear: String,
    offerType: String,
    price: Number,
    hp: Number,
    year: Number
});

module.exports = mongoose.model('ElectricCarSales', electricCarSalesSchema);
// Simple model made following the dataset structure in the warehouse