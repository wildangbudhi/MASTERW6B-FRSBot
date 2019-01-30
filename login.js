var username = process.argv[2];
var password = process.argv[3];
var publicKey = process.argv[4];
var plaintext = username + "|||" + password;

const JSEncrypt = require('node-jsencrypt');
var encryptor = new JSEncrypt();
encryptor.setPublicKey(publicKey);
var encrypted = encryptor.encrypt(plaintext);
console.log(encrypted);