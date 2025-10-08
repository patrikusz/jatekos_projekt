const express = require('express');
const AuthController = require('../controllers/authController');

const router = express.Router();
const authController = new AuthController();

router.post('/login', authController.login);
router.post('/register', authController.register);

module.exports = router;