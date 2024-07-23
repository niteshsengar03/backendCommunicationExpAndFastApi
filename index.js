const express = require('express');
const axios = require('axios');
const app = express();
const port = 3000;

app.use(express.json());

app.post('/calculate-sum', async (req, res) => {
    try {
        
        const response = await axios.post('http://127.0.0.1:8000/sum', {
            x: req.body.x,
            y: req.body.y
        });
        // Send back the sum received from the FastAPI server
        res.json(response.data);
    } catch (error) {
        console.error(error);
        res.status(500).send('Error communicating with the FastAPI server');
    }
});

app.listen(port, () => {
    console.log(`Express server listening at http://localhost:${port}`);
});