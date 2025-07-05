var eE = function(eo) {
                    function eu(eo, eu) {
                        return eo << eu | eo >>> 32 - eu
                    }
                    function ep(eo, eu) {
                        var ep, em, e_, ew, eS;
                        return e_ = 2147483648 & eo,
                        ew = 2147483648 & eu,
                        ep = 1073741824 & eo,
                        em = 1073741824 & eu,
                        eS = (1073741823 & eo) + (1073741823 & eu),
                        ep & em ? 2147483648 ^ eS ^ e_ ^ ew : ep | em ? 1073741824 & eS ? 3221225472 ^ eS ^ e_ ^ ew : 1073741824 ^ eS ^ e_ ^ ew : eS ^ e_ ^ ew
                    }
                    function em(eo, eu, ep) {
                        return eo & eu | ~eo & ep
                    }
                    function e_(eo, eu, ep) {
                        return eo & ep | eu & ~ep
                    }
                    function ew(eo, eu, ep) {
                        return eo ^ eu ^ ep
                    }
                    function eS(eo, eu, ep) {
                        return eu ^ (eo | ~ep)
                    }
                    function eC(eo, e_, ew, eS, eC, eE, eT) {
                        return eo = ep(eo, ep(ep(em(e_, ew, eS), eC), eT)),
                        ep(eu(eo, eE), e_)
                    }
                    function eE(eo, em, ew, eS, eC, eE, eT) {
                        return eo = ep(eo, ep(ep(e_(em, ew, eS), eC), eT)),
                        ep(eu(eo, eE), em)
                    }
                    function eT(eo, em, e_, eS, eC, eE, eT) {
                        return eo = ep(eo, ep(ep(ew(em, e_, eS), eC), eT)),
                        ep(eu(eo, eE), em)
                    }
                    function eM(eo, em, e_, ew, eC, eE, eT) {
                        return eo = ep(eo, ep(ep(eS(em, e_, ew), eC), eT)),
                        ep(eu(eo, eE), em)
                    }
                    function eL(eo) {
                        var eu, ep = "", em = "";
                        for (eu = 0; 3 >= eu; eu++)
                            ep += (em = "0" + (eo >>> 8 * eu & 255).toString(16)).substr(em.length - 2, 2);
                        return ep
                    }
                    var eI, eA, eO, eP, eD, eN, eR, eF, eB, eY = [], eZ = 7, eH = 12, eW = 17, ez = 22, eU = 5, eV = 9, eQ = 14, eG = 20, eX = 4, eK = 11, eJ = 16, e$ = 23, e0 = 6, e2 = 10, e5 = 15, e7 = 21;
                    for (eY = function(eo) {
                        for (var eu, ep = eo.length, em = ep + 8, e_ = (em - em % 64) / 64, ew = 16 * (e_ + 1), eS = Array(ew - 1), eC = 0, eE = 0; ep > eE; )
                            eu = (eE - eE % 4) / 4,
                            eC = eE % 4 * 8,
                            eS[eu] = eS[eu] | eo.charCodeAt(eE) << eC,
                            eE++;
                        return eu = (eE - eE % 4) / 4,
                        eC = eE % 4 * 8,
                        eS[eu] = eS[eu] | 128 << eC,
                        eS[ew - 2] = ep << 3,
                        eS[ew - 1] = ep >>> 29,
                        eS
                    }(eo = function(eo) {
                        eo = eo.replace(/\r\n/g, "\n");
                        for (var eu = "", ep = 0; ep < eo.length; ep++) {
                            var em = eo.charCodeAt(ep);
                            128 > em ? eu += String.fromCharCode(em) : em > 127 && 2048 > em ? eu += String.fromCharCode(em >> 6 | 192) + String.fromCharCode(63 & em | 128) : eu += String.fromCharCode(em >> 12 | 224) + String.fromCharCode(em >> 6 & 63 | 128) + String.fromCharCode(63 & em | 128)
                        }
                        return eu
                    }(eo)),
                    eN = 1732584193,
                    eR = 4023233417,
                    eF = 2562383102,
                    eB = 271733878,
                    eI = 0; eI < eY.length; eI += 16)
                        eA = eN,
                        eO = eR,
                        eP = eF,
                        eD = eB,
                        eN = eC(eN, eR, eF, eB, eY[eI + 0], eZ, 3614090360),
                        eB = eC(eB, eN, eR, eF, eY[eI + 1], eH, 3905402710),
                        eF = eC(eF, eB, eN, eR, eY[eI + 2], eW, 606105819),
                        eR = eC(eR, eF, eB, eN, eY[eI + 3], ez, 3250441966),
                        eN = eC(eN, eR, eF, eB, eY[eI + 4], eZ, 4118548399),
                        eB = eC(eB, eN, eR, eF, eY[eI + 5], eH, 1200080426),
                        eF = eC(eF, eB, eN, eR, eY[eI + 6], eW, 2821735955),
                        eR = eC(eR, eF, eB, eN, eY[eI + 7], ez, 4249261313),
                        eN = eC(eN, eR, eF, eB, eY[eI + 8], eZ, 1770035416),
                        eB = eC(eB, eN, eR, eF, eY[eI + 9], eH, 2336552879),
                        eF = eC(eF, eB, eN, eR, eY[eI + 10], eW, 4294925233),
                        eR = eC(eR, eF, eB, eN, eY[eI + 11], ez, 2304563134),
                        eN = eC(eN, eR, eF, eB, eY[eI + 12], eZ, 1804603682),
                        eB = eC(eB, eN, eR, eF, eY[eI + 13], eH, 4254626195),
                        eF = eC(eF, eB, eN, eR, eY[eI + 14], eW, 2792965006),
                        eR = eC(eR, eF, eB, eN, eY[eI + 15], ez, 1236535329),
                        eN = eE(eN, eR, eF, eB, eY[eI + 1], eU, 4129170786),
                        eB = eE(eB, eN, eR, eF, eY[eI + 6], eV, 3225465664),
                        eF = eE(eF, eB, eN, eR, eY[eI + 11], eQ, 643717713),
                        eR = eE(eR, eF, eB, eN, eY[eI + 0], eG, 3921069994),
                        eN = eE(eN, eR, eF, eB, eY[eI + 5], eU, 3593408605),
                        eB = eE(eB, eN, eR, eF, eY[eI + 10], eV, 38016083),
                        eF = eE(eF, eB, eN, eR, eY[eI + 15], eQ, 3634488961),
                        eR = eE(eR, eF, eB, eN, eY[eI + 4], eG, 3889429448),
                        eN = eE(eN, eR, eF, eB, eY[eI + 9], eU, 568446438),
                        eB = eE(eB, eN, eR, eF, eY[eI + 14], eV, 3275163606),
                        eF = eE(eF, eB, eN, eR, eY[eI + 3], eQ, 4107603335),
                        eR = eE(eR, eF, eB, eN, eY[eI + 8], eG, 1163531501),
                        eN = eE(eN, eR, eF, eB, eY[eI + 13], eU, 2850285829),
                        eB = eE(eB, eN, eR, eF, eY[eI + 2], eV, 4243563512),
                        eF = eE(eF, eB, eN, eR, eY[eI + 7], eQ, 1735328473),
                        eR = eE(eR, eF, eB, eN, eY[eI + 12], eG, 2368359562),
                        eN = eT(eN, eR, eF, eB, eY[eI + 5], eX, 4294588738),
                        eB = eT(eB, eN, eR, eF, eY[eI + 8], eK, 2272392833),
                        eF = eT(eF, eB, eN, eR, eY[eI + 11], eJ, 1839030562),
                        eR = eT(eR, eF, eB, eN, eY[eI + 14], e$, 4259657740),
                        eN = eT(eN, eR, eF, eB, eY[eI + 1], eX, 2763975236),
                        eB = eT(eB, eN, eR, eF, eY[eI + 4], eK, 1272893353),
                        eF = eT(eF, eB, eN, eR, eY[eI + 7], eJ, 4139469664),
                        eR = eT(eR, eF, eB, eN, eY[eI + 10], e$, 3200236656),
                        eN = eT(eN, eR, eF, eB, eY[eI + 13], eX, 681279174),
                        eB = eT(eB, eN, eR, eF, eY[eI + 0], eK, 3936430074),
                        eF = eT(eF, eB, eN, eR, eY[eI + 3], eJ, 3572445317),
                        eR = eT(eR, eF, eB, eN, eY[eI + 6], e$, 76029189),
                        eN = eT(eN, eR, eF, eB, eY[eI + 9], eX, 3654602809),
                        eB = eT(eB, eN, eR, eF, eY[eI + 12], eK, 3873151461),
                        eF = eT(eF, eB, eN, eR, eY[eI + 15], eJ, 530742520),
                        eR = eT(eR, eF, eB, eN, eY[eI + 2], e$, 3299628645),
                        eN = eM(eN, eR, eF, eB, eY[eI + 0], e0, 4096336452),
                        eB = eM(eB, eN, eR, eF, eY[eI + 7], e2, 1126891415),
                        eF = eM(eF, eB, eN, eR, eY[eI + 14], e5, 2878612391),
                        eR = eM(eR, eF, eB, eN, eY[eI + 5], e7, 4237533241),
                        eN = eM(eN, eR, eF, eB, eY[eI + 12], e0, 1700485571),
                        eB = eM(eB, eN, eR, eF, eY[eI + 3], e2, 2399980690),
                        eF = eM(eF, eB, eN, eR, eY[eI + 10], e5, 4293915773),
                        eR = eM(eR, eF, eB, eN, eY[eI + 1], e7, 2240044497),
                        eN = eM(eN, eR, eF, eB, eY[eI + 8], e0, 1873313359),
                        eB = eM(eB, eN, eR, eF, eY[eI + 15], e2, 4264355552),
                        eF = eM(eF, eB, eN, eR, eY[eI + 6], e5, 2734768916),
                        eR = eM(eR, eF, eB, eN, eY[eI + 13], e7, 1309151649),
                        eN = eM(eN, eR, eF, eB, eY[eI + 4], e0, 4149444226),
                        eB = eM(eB, eN, eR, eF, eY[eI + 11], e2, 3174756917),
                        eF = eM(eF, eB, eN, eR, eY[eI + 2], e5, 718787259),
                        eR = eM(eR, eF, eB, eN, eY[eI + 9], e7, 3951481745),
                        eN = ep(eN, eA),
                        eR = ep(eR, eO),
                        eF = ep(eF, eP),
                        eB = ep(eB, eD);
                    return (eL(eN) + eL(eR) + eL(eF) + eL(eB)).toLowerCase()
                }
s = '12574478'
get_f = function (params,token,time) {
    r = {
        "H5Request": true,
        "WindVaneRequest": false,
        "useJsonpResultType": false,
        "safariGoLogin": true,
        "useAlipayJSBridge": false,
        "mainDomain": "taobao.com",
        "subDomain": "m",
        "prefix": "h5api",
        "getJSONP": true,
        "token": token,
    }
    l = eE(r.token+ "&" + time + "&" + s + "&" + params)
    f = {
        jsv: "2.7.4",
        appKey: s,
        t: time,
        sign: l
    }
    console.log(f)
    return f
}
console.log(get_f());