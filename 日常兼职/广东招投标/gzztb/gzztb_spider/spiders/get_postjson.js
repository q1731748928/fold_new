var CryptoJS = require('crypto-js')
function get_postjson(Y, secretKey) {
    function L0(H, R="XwKsGlMcdPMEhR1B") {
    var o = CryptoJS.enc.Utf8.parse(R)
      , e = CryptoJS.enc.Utf8.parse(H)
      , x = CryptoJS.AES.encrypt(e, o, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return x.toString()
}
postjson = L0(JSON.stringify({
                        x: Y,
                        y: 5
                    }), secretKey)
    return postjson
}

console.log(get_postjson(64, 'lDEEXRMy4Tu5hip4'));
