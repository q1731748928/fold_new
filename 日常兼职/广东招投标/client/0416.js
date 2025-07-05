// 从命令行获取请求方法和参数字符串
const requestMethod = process.argv[2] || 'POST'; // 默认为POST请求
const paramsStr = process.argv[3] || 'type=trading-type&publishStartTime=&publishEndTime=&keyword=&thirdType=10&siteCode=44&secondType=A&projectType=A02&dateType=&searchType=pf&total=50&pageNo=1&pageSize=10&totals=38067&openConvert=false';
const CryptoJS = require("crypto-js");

///////////////////////////////////////////////////////nQe
const NV = "zxcvbnmlkjhgfdsaqwertyuiop0987654321QWERTYUIOPLKJHGFDSAZXCVBNM",
  tQe = NV + "-@#$%^&*+!";

function eQe(e, t) {
  switch (arguments.length) {
    case 1:
      return parseInt(Math.random() * e + 1, 10);
    case 2:
      return parseInt(Math.random() * (t - e + 1) + e, 10);
    default:
      return 0;
  }
}

function nQe(e) {
  return [...Array(e)].map(() => NV[eQe(0, 61)]).join("");
}
////////////////////////////////////////结束

function rQe(e) {
    let t = "";
    if (typeof e == "object") {
        // 如果是对象，转换为键值对数组并排序
        t = Object.keys(e)
            .map(n => `${n}=${e[n]}`)
            .sort()
            .join("&");
    } else if (typeof e == "string") {
        // 如果是字符串，直接拆分后排序
        t = e.split("&").sort().join("&");
    }
    return t;
}

function YHe(input) {
    const hash = CryptoJS.SHA256(input);
    return {
        hex: hash.toString(CryptoJS.enc.Hex),  // 返回16进制字符串
        words: hash.words                      // 返回words数组
    };
}

const m = "Bg5Wj$3UaYf"
    , p = Date.now()
    , h = nQe(16)

function dg(e={}, method='POST') {
    const {p: t, t: n, n: r, k: o} = e;
    let a = '';
    if (method === 'POST') {
        if (typeof t == "object") {
            a = Object.keys(t)
                .map(n => `${n}=${t[n]}`)
                .sort()
                .join("&");
        } else if (typeof t == "string") {
            a = t.split("&").sort().join("&");
        }
    } else { // GET请求时
        a = ''; // 对于GET请求，传入空字符串作为参数
    }

    const { hex, words } = YHe(r + o + decodeURIComponent(a) + n); // 获取哈希结果
    return {
        signHex: hex,     // 返回16进制签名
        signWords: words  // 返回words数组
    }
}

/****************** 使用示例 ******************/

const sign1 = dg({
    p: "",
    t: p,
    n: h,
    k: m
}, requestMethod);

let sign2;
if (requestMethod === 'POST') {
    sign2 = dg({
        p: paramsStr,
        t: p,
        n: h,
        k: m
    }, 'POST');
} else {
    sign2 = dg({
        p: '',
        t: p,
        n: h,
        k: m
    }, 'GET');
}

const result = {
    nonce: h,
    timestamp: p,
    signatures: sign1.signHex,
    signature: sign2.signHex
};
console.log(JSON.stringify(result));