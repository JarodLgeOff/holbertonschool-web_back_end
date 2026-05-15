const express = require('express');
const fs = require('fs');

const databasePath = process.argv[2];

const app = express();

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);

      const output = [];
      output.push(`Number of students: ${students.length}`);

      const fields = {};
      students.forEach((student) => {
        const parts = student.split(',');
        const firstname = parts[0];
        const field = parts[3];
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });

      Object.keys(fields).forEach((field) => {
        const list = fields[field];
        output.push(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      });

      resolve(output.join('\n'));
    });
  });
}

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.set('Content-Type', 'text/plain');
  countStudents(databasePath)
    .then((report) => {
      res.send(`This is the list of our students\n${report}`);
    })
    .catch((err) => {
      res.send(`This is the list of our students\n${err.message}`);
    });
});

app.listen(1245);

module.exports = app;
