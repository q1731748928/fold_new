const CryptoJS = require("crypto-js");

// 接收命令行参数
const args = process.argv.slice(2); // 去掉前两个默认参数
const x = args[0];         // 第一个用户参数是 x
const secretKey = args[1]; // 第二个用户参数是 secretKey

// AES加密函数
function EncryAES(x, secretKey) {
    const payload = JSON.stringify({ 'x': x, "y": 5 });
    const key = CryptoJS.enc.Utf8.parse(secretKey);
    const data = CryptoJS.enc.Utf8.parse(payload);

    const encrypted = CryptoJS.AES.encrypt(data, key, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });

    return encrypted.toString();
}

// 执行并输出结果到控制台
console.log(EncryAES(x, secretKey));