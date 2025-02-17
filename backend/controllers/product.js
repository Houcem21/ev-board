const productModel = require('../models/product');

// Create a new product and save it to the database
exports.create = async (req, res) => {
    // Request validation
    if (!req.body.name || !req.body.price || !req.body.quantity) {
        return res.status(400).send({
            message: "Product content can not be empty"
        });
    }

    // Create a product
    const product = new productModel({
        name: req.body.name,
        price: req.body.price,
        description: req.body.description || "No description provided",
        quantity: req.body.quantity
    });

    // Save product in the database
    await product.save()
        .then(data => {
            res.send({
                message: "Product created successfully",
                product: data
            });
        }).catch(err => {
            res.status(500).send({
                message: err.message || "Some error occurred while creating the product."
            });
        });
};

// Retrieve and return all products from the database.
exports.findAll = async (req, res) => {
    await productModel.find()
        .then(products => {
            res.send(products);
        }).catch(err => {
            res.status(500).send({
                message: err.message || "Some error occurred while retrieving products."
            });
        });
};

// Find a single product with a productId
exports.findOne = async (req, res) => {
    await productModel.findById(req.params.productId)
        .then(product => {
            if (!product) {
                return res.status(404).send({
                    message: "Product not found. Given id " + req.params.productId
                });
            }
            res.send(product);
        }).catch(err => {
            if (err.kind === 'ObjectId') {
                return res.status(404).send({
                    message: "Error : Product not found with id " + req.params.productId
                });
            }
            return res.status(500).send({
                message: "Error retrieving product with id " + req.params.productId
            });
        });
};

// Update a product identified by the productId in the request
exports.update = async (req, res) => {
    if(!req.body) {
        return res.status(400).send({
            message: "Product content can not be empty"
        });
    }
    const id = req.params.productId;
    await productModel.findByIdAndUpdate(id, req.body, {new: true}, {useFindAndModify: false})
        .then(product => {
            if(!product) {
                return res.status(404).send({
                    message: "Product not found with id " + id
                });
            }
            res.send({
                message: "Product updated successfully",
                product: product
            });
        }).catch(err => {
            if(err.kind === 'ObjectId') {
                return res.status(404).send({
                    message: "Product not found with id " + id
                });
            }
            return res.status(500).send({
                message: "Error updating product with id " + id
            });
        });
};

// Delete a product with the specified productId in the request
exports.delete = async (req, res) => {
    await productModel.findByIdAndDelete(req.params.productId, {useFindAndModify: false})
        .then(product => {
            if(!product) {
                return res.status(404).send({
                    message: "Product not found with id " + req.params.productId
                });
            }
            res.send({
                message: "Product deleted successfully"
            });
        }).catch(err => {
            if(err.kind === 'ObjectId' || err.name === 'NotFound') {
                return res.status(404).send({
                    message: "Product not found with id " + req.params.productId
                });
            }
            return res.status(500).send({
                message: "Could not delete product with id " + req.params.productId
            });
        });
};

// CRUD functions implemented for the product model
// This is a template model