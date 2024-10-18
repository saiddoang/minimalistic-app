const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Appsnya Jalan Euy!');
});

const port = process.env.PORT || 5000;
app.listen(port, () => {
  console.log(`App running on port ${port}`);
});
