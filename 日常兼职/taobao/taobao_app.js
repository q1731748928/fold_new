u = (new Date).getTime()
s = "12574478"
n = {
    "api": "mtop.relationrecommend.wirelessrecommend.recommend",
    "v": "2.0",
    "data": "{\"appId\":\"34385\",\"params\":\"{\\\"device\\\":\\\"HMA-AL00\\\",\\\"isBeta\\\":\\\"false\\\",\\\"grayHair\\\":\\\"false\\\",\\\"from\\\":\\\"nt_history\\\",\\\"brand\\\":\\\"HUAWEI\\\",\\\"info\\\":\\\"wifi\\\",\\\"index\\\":\\\"4\\\",\\\"rainbow\\\":\\\"\\\",\\\"schemaType\\\":\\\"auction\\\",\\\"elderHome\\\":\\\"false\\\",\\\"isEnterSrpSearch\\\":\\\"true\\\",\\\"newSearch\\\":\\\"false\\\",\\\"network\\\":\\\"wifi\\\",\\\"subtype\\\":\\\"\\\",\\\"hasPreposeFilter\\\":\\\"false\\\",\\\"prepositionVersion\\\":\\\"v2\\\",\\\"client_os\\\":\\\"Android\\\",\\\"gpsEnabled\\\":\\\"false\\\",\\\"searchDoorFrom\\\":\\\"srp\\\",\\\"debug_rerankNewOpenCard\\\":\\\"false\\\",\\\"homePageVersion\\\":\\\"v7\\\",\\\"searchElderHomeOpen\\\":\\\"false\\\",\\\"search_action\\\":\\\"initiative\\\",\\\"sugg\\\":\\\"_4_1\\\",\\\"sversion\\\":\\\"13.6\\\",\\\"style\\\":\\\"list\\\",\\\"ttid\\\":\\\"600000@taobao_pc_10.7.0\\\",\\\"needTabs\\\":\\\"true\\\",\\\"areaCode\\\":\\\"CN\\\",\\\"vm\\\":\\\"nw\\\",\\\"countryNum\\\":\\\"156\\\",\\\"m\\\":\\\"pc\\\",\\\"page\\\":1,\\\"n\\\":48,\\\"q\\\":\\\"%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91\\\",\\\"tab\\\":\\\"all\\\",\\\"pageSize\\\":48,\\\"totalPage\\\":100,\\\"totalResults\\\":4800,\\\"sourceS\\\":\\\"0\\\",\\\"sort\\\":\\\"_coefp\\\",\\\"bcoffset\\\":\\\"\\\",\\\"ntoffset\\\":\\\"\\\",\\\"filterTag\\\":\\\"\\\",\\\"service\\\":\\\"\\\",\\\"prop\\\":\\\"\\\",\\\"loc\\\":\\\"\\\",\\\"start_price\\\":null,\\\"end_price\\\":null,\\\"startPrice\\\":null,\\\"endPrice\\\":null,\\\"itemIds\\\":null,\\\"p4pIds\\\":null,\\\"categoryp\\\":\\\"\\\"}\"}",
    "type": "get",
    "dataType": "jsonp"
}

function c(e) {
    function t(e, t) {
        return e << t | e >>> 32 - t
    }

    function n(e, t) {
        var n, r, o, i, a;
        return o = 2147483648 & e,
            i = 2147483648 & t,
            a = (1073741823 & e) + (1073741823 & t),
            (n = 1073741824 & e) & (r = 1073741824 & t) ? 2147483648 ^ a ^ o ^ i : n | r ? 1073741824 & a ? 3221225472 ^ a ^ o ^ i : 1073741824 ^ a ^ o ^ i : a ^ o ^ i
    }

    function r(e, t, n) {
        return e & t | ~e & n
    }

    function o(e, t, n) {
        return e & n | t & ~n
    }

    function i(e, t, n) {
        return e ^ t ^ n
    }

    function a(e, t, n) {
        return t ^ (e | ~n)
    }

    function s(e, o, i, a, s, u, c) {
        return e = n(e, n(n(r(o, i, a), s), c)),
            n(t(e, u), o)
    }

    function u(e, r, i, a, s, u, c) {
        return e = n(e, n(n(o(r, i, a), s), c)),
            n(t(e, u), r)
    }

    function c(e, r, o, a, s, u, c) {
        return e = n(e, n(n(i(r, o, a), s), c)),
            n(t(e, u), r)
    }

    function l(e, r, o, i, s, u, c) {
        return e = n(e, n(n(a(r, o, i), s), c)),
            n(t(e, u), r)
    }

    function f(e) {
        for (var t, n = e.length, r = n + 8, o, i = 16 * ((r - r % 64) / 64 + 1), a = new Array(i - 1), s = 0, u = 0; n > u;)
            s = u % 4 * 8,
                a[t = (u - u % 4) / 4] = a[t] | e.charCodeAt(u) << s,
                u++;
        return s = u % 4 * 8,
            a[t = (u - u % 4) / 4] = a[t] | 128 << s,
            a[i - 2] = n << 3,
            a[i - 1] = n >>> 29,
            a
    }

    function d(e) {
        var t, n, r = "", o = "";
        for (n = 0; 3 >= n; n++)
            r += (o = "0" + (t = e >>> 8 * n & 255).toString(16)).substr(o.length - 2, 2);
        return r
    }

    function p(e) {
        e = e.replace(/\r\n/g, "\n");
        for (var t = "", n = 0; n < e.length; n++) {
            var r = e.charCodeAt(n);
            128 > r ? t += String.fromCharCode(r) : r > 127 && 2048 > r ? (t += String.fromCharCode(r >> 6 | 192),
                t += String.fromCharCode(63 & r | 128)) : (t += String.fromCharCode(r >> 12 | 224),
                t += String.fromCharCode(r >> 6 & 63 | 128),
                t += String.fromCharCode(63 & r | 128))
        }
        return t
    }

    var h, m, y, v, g, b, _, w, S, x = [], M = 7, k = 12, L = 17, O = 22, T = 5, E = 9, j = 14, P = 20, C = 4, A = 11,
        D = 16, N = 23, Y = 6, I = 10, R = 15, F = 21, H;
    for (x = f(e = p(e)),
             b = 1732584193,
             _ = 4023233417,
             w = 2562383102,
             S = 271733878,
             h = 0; h < x.length; h += 16)
        m = b,
            y = _,
            v = w,
            g = S,
            b = s(b, _, w, S, x[h + 0], 7, 3614090360),
            S = s(S, b, _, w, x[h + 1], k, 3905402710),
            w = s(w, S, b, _, x[h + 2], L, 606105819),
            _ = s(_, w, S, b, x[h + 3], O, 3250441966),
            b = s(b, _, w, S, x[h + 4], 7, 4118548399),
            S = s(S, b, _, w, x[h + 5], k, 1200080426),
            w = s(w, S, b, _, x[h + 6], L, 2821735955),
            _ = s(_, w, S, b, x[h + 7], O, 4249261313),
            b = s(b, _, w, S, x[h + 8], 7, 1770035416),
            S = s(S, b, _, w, x[h + 9], k, 2336552879),
            w = s(w, S, b, _, x[h + 10], L, 4294925233),
            _ = s(_, w, S, b, x[h + 11], O, 2304563134),
            b = s(b, _, w, S, x[h + 12], 7, 1804603682),
            S = s(S, b, _, w, x[h + 13], k, 4254626195),
            w = s(w, S, b, _, x[h + 14], L, 2792965006),
            b = u(b, _ = s(_, w, S, b, x[h + 15], O, 1236535329), w, S, x[h + 1], 5, 4129170786),
            S = u(S, b, _, w, x[h + 6], 9, 3225465664),
            w = u(w, S, b, _, x[h + 11], j, 643717713),
            _ = u(_, w, S, b, x[h + 0], P, 3921069994),
            b = u(b, _, w, S, x[h + 5], 5, 3593408605),
            S = u(S, b, _, w, x[h + 10], 9, 38016083),
            w = u(w, S, b, _, x[h + 15], j, 3634488961),
            _ = u(_, w, S, b, x[h + 4], P, 3889429448),
            b = u(b, _, w, S, x[h + 9], 5, 568446438),
            S = u(S, b, _, w, x[h + 14], 9, 3275163606),
            w = u(w, S, b, _, x[h + 3], j, 4107603335),
            _ = u(_, w, S, b, x[h + 8], P, 1163531501),
            b = u(b, _, w, S, x[h + 13], 5, 2850285829),
            S = u(S, b, _, w, x[h + 2], 9, 4243563512),
            w = u(w, S, b, _, x[h + 7], j, 1735328473),
            b = c(b, _ = u(_, w, S, b, x[h + 12], P, 2368359562), w, S, x[h + 5], 4, 4294588738),
            S = c(S, b, _, w, x[h + 8], A, 2272392833),
            w = c(w, S, b, _, x[h + 11], D, 1839030562),
            _ = c(_, w, S, b, x[h + 14], N, 4259657740),
            b = c(b, _, w, S, x[h + 1], 4, 2763975236),
            S = c(S, b, _, w, x[h + 4], A, 1272893353),
            w = c(w, S, b, _, x[h + 7], D, 4139469664),
            _ = c(_, w, S, b, x[h + 10], N, 3200236656),
            b = c(b, _, w, S, x[h + 13], 4, 681279174),
            S = c(S, b, _, w, x[h + 0], A, 3936430074),
            w = c(w, S, b, _, x[h + 3], D, 3572445317),
            _ = c(_, w, S, b, x[h + 6], N, 76029189),
            b = c(b, _, w, S, x[h + 9], 4, 3654602809),
            S = c(S, b, _, w, x[h + 12], A, 3873151461),
            w = c(w, S, b, _, x[h + 15], D, 530742520),
            b = l(b, _ = c(_, w, S, b, x[h + 2], N, 3299628645), w, S, x[h + 0], 6, 4096336452),
            S = l(S, b, _, w, x[h + 7], I, 1126891415),
            w = l(w, S, b, _, x[h + 14], R, 2878612391),
            _ = l(_, w, S, b, x[h + 5], F, 4237533241),
            b = l(b, _, w, S, x[h + 12], 6, 1700485571),
            S = l(S, b, _, w, x[h + 3], I, 2399980690),
            w = l(w, S, b, _, x[h + 10], R, 4293915773),
            _ = l(_, w, S, b, x[h + 1], F, 2240044497),
            b = l(b, _, w, S, x[h + 8], 6, 1873313359),
            S = l(S, b, _, w, x[h + 15], I, 4264355552),
            w = l(w, S, b, _, x[h + 6], R, 2734768916),
            _ = l(_, w, S, b, x[h + 13], F, 1309151649),
            b = l(b, _, w, S, x[h + 4], 6, 4149444226),
            S = l(S, b, _, w, x[h + 11], I, 3174756917),
            w = l(w, S, b, _, x[h + 2], R, 718787259),
            _ = l(_, w, S, b, x[h + 9], F, 3951481745),
            b = n(b, m),
            _ = n(_, y),
            w = n(w, v),
            S = n(S, g);
    return (d(b) + d(_) + d(w) + d(S)).toLowerCase()
}

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
    l = c(r.token+ "&" + time + "&" + s + "&" + params)
    f = {
        jsv: "2.7.2",
        appKey: s,
        t: time,
        sign: l
    }
    console.log(f)
    return f
}
console.log(get_f());

