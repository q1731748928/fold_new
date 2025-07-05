const CryptoJS = require("crypto-js");
window = {
    n: {
    "0": 134982529,
    "1": 254232810,
    "2": 164556709,
    "3": 234907349,
    "4": 134685994,
    "5": 35463984,
    "6": 258277946,
    "7": 12518857,
    "8": 44638621,
    "9": 93783641,
    "10": 212253739,
    "11": 62792472,
    "12": 186688352,
    "13": 109500232,
    "14": 182488077,
    "15": 261196188,
    "16": 26354094,
    "17": 103248217,
    "18": 106891695,
    "19": 165771045,
    "20": 41530993,
    "21": 263704736,
    "22": 111785174,
    "23": 12753611,
    "24": 232116673,
    "25": 155524985,
    "26": 218291229,
    "27": 122452343,
    "28": 248250238,
    "29": 118739550,
    "30": 251169095,
    "31": 129059733,
    "32": 149835464,
    "33": 5498868,
    "34": 71719731,
    "35": 154456417,
    "36": 49635,
    "t": 37,
    "s": 0
}
}
var NodeRSA = require('node-rsa');

_ᕹᕴᕸᕶ.$_Bq = function() {
    var _ᕹᕴᕸᕶ = 2;
    for (; _ᕹᕴᕸᕶ !== 1; ) {
        switch (_ᕹᕴᕸᕶ) {
        case 2:
            return {
                $_HFBFP: function _ᕹᕴᕸᕶ(_ᕿᕸᖉᖈ, _ᕷᕹᖀᖈ) {
                    var _ᖙᖆᕺᕵ = 2;
                    for (; _ᖙᖆᕺᕵ !== 10; ) {
                        switch (_ᖙᖆᕺᕵ) {
                        case 4:
                            $_HFCAG[($_HFCBb + _ᕷᕹᖀᖈ) % _ᕿᕸᖉᖈ] = [];
                            _ᖙᖆᕺᕵ = 3;
                            break;
                        case 13:
                            $_HFCCF -= 1;
                            _ᖙᖆᕺᕵ = 6;
                            break;
                        case 9:
                            var $_HFCDe = 0;
                            _ᖙᖆᕺᕵ = 8;
                            break;
                        case 8:
                            _ᖙᖆᕺᕵ = $_HFCDe < _ᕿᕸᖉᖈ ? 7 : 11;
                            break;
                        case 12:
                            $_HFCDe += 1;
                            _ᖙᖆᕺᕵ = 8;
                            break;
                        case 6:
                            _ᖙᖆᕺᕵ = $_HFCCF >= 0 ? 14 : 12;
                            break;
                        case 1:
                            var $_HFCBb = 0;
                            _ᖙᖆᕺᕵ = 5;
                            break;
                        case 2:
                            var $_HFCAG = [];
                            _ᖙᖆᕺᕵ = 1;
                            break;
                        case 3:
                            $_HFCBb += 1;
                            _ᖙᖆᕺᕵ = 5;
                            break;
                        case 14:
                            $_HFCAG[$_HFCDe][($_HFCCF + _ᕷᕹᖀᖈ * $_HFCDe) % _ᕿᕸᖉᖈ] = $_HFCAG[$_HFCCF];
                            _ᖙᖆᕺᕵ = 13;
                            break;
                        case 5:
                            _ᖙᖆᕺᕵ = $_HFCBb < _ᕿᕸᖉᖈ ? 4 : 9;
                            break;
                        case 7:
                            var $_HFCCF = _ᕿᕸᖉᖈ - 1;
                            _ᖙᖆᕺᕵ = 6;
                            break;
                        case 11:
                            return $_HFCAG;
                            break
                        }
                    }
                }(24, 6)
            };
            break
        }
    }
}();
_ᕹᕴᕸᕶ.$_DP = function() {
    return _ᕹᕴᕸᕶ.$_Bq.$_HFBFP
}
function _ᕹᕴᕸᕶ() {}
function e() {
                    var _ᕷᕹᖀᖈ = _ᕹᕴᕸᕶ.$_DP()[4][22];
                    for (; _ᕷᕹᖀᖈ !== _ᕹᕴᕸᕶ.$_DP()[16][21]; ) {
                        switch (_ᕷᕹᖀᖈ) {
                        case _ᕹᕴᕸᕶ.$_DP()[8][22]:
                            return (65536 * (1 + Math["random"]()) | 0)["toString"](16)["substring"](1);
                            break
                        }
                    }
                }


function guid() {
                    var _ᕿᕸᖉᖈ = _ᕹᕴᕸᕶ.$_Cs
                      , _ᕷᕹᖀᖈ = ["$_EIFc"].concat(_ᕿᕸᖉᖈ)
                      , _ᖙᖆᕺᕵ = _ᕷᕹᖀᖈ[1];
                    _ᕷᕹᖀᖈ.shift();
                    var _ᕴᖉᕸᖚ = _ᕷᕹᖀᖈ[0];
                    return e() + e() + e() + e()
                }

function aesEncrypt(text, key, iv) {
    // 将输入的 key 和 iv 转换为 CryptoJS 支持的格式
    var keyWords = CryptoJS.enc.Utf8.parse(key);  // 密钥
    var ivWords = CryptoJS.enc.Utf8.parse(iv);    // 初始化向量（IV）

    // 使用 AES CBC 模式进行加密
    var encrypted = CryptoJS.AES.encrypt(text, keyWords, {
        iv: ivWords,
        mode: CryptoJS.mode.CBC,      // 使用 CBC 模式
        padding: CryptoJS.pad.Pkcs7  // 填充方式使用 Pkcs7
    });

    // 返回加密后的密文，使用 Base64 编码
    return encrypted.ciphertext.toString(CryptoJS.enc.Hex);
}

// 示例使用
var text = '{"setLeft":52,"passtime":683,"userresponse":53.69260133075313,"device_id":"","lot_number":"dc20c96ba1cb4254ad914bfdba976e3f","pow_msg":"1|0|md5|2025-05-23T21:01:14.347176+08:00|24f56dc13c40dc4a02fd0318567caef5|dc20c96ba1cb4254ad914bfdba976e3f||c4f51e87e5ad1753","pow_sign":"fe3f2285c4033a467912723503e31299","geetest":"captcha","lang":"zh","ep":"123","biht":"1426265548","SPCP":"YTY2","4bfdba97":{"ba9976":"fdba976e"},"em":{"ph":0,"cp":0,"ek":"11","wd":1,"nt":0,"si":0,"sc":0}}'
// var key = e() + e() + e() + e()      // 密钥，16 倍数
var key = "27f71f3d5bd67907"
var iv = "0000000000000000"
// var key = guid()
var encryptedText = aesEncrypt(text, key, iv);
// console.log('Encrypted:', encryptedText);
