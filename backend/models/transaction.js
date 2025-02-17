const mongoose = require('mongoose');

var schema = new mongoose.Schema({
    amount: {
        type: Number,
        required: true
    },
    description: {
        type: String,
        required: true
    },
    date: {
        type: Date,
        default: Date.now
    },
    product: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Product'
    }
});

var transaction = mongoose.model('Transaction', schema);
module.exports = transaction;

// Not being used rn
// template