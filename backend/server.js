// server.js
const express = require('express');
const cors = require('cors');
const { detectFakeNews } = require('./routes');

require('dotenv').config();

const app = express();
app.use(cors());
app.use(express.json());

// Route
app.post('/api/detect', detectFakeNews);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Backend running on port ${PORT}`));
