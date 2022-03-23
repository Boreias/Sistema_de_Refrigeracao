const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const historico_comandosSchema = new Schema({
   identificador: {
  type: String, 
  required: [true, 'Identificador Obrigatório'], 
  max: 100
  },
 temperatura: {
  type: String, 
  required: [true, 'Temperatura é Obrigatória'], 
  max: 250
  },
  data: {
    type: String, 
    required: [true, 'Data é Obrigatória'],
    max: 250
    }
 });
 
module.exports = mongoose.model('Historico_Comandos', historico_comandosSchema);