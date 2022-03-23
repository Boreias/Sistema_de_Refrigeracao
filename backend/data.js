var hoje = new Date();

var dia = hoje.getDate();
var mes = hoje.getMonth();
var ano = hoje.getFullYear();
var hora = hoje.getHours();
var min = hoje.getMinutes();
var seg = hoje.getSeconds();

var dataAtual = dia + '/' + (mes+1) + '/' + ano + ' ' + hora + ':' + min + ':' + seg;

module.exports = dataAtual