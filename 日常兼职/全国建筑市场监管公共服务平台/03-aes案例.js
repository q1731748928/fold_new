var CryptoJS = require('crypto-js')



f = CryptoJS.enc.Utf8.parse("Dt8j9wGw%6HbxfFn")
console.log(f)
m = CryptoJS.enc.Utf8.parse("0123456789ABCDEF")
function b(t) {
    var e = CryptoJS.enc.Hex.parse(t)
        , n = CryptoJS.enc.Base64.stringify(e)
        , a = CryptoJS.AES.decrypt(n, f, {
        iv: m,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    })
        , r = a.toString(CryptoJS.enc.Utf8);
    return r.toString()
}


aa = b("638d882f721469a32cd0948d5e35d40e4ec3b49bf357eeaf12e1304866056a31e28053f8d265b9e34231f61f79eb82fa0f762754aa4294eaf3359bc01c99c585a3f661f3181e11bbea6dc68b2835979613286a7e83067cc1f67618cc633e8dd1d1864c6d54a54efc06d41d87f872f4b9c973324f74d77898dc8e08a223ff1638772d8fd5023d519e3d03d6a62906f4c960576b9391dbb65276328d4699f532943362cc2faff4be872349c08c4fff07c3be56edc2b751796477aabbbb331755dcdd24718e50a719610700b9ebe6c32e42e4911234b74d12d4bc87d67172f73c7d")
console.log(aa)
// {"code":2000,"data":{"randomId":"1931188629921726464","success":1,"new_captcha":true,"challenge":"9c956692c3037efc8e919a5b30d6b142","gt":"c0084ad0567738668c18a81b2e9ca4cd"},"message":"初始化成功","succesue}


