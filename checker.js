// var formatMessage = require('format-message');
var parse = require('format-message-parse');
var args = process.argv.slice(2); // on vire les 2 premiers arguments qui sont: 'node' et 'chemin du fichier .js' ainsi args[0] est la chaine de caractere à parser

// console.log(args);
// var tocarev = JSON.stringify({name : "ulrich"})
// console.log(tocarev);
// console.log(typeof(tocarev));
// console.log(process.argv[3]);
// console.log(JSON.parse(tocarev));
// console.log(JSON.parse(process.argv[3]));

let r = parse(args[0]); // on utilise la libraire formatMessage qui fait le parsing
console.log(r); // affiche le resultat pour qu'on puisse le recuperer depuis le process appelant (c-a-d le script python)