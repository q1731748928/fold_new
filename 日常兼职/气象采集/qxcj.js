var CryptoJS=require('crypto-js')
const  ask4u6FbhGV8 = "a0QHmC1Ova5958nC";//AESkey，可自定义
const  asi2hhkBUJbo = "bMu71lHRX6bRmPxU";//密钥偏移量IV，可自定义

const  acky6QolJSJi = "dLRSzDrm8xkryEyL";//AESkey，可自定义
const  acixHVhiNqmK = "fex6AA4zRfVrSPmr";//密钥偏移量IV，可自定义

const  dskQCqpdBOGo = "hEaIOlrX7tlhAOkz";//DESkey，可自定义
const  dsiqYiQHbZQp = "xMBwDXG1HOubUV04";//密钥偏移量IV，可自定义

const  dckCheMkUojW = "oi4aKMxMECWSyTaz";//DESkey，可自定义
const  dciEekKS6Cws = "p2uRrSFcN9oKLrKY";//密钥偏移量IV，可自定义




var DES = {
 encrypt: function(text, key, iv){
    var secretkey = (CryptoJS.MD5(key).toString()).substr(0, 16);
    var secretiv = (CryptoJS.MD5(iv).toString()).substr(24, 8);
    secretkey = CryptoJS.enc.Utf8.parse(secretkey);
    secretiv = CryptoJS.enc.Utf8.parse(secretiv);
    var result = CryptoJS.DES.encrypt(text, secretkey, {
      iv: secretiv,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
    });
    return result.toString();
 },
 decrypt: function(text, key, iv){
    var secretkey = (CryptoJS.MD5(key).toString()).substr(0, 16);
    var secretiv = (CryptoJS.MD5(iv).toString()).substr(24, 8);
    secretkey = CryptoJS.enc.Utf8.parse(secretkey);
    secretiv = CryptoJS.enc.Utf8.parse(secretiv);
    var result = CryptoJS.DES.decrypt(text, secretkey, {
      iv: secretiv,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
    });
    return result.toString(CryptoJS.enc.Utf8);
  }
};



var AES = {
  encrypt: function(text, key, iv) {
    var secretkey = (CryptoJS.MD5(key).toString()).substr(16, 16);
    var secretiv = (CryptoJS.MD5(iv).toString()).substr(0, 16);
    secretkey = CryptoJS.enc.Utf8.parse(secretkey);
    secretiv = CryptoJS.enc.Utf8.parse(secretiv);
    var result = CryptoJS.AES.encrypt(text, secretkey, {
      iv: secretiv,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
    });
    return result.toString();
  },
  decrypt: function(text, key, iv) {
    var secretkey = (CryptoJS.MD5(key).toString()).substr(16, 16);
    var secretiv = (CryptoJS.MD5(iv).toString()).substr(0, 16);
    secretkey = CryptoJS.enc.Utf8.parse(secretkey);
    secretiv = CryptoJS.enc.Utf8.parse(secretiv);
    var result = CryptoJS.AES.decrypt(text, secretkey, {
      iv: secretiv,
      mode: CryptoJS.mode.CBC,
      padding: CryptoJS.pad.Pkcs7
    });
    return result.toString(CryptoJS.enc.Utf8);
  }
};


var gethistory = (function(){

function osZ34YC04S(obj){
    var newObject = {};
    Object.keys(obj).sort().map(function(key){
        newObject[key] = obj[key];
    });
    return newObject;
}
return function(name){
    m0fhOhhGL='GETMONTHDATA'
    var oNLhNQ={city:name}
    var aMFs = '3c9208efcfb2f5b843eec8d96de6d48a';
    var cVWG2 = 'WEB';
    var t5GECZQ = new Date().getTime();

    var pKmSFk8 = {
      appId: aMFs,
      method: m0fhOhhGL,
      timestamp: t5GECZQ,
      clienttype: cVWG2,
      object: oNLhNQ,
      secret: CryptoJS.MD5(aMFs + m0fhOhhGL + t5GECZQ + cVWG2 + JSON.stringify(osZ34YC04S(oNLhNQ))).toString(CryptoJS.enc.Hex)
    };
    console.log(pKmSFk8.secret)
    pKmSFk8 = CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse(JSON.stringify(pKmSFk8)));
    pKmSFk8 = AES.encrypt(pKmSFk8, acky6QolJSJi, acixHVhiNqmK);
    return pKmSFk8;
};
})();
function get_data(data) {
    data=CryptoJS.enc.Base64.parse(data).toString(CryptoJS.enc.Utf8)
    data = DES.decrypt(data, dskQCqpdBOGo, dsiqYiQHbZQp);
    data = AES.decrypt(data, ask4u6FbhGV8, asi2hhkBUJbo);
    data=CryptoJS.enc.Base64.parse(data).toString(CryptoJS.enc.Utf8)
    return JSON.parse(data)
}

