const express = require('express');
const bodyParser = require('body-parser');
const diaAtual = require('../data')

const app = express();

//Servidor
let porta = 8090;
app.listen(porta, () => {
 console.log('Servidor em execução na porta: ' + porta);
});

const TempLigar = require('./model/dbHistorico_comandos');


const MongoClient = require('mongodb').MongoClient;
const uri = 'mongodb+srv://<mongo-user>:<mongo-password>@<mongo-server>?retryWrites=true&w=majority'; //Ajustar conforme o banco de dados
const database_name = 'ProjetoFinal';
const collection_name= 'HistoricoComandos';
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

app.post('/HistoricoComandos', (req, res, next) => {
    var temperatura = new TempLigar({
        "identificador": req.body.identificador,
        "temperatura": req.body.temperatura,
        "data": diaAtual
     });
    db.insertOne(temperatura, (err, result) => {
        if (err) return console.log("Error: " + err);
        console.log('Temperatura cadastrada com sucesso!');
        res.send('Temperatura cadastrada com sucesso!');
    });
});

app.get('/HistoricoComandos', (req, res, next) => {
    db.find({}).toArray((err, result) => {
        if (err) return console.log("Error: " + err);
        res.send(result);
    });
});

app.get('/HistoricoComandos/:identificador', (req, res, next) => {
    const result = db.findOne({ "identificador": req.params.identificador }, (err, result) => {
    if (err) return console.log("Temperatura não encontrada")
    res.send(result);
    });
});

app.put('/HistoricoComandos/:identificador', (req, res, next) => {
    db.updateOne({"identificador": req.params.identificador }, {
        $set: {
          "temperatura": req.body.temperatura,
          "data": diaAtual
        }
    }, (err, result) => {
        if (err) return console.log("Error: " + err);
        console.log('Temperatura alterada com sucesso!');
        res.send('Temperatura alterada com sucesso!');
    });
});
/*
app.delete('/HistoricoComandos/:identificador', (req, res, next) => {
    db.deleteOne({"identificador": req.params.identificador },(err, result) => {
        if (err) return console.log("Error: " + err);
        console.log('Temperatura removida!');
        res.send('Temperatura removida!');
    });
});
*/