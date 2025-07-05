var CryptoJS = require('crypto-js')
var a = '9622';
var timestamp = String(Date.parse(new Date()) / 1000);
var tokens = CryptoJS.MD5(btoa(a + timestamp)).toString();
function get_params() {
    return {timestamp, tokens}
}