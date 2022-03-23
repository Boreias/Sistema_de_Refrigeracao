const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const tempLigarSchema = new Schema({
   identificador: {
  type: String, 
  required: [true, 'Identificador Obrigatório'], 
  max: 100
  },
 temperatura: {
  type: String, 
  required: [true, 'Temperatura é Obrigatória'], 
  max: 250
  }
 });
 
module.exports = mongoose.model('TempLigar', tempLigarSchema);