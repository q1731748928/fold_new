const path = require("path");
delete __dirname
delete __filenames
delete process


window = global;
Window = function(){};
window.__proto__ = Window.prototype;

function HTMLAllCollection() {}
window.HTMLAllCollection = HTMLAllCollection;



location = {
    "ancestorOrigins": {},
    "href": "https://jingxi.com/",
    "origin": "https://jingxi.com",
    "protocol": "https:",
    "host": "jingxi.com",
    "hostname": "jingxi.com",
    "port": "",
    "pathname": "/",
    "search": "",
    "hash": ""
}

document={
    querySelector:function(ele){
        console.log('document querySelector:::',ele)
    },
    createElement:function(ele){
        console.log('document createElement:::',ele)
        if (ele == 'script'){
            return {}
        }
        if (ele == 'canvas'){
            return {}
        }
    },
    getElementById:function(ele){
        console.log('document getElementById:::',ele)
    },
    createEvent:function(ele){
        console.log('document createEvent:::',ele)
    },
    cookie: 'shshshfpa=62539cd0-d17f-80d4-7be0-6d23aed03bc4-1741747326; shshshfpx=62539cd0-d17f-80d4-7be0-6d23aed03bc4-1741747326; ipLoc-djd=22-1930-50948-71603; _base_=YKH2KDFHMOZBLCUV7NSRBWQUJPBI7JIMU5R3EFJ5UDHJ5LCU7R2NILKK5UJ6GLA2RGYT464UKXAI4Z6HPCTN4UQM3WHVQ4ENFP57OC6DLJ2PMWO3OPKDCGVA26WCXPGWTCNE6YVKRXISVA6XLQWMI7TAZWS3GKYL2ZCNGXSSG4SOQWCP5WPWO6EFS7HEHMRWVKBRVHB33TFD5WR4O3PTGOTVOBJSMQ7LPFV7Q46KT47K7XGVE7YMZ6QGODVGHO5KCYGYWQX2Q6PMWUTN6JOUSDHV2NPKLJWUF2FVTVM47UOMUQIOKATCQ3LFS6DZMD3SVKZO2JAUQFGBYBPBUJFFKWNDEL2KB2GOJRFCS5A; user-key=42e6098d-6999-4161-8cf8-33838d33b76d; __jdu=17424453509111974390222; PCSYCityID=CN_510000_510100_0; language=zh_CN; unick=b9669m3jmd9rnu; _tp=c6DJY3SU5Wjx4dHAXBCR2Q%3D%3D; _pst=xuxu3261; TrackID=1B70xFYB91HF9ksDWBcWwcAgVntjAAzeRDb3qv8wWQoNzPl9zqvWSoL0bAhejIssHuy-eSKZnY3fkJnkpo0vqSWsBmvxfYudvjXYFWag1UOU|||HFc0E15e1dK1ffsfn98I-w; pinId=HFc0E15e1dK1ffsfn98I-w; light_key=AASBKE7rOxgWQziEhC_QY6ya_NFmbeIHEL9R4n6d6JIhbibCpcNAwDMat30Etkwu0m8EW_pG; 3AB9D23F7A4B3C9B=6DTZX7CBH3GTNDGDN3MIPWVXORL7WR5XZXY3IV62A66CYOGS6T3FBFQIWNQYAY37WGHAVCVJTL56UXZOOSUNTZK4FQ; wxa_level=1; retina=0; cid=9; appCode=ms0ca95114; webp=1; __jdc=56585130; mba_muid=17424453509111974390222; mt_xid=V2_52007VwMUV15dV14dTRhUBWcDGlRYWlpbHEoabFVuUxNUX1AFRkodSQ8ZYlZCB0EIWw4ZVRhYBWQKE1RVDAZaHHkaXQZjHxNQQVtVSx9PEl4MbAAaYl9oUmoWShpYA24DG1VbXFRbGU0aVQVlMxJbWV8%3D; x-rp-evtoken=mGW9U4qbzsaBdCMe70m9pKvUZqtaRf1uPCTmQ8EVvOghX5PD5GEqPl3-QFMkmdBVNDbzKsh0iitbASzX5XoFQg%3D%3D; sc_width=1536; pt_token=qim9tko0; pwdt_id=jd_MTUBZHCRNKpo; sfstoken=tk01mea1a1d48a8sMiszKzN1VjdziemAsPNvNaqK4v8NQRxUtrrg2ANEDiXnck4Zx1A/B1q/iLw4KkvhOJZw/jBtnHfr; __jda=56585130.17424453509111974390222.1742445351.1742981689.1742993615.12; wqmnx1=MDEyNjM2MXQvbW9kMDAyP2RlLzAzLy8yZC8zOGphODYyOWwgbyAgOyBXLzZNa2tyMy5hNzFzZGEyMk9EKSZI; __wga=1742993792555.1742993737262.1742981919828.1742981919828.2.2; shshshfpb=BApXSGDeO0fBApTLAIzhuYMkpBFQVFooeBgM1dAlp9xJ1PdZfQqvipzjRpAjIHa1jfFTMBqbn; yodaId=%E2%82%B995b92daccb0fda14290e8dd209ba5ae0%E2%82%B9; cd_eid=jdd036DTZX7CBH3GTNDGDN3MIPWVXORL7WR5XZXY3IV62A66CYOGS6T3FBFQIWNQYAY37WGHAVCVJTL56UXZOOSUNTZK4FQAAAAMV2KDKAGQAAAAADXZD4J42MTVPUIX; visitkey=7999382343586060544; __jxjda=68990090.7999382343586060544.1742994072.1742994072.1742994072.1; __jdv=122270672%7Cdirect%7C-%7Cnone%7C-%7C1742994081599; _tj_rvurl=https%3A//wq.jd.com/wxapphttps%3A//m.jingxi.com/item/view%3Fas%3D0%26pps%3D; jxsid_s_u=https%3A//wqs.jd.com/item/view.html; e_wq_addr=DJK0Ctc5DzU2CIU3GzSyXzSmCtTpDNCyCzLpDNC4CzuvD0CvdJU2HOSvdJVOHOHpTXU1CzU3TXU1CJG1TXU1HJKyXyV1EJYmDsV1DOUyHMV1DUUmCv8vdJZNGtCvdJZPGUOvdJq4DJcvdJumDJCvD0CvdJU2HOSvdJVOHOGvdJUzDJcvdJUnDNUvdJVPCNSvdJu2CNYvdJHPCuGvdJVPCNSvdJZNGtCvdJZPGUOvdJq4DJcvdJumDJCvdJUzDJcvdJUnDNUvdJY1ENcvdJUzCJYvdJY1GzUvdJZPCzqvdJqmDOCvdJHPCUOvdJVMDtYvdJu2DtSvD0CnCNYkCNY5DzS3TJTNCzOkDJC1Czqy; wq_addr=5042797561%7C22_2022_43230_43839%7C%u56DB%u5DDD_%u5357%u5145%u5E02_%u9606%u4E2D%u5E02_%u6CB3%u6EAA%u8857%u9053%7C%u56DB%u5DDD%u5357%u5145%u5E02%u9606%u4E2D%u5E02%u6CB3%u6EAA%u8857%u9053%u5357%u5145%u6587%u5316%u65C5%u6E38%u804C%u4E1A%u5B66%u9662%7C106.069727%2C31.535382; jxsid=17429941149344645706; PPRD_P=UUID.7999382343586060544-CT.138631.89.2-LOGID.1742994340860.1533546684; jxsid_s_t=1742994340905; 3AB9D23F7A4B3CSS=jdd036DTZX7CBH3GTNDGDN3MIPWVXORL7WR5XZXY3IV62A66CYOGS6T3FBFQIWNQYAY37WGHAVCVJTL56UXZOOSUNTZK4FQAAAAMV2KOQ27IAAAAACCC5SNJ4PA4STUX; _gia_d=1; __jdb=56585130.15.17424453509111974390222|12.1742993615; mba_sid=17429936157471419578251.51; sdtoken=AAbEsBpEIOVjqTAKCQtvQu17GYPf5yautLy2hrZQqubyCtdEe7K-I5fcIUQKlAJj8CzCMB6dQ2n5r0Dln2lBaWG30whpL_3Bo6Q24MW0w_PeRnGZ8JfF-dpDUNcnlVF_sskHq2fR2XTW',
    head: {childElementCount:42},
    body: {childElementCount:25},
    all: {},
    documentElement: {
        getAttribute:function(){}
    },
    getElementsByTagName:function(ele){
        console.log('document getElementsByTagName:::',ele)
        if (ele == 'head'){
            return []
        }
    }

}
document.all.__proto__ = HTMLAllCollection.prototype



navigator = {
    appName: "Netscape",
    appVersion: '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
    platform: "Win32",
    product: "Gecko",
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0',
    language: "zh-CN",
    languages: [
        "zh-CN",
        "en",
        "en-GB",
        "en-US"
    ],
    plugins: {
        length:5
    },
    webdriver: false,
    hardwareConcurrency: 8,
}




localStorage = {}
localStorage['WQ_dy1_vk'] = '{"5.0":{"73806":{"e":31536000,"v":"wppax9scdrdpr3m6","t":1740717538097},"b5216":{"e":31536000,"v":"r99ax3swca9999p5","t":1740717543482}}}'
localStorage.getItem = function (ele){
    console.log("[native code] localStorage getItem:::",ele)
    if (ele == 'WQ_gather_wgl1'){
        return '{"v":"b2bffcfae898a7d97b93b3174a5c891a","t":1740718818567,"e":31536000}'
    }
    if (ele == 'WQ_dy1_tk_algo'){
        return '{"r99ax3swca9999p5":{"b5216":{"v":"eyJ0ayI6InRrMDN3YjJjMzFjOTkxOG52ckVPMnlTZXhXSUI0NURhVW1GdjB0YkJ0QnhaTEpHb1ZfTHVoOUJsQ01IODdzbFZ6Z3JOSmd2WmRTNkExV2psRTVnTlphZ3lIaU1wIiwiYWxnbyI6ImZ1bmN0aW9uIHRlc3QodGssZnAsdHMsYWksYWxnbyl7dmFyIHJkPSd4bjhsRTFJME40N3AnO3ZhciBzdHI9XCJcIi5jb25jYXQodGspLmNvbmNhdChmcCkuY29uY2F0KHRzKS5jb25jYXQoYWkpLmNvbmNhdChyZCk7cmV0dXJuIGFsZ28uTUQ1KHN0cik7fSJ9","e":86400,"t":1740717557947}}}'
    }
    if (ele == 'WQ_gather_cv1'){
        return '{"v":"3fb777da864642050ee0bbb3a51937cf","t":1740719278039,"e":31536000}'
    }
    return this[ele]
};
localStorage.setItem = function (key,value){
    console.log("[native code] localStorage getItem:::",key,value)
    this[key] = value
};


getOwnPropertyDescriptor_=Object.getOwnPropertyDescriptor
Object.getOwnPropertyDescriptor = function (obj, prop) {
    // console.log('[native code] Object getOwnPropertyDescriptor:::','对象--->',obj,'属性--->',prop)
    if (obj === navigator && prop === 'userAgent') {
        return undefined
    }
    if (obj === navigator && prop === 'webdriver'){
        return undefined
    }
    if (prop == 'window'){
        xxx = getOwnPropertyDescriptor_(obj, prop)
        xxx.get = function window(){}
        return xxx
    }
    return getOwnPropertyDescriptor_(obj, prop)
}

// 执行文件的文件名
const name = "h5st.js";
// 拼接输出的文件路径
const customPath = `${location.href}${name}`;
const targetFileName = path.basename(name);
Error.prepareStackTrace = function (error, structuredStackTrace) {
    return `${error.name}: ${error.message}\n` +
        structuredStackTrace
            .filter(callSite => !callSite.getFileName()?.startsWith("node:"))
            .map(callSite => {
                let fileName = callSite.getFileName();
                if (fileName && path.basename(fileName) === targetFileName) {
                    fileName = customPath; // 替换路径
                }
                return `    at ${callSite.getFunctionName() || "<anonymous>"} (${fileName}:${callSite.getLineNumber()}:${callSite.getColumnNumber()})`;
            })
            .join("\n");
};




function ProxyDocumentObjects(proxyObjs) {
    for (let i = 0; i < proxyObjs.length; i++) {
        const documentObj = proxyObjs[i];
        const keys = Object.keys(documentObj);
        keys.forEach(key => {
            const value = documentObj[key];
            if (value && typeof value === "object") {
                documentObj[key] = new Proxy(value, {
                    get(target, property, receiver) {
                        const propValue = Reflect.get(target, property, receiver);
                        console.log("方法:", "get", "对象:", `${key}`, "属性:", property, "属性类型:", `${typeof property}`, "属性值:", propValue, "属性值类型:", `${typeof propValue}`);
                        return propValue;
                    },
                    set(target, property, newValue, receiver) {
                        console.log("方法:", "set", "对象:", `${key}`, "属性:", property, "属性类型:", `${typeof property}`, "属性值:", newValue, "属性值类型:", `${typeof newValue}`);
                        return Reflect.set(target, property, newValue, receiver);
                    }
                });
            }
        });
    }
}
// 这里需要写对象
// const proxyObjs = [window, document, navigator,location,localStorage];
// ProxyDocumentObjects(proxyObjs);


// debugger