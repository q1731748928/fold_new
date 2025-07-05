delete __dirname
delete __filename


window = global;
Window=function(){}
window.Window = Window
window.__proto__ = Window.prototype


delete global
delete Buffer
delete process

_script={
    type:{}
}
_canvas={
    getContext:function(ele){
        console.log('_canvas getContext:::',ele)
    }
}

function HTMLAllCollection(){}
window.HTMLAllCollection=HTMLAllCollection
_all = {}
_all.__proto__ = HTMLAllCollection.prototype

_body = {
    childElementCount:25,
    innerHTML:''
}
_head = {
    childElementCount:54
}
_documentElement={}

function HTMLDocument(){}
window.HTMLDocument=HTMLDocument
document={
    querySelector:function(ele){
        console.log('document querySelector:::',ele)
    },
    createElement:function(ele){
        console.log('document createElement:::',ele)
        if (ele == 'script'){
            return _script
        }
        if (ele == 'canvas'){
            return _canvas
        }
    },
    createEvent:function(ele){
        console.log('document createEvent:::',ele)
    },
    all:_all,
    cookie:'__jdv=76161171|direct|-|none|-|1740717435794; __jdu=17407174357931755805150; 3AB9D23F7A4B3C9B=TMCSF47R7PGBYVJMC2DDA4BEFBN6LOXW2JZRXF5IT7YF5UYYFBCDTKXOPXDRTRQW4TZLCNHSV4XJLU2V3QZDSZUX4M; areaId=22; ipLoc-djd=22-1930-0-0; PCSYCityID=CN_510000_510100_0; shshshfpa=7dc04283-3264-44d3-0fe4-446527f9298f-1740717559; shshshfpx=7dc04283-3264-44d3-0fe4-446527f9298f-1740717559; o2State={%22webp%22:true%2C%22avif%22:true%2C%22lastvisit%22:1740792693834}; login_bottom_bar_count=1; __jda=76161171.17407174357931755805150.1740717436.1740799308.1740836843.5; __jdc=76161171; shshshfpb=BApXS-kr-UvBANuyTwCOqZ70tLRKcP5hVBgIwcnZp9xJ1MtMF3IG2; __jdb=76161171.4.17407174357931755805150|5.1740836843; 3AB9D23F7A4B3CSS=jdd03TMCSF47R7PGBYVJMC2DDA4BEFBN6LOXW2JZRXF5IT7YF5UYYFBCDTKXOPXDRTRQW4TZLCNHSV4XJLU2V3QZDSZUX4MAAAAMVKH4XSYAAAAAACPYS6JCLW7QGHYX; sdtoken=AAbEsBpEIOVjqTAKCQtvQu179pZ0Wt6YyJiPtGBvHT-2fEaqNpY9R67j-iEH5OCfC34pOta1_TmeLAGfFCZTeaM6FUIC00iFC31n00bMa4hERFgMsvy49kzDSnbV',
    body: _body,
    head:_head,
    documentElement: _documentElement,
    getElementsByTagName:function(ele){
        console.log('document getElementsByTagName:::',ele)
        if (ele == 'head'){
            return []
        }
    }

}
document.__proto__ = HTMLDocument.prototype



function Navigator(){}
window.Navigator=Navigator

navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
    webdriver:false,
    languages:[
        "zh-CN",
        "en",
        "en-GB",
        "en-US"
    ],
    plugins:{
        length:5,
    },
    platform: 'Win32',
    hardwareConcurrency:8,
}
navigator.__proto__ = Navigator.prototype


function Location(){}
window.Location=Location
location = {
    "ancestorOrigins": {},
    "href": "https://www.jd.com/",
    "origin": "https://www.jd.com",
    "protocol": "https:",
    "host": "www.jd.com",
    "hostname": "www.jd.com",
    "port": "",
    "pathname": "/",
    "search": "",
    "hash": ""
}
location.__proto__ = Location.prototype



function Storage(){}
window.Storage=Storage

localStorage = {
    getItem:function(ele){
        console.log('localStorage getItem:::',ele)
        if (ele == 'WQ_dy1_vk'){
            return '{"5.0":{"73806":{"e":31536000,"v":"wppax9scdrdpr3m6","t":1740717538097},"b5216":{"e":31536000,"v":"r99ax3swca9999p5","t":1740717543482}}}'
        }
        if (ele == 'WQ_gather_cv1'){
            return '{"v":"3fb777da864642050ee0bbb3a51937cf","t":1740836843357,"e":31536000}'
        }
        if (ele == 'WQ_dy1_tk_algo'){
            return '{"r99ax3swca9999p5":{"b5216":{"v":"eyJ0ayI6InRrMDN3NWQ3MzFhNzYxOG5USkhmSGVOV3BSNU9DX1U0NW5HMzU3NDZFNHRHaGJuLTJ5dVF2T1BEMEZxbEdMdjdOM012dkNCVXA1RkZRMXhIRGczZm9ha0lJLWdBIiwiYWxnbyI6ImZ1bmN0aW9uIHRlc3QodGssZnAsdHMsYWksYWxnbyl7dmFyIHJkPSdnbDB4dFFRZjFldWgnO3ZhciBzdHI9XCJcIi5jb25jYXQodGspLmNvbmNhdChmcCkuY29uY2F0KHRzKS5jb25jYXQoYWkpLmNvbmNhdChyZCk7cmV0dXJuIGFsZ28uTUQ1KHN0cik7fSJ9","e":86400,"t":1740836843631}},"wppax9scdrdpr3m6":{"73806":{"v":"eyJ0ayI6InRrMDN3YzM2ZTFjYzIxOG41RXl5Qk16NXhLYXBLRm8tWXljNVR5WW5TcGk1dzJjOWFRZW1YdmJEcW03WjJUZXNwMUNnemlOUDZRMy1iSU5FR1VkeklvSUtvaWFtIiwiYWxnbyI6ImZ1bmN0aW9uIHRlc3QodGssZnAsdHMsYWksYWxnbyl7dmFyIHJkPSc2WHJtVG5QZ1NqSWUnO3ZhciBzdHI9XCJcIi5jb25jYXQodGspLmNvbmNhdChmcCkuY29uY2F0KHRzKS5jb25jYXQoYWkpLmNvbmNhdChyZCk7cmV0dXJuIGFsZ28uTUQ1KHN0cik7fSJ9","e":86400,"t":1740836843633}}}'
        }
        if (ele == 'WQ_gather_wgl1'){
            return '{"v":"b2bffcfae898a7d97b93b3174a5c891a","t":1740836843375,"e":31536000}'
        }
    },
    setItem:function(ele){
        console.log('setItem',ele)
    }
}
localStorage.__proto__ = Storage.prototype