const { Int32 } = require('mongodb');
const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const historico_sensorSchema = new Schema({
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
   },
   ligado: {
      type: Boolean,
      required: [true, 'É obrigadtório informar se está ligado ou não']
   }
 });
 
module.exports = mongoose.model('Historico_Sensor', historico_sensorSchema);