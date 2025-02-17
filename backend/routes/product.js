const express = require('express');
const ProductController = require('../controllers/product');
const router = express.Router();

router.get('/', ProductController.findAll);
router.get('/:productId', ProductController.findOne);
router.post('/', ProductController.create);
router.put('/:productId', ProductController.update);
router.delete('/:productId', ProductController.delete);

module.exports = router;

// CRUD operations for the product model
// Template