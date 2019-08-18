# weblate-icu-checker
a function that check if a string is an icu-format valid 
by using a function that verify if a string that contains parameters is broken or not

L’outil de validation du format ICU :
https://format-message.github.io/icu-message-format-for-translators/editor.html

Usage de la libraire "format-message" pour parser toutes les chaines 

https://github.com/format-message/format-message
https://www.npmjs.com/package/format-message

var parse = require('format-message-parse');
formatMessage('Hello, { name }!', { name: user.name })

commandes :

-	npm init
-	npm install format-message –save
-	node nomdufichier.js

