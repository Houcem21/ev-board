const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/', (req, res) => {
  res.json({ "message": 'test backend code runing, check CRUD operations' });
});

app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
});

// Set up the database connection

const dbConfig = require('./config/db.config.js');
const mongoose = require('mongoose');

mongoose.Promise = global.Promise;

mongoose.connect(dbConfig.url, {
    useNewUrlParser: true
}).then(() => {
    console.log('Successfully connected to the database');
}).catch(err => {
    console.log('Could not connect to the database. Exiting now...', err);
    process.exit();
});

// Define the routes
const ProductRoutes = require('./routes/product');
app.use('/api/products', ProductRoutes);

// So this is basically a simple CRUD app
// We have a product model, controller and routes
// It should come in handy when I need to render
// the products in the frontend
// Maybe I can use it for the python
// visualizations as well, idk

// Time for Data Warehousing
const dwhRoutes = require('./routes/dwh');

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/backend', { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('Connected to MongoDB'))
    .catch(err => console.log('Error connecting to MongoDB:', err));

app.use(express.json());
app.use('/api/dwh', dwhRoutes);

// Start the server on a new port
const port = 5001;
// I was using the variable but it read as 3000 so manually it shall be
app.listen(5001, () => {
    console.log(`Server is running on port ${port}`);
});