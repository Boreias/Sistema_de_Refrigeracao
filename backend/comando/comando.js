const express = require('express');
const bodyParser = require('body-parser');

const app = express();

//Servidor
let porta = 8080;
app.listen(porta, () => {
 console.log('Servidor em execução na porta: ' + porta);
});

const TempLigar = require('./model/dbTempLigar');


const MongoClient = require('mongodb').MongoClient;
const uri = 'mongodb+srv://<mongo-user>:<mongo-password>@<mongo-server>?retryWrites=true&w=majority'; //Ajustar conforme o banco de dados
const database_name = 'ProjetoFinal';
const collection_name= 'Comando';
var db;
MongoClient.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true }, (error, client) => {
        if(error) {
            console.log('ERRO: não foi possível conectar à base de dados ` ' + database_name + ' `.');
            throw error;
        }
        db = client.db(database_name).collection(collection_name);
        console.log('Conectado à base de dados ` ' + database_name + ' `!');
    });

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

app.post('/Comando', (req, res, next) => {
    var temperatura = new TempLigar({
        "identificador": req.body.identificador,
        "temperatura": req.body.temperatura
     });
    db.insertOne(temperatura, (err, result) => {
        if (err) return console.log("Error: " + err);
        console.log('Temperatura cadastrada com sucesso!');
        res.send('Temperatura cadastrada com sucesso!');
    });
});

app.get('/Comando/:identificador', (req, res, next) => {
    const result = db.findOne({ "identificador": req.params.identificador }, (err, result) => {
    if (err) return console.log("Temperatura não encontrada")
    res.send(result);
    });
});

app.put('/Comando/:identificador', (req, res, next) => {
    db.updateOne({"identificador": req.params.identificador }, {
        $set: {
          "temperatura": req.body.temperatura
        }
    }, (err, result) => {
        if (err) return console.log("Error: " + err);
        console.log('Temperatura alterada com sucesso!');
        res.send('Temperatura alterada com sucesso!');
    });
});
/*
app.delete('/Comando/:identificador', (req, res, next) => {
    db.deleteOne({"identificador": req.params.identificador },(err, result) => {
        if (err) return console.log("Error: " + err);
        console.log('Temperatura removida!');
        res.send('Temperatura removida!');
    });
});
*/