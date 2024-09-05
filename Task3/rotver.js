const express = require('express');
const app = express();
const port = 3000;

app.get('/user', (req, res) => {
    res.json({name: 'Sithu', age: 37 , email: 'sithu.ko.ko@outlook.com', contact: ''});
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
