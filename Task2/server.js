const express = require('express');
const app = express();
const port = 3000;

const users = [
    { name: 'John Doe', age: 25, email: 'john@example.com', contact: '1234567890', address: '123 Main St, Cityville' },
    { name: 'Jane Smith', age: 30, email: 'jane@example.com', contact: '0987654321', address: '456 Elm St, Townsville' },
    { name: 'Michael Johnson', age: 28, email: 'michael@example.com', contact: '1112223333', address: '789 Oak St, Villagetown' },
    { name: 'Emily Brown', age: 22, email: 'emily@example.com', contact: '2223334444', address: '321 Pine St, Cityville' },
    { name: 'William Davis', age: 35, email: 'william@example.com', contact: '3334445555', address: '654 Cedar St, Townsville' },
    { name: 'Linda Miller', age: 27, email: 'linda@example.com', contact: '4445556666', address: '987 Birch St, Villagetown' },
    { name: 'David Wilson', age: 32, email: 'david@example.com', contact: '5556667777', address: '147 Maple St, Cityville' },
    { name: 'Sophia Taylor', age: 29, email: 'sophia@example.com', contact: '6667778888', address: '258 Oak St, Townsville' },
    { name: 'James Anderson', age: 26, email: 'james@example.com', contact: '7778889999', address: '369 Pine St, Villagetown' },
    { name: 'Olivia Moore', age: 24, email: 'olivia@example.com', contact: '8889990000', address: '741 Cedar St, Cityville' },
];

app.get('/users', (req, res) => {
    res.json(users);
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
