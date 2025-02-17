const mongoose = require('mongoose');

const yearSchema = new mongoose.Schema({
    year: { type: Number, unique: true }
});

// This looks odd ik, but it's as organized as
// i think it should be

module.exports = mongoose.model('Year', yearSchema);