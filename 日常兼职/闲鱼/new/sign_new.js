function get_sign(params, token, time) {
    l = "12574478"
    var u = function (e) {
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

        function r(e, r, o, i, a, l, s) {
            return e = n(e, n(n(function (e, t, n) {
                return e & t | ~e & n
            }(r, o, i), a), s)),
                n(t(e, l), r)
        }

        function o(e, r, o, i, a, l, s) {
            return e = n(e, n(n(function (e, t, n) {
                return e & n | t & ~n
            }(r, o, i), a), s)),
                n(t(e, l), r)
        }

        function i(e, r, o, i, a, l, s) {
            return e = n(e, n(n(function (e, t, n) {
                return e ^ t ^ n
            }(r, o, i), a), s)),
                n(t(e, l), r)
        }

        function a(e, r, o, i, a, l, s) {
            return e = n(e, n(n(function (e, t, n) {
                return t ^ (e | ~n)
            }(r, o, i), a), s)),
                n(t(e, l), r)
        }

        function l(e) {
            var t, n = "", r = "";
            for (t = 0; 3 >= t; t++)
                n += (r = "0" + (e >>> 8 * t & 255).toString(16)).substr(r.length - 2, 2);
            return n
        }

        var s, u, c, f, d, p, h, m, g, v;
        for (e = function (e) {
            e = e.replace(/\r\n/g, "\n");
            for (var t = "", n = 0; n < e.length; n++) {
                var r = e.charCodeAt(n);
                128 > r ? t += String.fromCharCode(r) : r > 127 && 2048 > r ? (t += String.fromCharCode(r >> 6 | 192),
                    t += String.fromCharCode(63 & r | 128)) : (t += String.fromCharCode(r >> 12 | 224),
                    t += String.fromCharCode(r >> 6 & 63 | 128),
                    t += String.fromCharCode(63 & r | 128))
            }
            return t
        }(e),
                 v = function (e) {
                     for (var t, n = e.length, r = n + 8, o = 16 * ((r - r % 64) / 64 + 1), i = new Array(o - 1), a = 0, l = 0; n > l;)
                         a = l % 4 * 8,
                             i[t = (l - l % 4) / 4] = i[t] | e.charCodeAt(l) << a,
                             l++;
                     return a = l % 4 * 8,
                         i[t = (l - l % 4) / 4] = i[t] | 128 << a,
                         i[o - 2] = n << 3,
                         i[o - 1] = n >>> 29,
                         i
                 }(e),
                 p = 1732584193,
                 h = 4023233417,
                 m = 2562383102,
                 g = 271733878,
                 s = 0; s < v.length; s += 16)
            u = p,
                c = h,
                f = m,
                d = g,
                p = r(p, h, m, g, v[s + 0], 7, 3614090360),
                g = r(g, p, h, m, v[s + 1], 12, 3905402710),
                m = r(m, g, p, h, v[s + 2], 17, 606105819),
                h = r(h, m, g, p, v[s + 3], 22, 3250441966),
                p = r(p, h, m, g, v[s + 4], 7, 4118548399),
                g = r(g, p, h, m, v[s + 5], 12, 1200080426),
                m = r(m, g, p, h, v[s + 6], 17, 2821735955),
                h = r(h, m, g, p, v[s + 7], 22, 4249261313),
                p = r(p, h, m, g, v[s + 8], 7, 1770035416),
                g = r(g, p, h, m, v[s + 9], 12, 2336552879),
                m = r(m, g, p, h, v[s + 10], 17, 4294925233),
                h = r(h, m, g, p, v[s + 11], 22, 2304563134),
                p = r(p, h, m, g, v[s + 12], 7, 1804603682),
                g = r(g, p, h, m, v[s + 13], 12, 4254626195),
                m = r(m, g, p, h, v[s + 14], 17, 2792965006),
                p = o(p, h = r(h, m, g, p, v[s + 15], 22, 1236535329), m, g, v[s + 1], 5, 4129170786),
                g = o(g, p, h, m, v[s + 6], 9, 3225465664),
                m = o(m, g, p, h, v[s + 11], 14, 643717713),
                h = o(h, m, g, p, v[s + 0], 20, 3921069994),
                p = o(p, h, m, g, v[s + 5], 5, 3593408605),
                g = o(g, p, h, m, v[s + 10], 9, 38016083),
                m = o(m, g, p, h, v[s + 15], 14, 3634488961),
                h = o(h, m, g, p, v[s + 4], 20, 3889429448),
                p = o(p, h, m, g, v[s + 9], 5, 568446438),
                g = o(g, p, h, m, v[s + 14], 9, 3275163606),
                m = o(m, g, p, h, v[s + 3], 14, 4107603335),
                h = o(h, m, g, p, v[s + 8], 20, 1163531501),
                p = o(p, h, m, g, v[s + 13], 5, 2850285829),
                g = o(g, p, h, m, v[s + 2], 9, 4243563512),
                m = o(m, g, p, h, v[s + 7], 14, 1735328473),
                p = i(p, h = o(h, m, g, p, v[s + 12], 20, 2368359562), m, g, v[s + 5], 4, 4294588738),
                g = i(g, p, h, m, v[s + 8], 11, 2272392833),
                m = i(m, g, p, h, v[s + 11], 16, 1839030562),
                h = i(h, m, g, p, v[s + 14], 23, 4259657740),
                p = i(p, h, m, g, v[s + 1], 4, 2763975236),
                g = i(g, p, h, m, v[s + 4], 11, 1272893353),
                m = i(m, g, p, h, v[s + 7], 16, 4139469664),
                h = i(h, m, g, p, v[s + 10], 23, 3200236656),
                p = i(p, h, m, g, v[s + 13], 4, 681279174),
                g = i(g, p, h, m, v[s + 0], 11, 3936430074),
                m = i(m, g, p, h, v[s + 3], 16, 3572445317),
                h = i(h, m, g, p, v[s + 6], 23, 76029189),
                p = i(p, h, m, g, v[s + 9], 4, 3654602809),
                g = i(g, p, h, m, v[s + 12], 11, 3873151461),
                m = i(m, g, p, h, v[s + 15], 16, 530742520),
                p = a(p, h = i(h, m, g, p, v[s + 2], 23, 3299628645), m, g, v[s + 0], 6, 4096336452),
                g = a(g, p, h, m, v[s + 7], 10, 1126891415),
                m = a(m, g, p, h, v[s + 14], 15, 2878612391),
                h = a(h, m, g, p, v[s + 5], 21, 4237533241),
                p = a(p, h, m, g, v[s + 12], 6, 1700485571),
                g = a(g, p, h, m, v[s + 3], 10, 2399980690),
                m = a(m, g, p, h, v[s + 10], 15, 4293915773),
                h = a(h, m, g, p, v[s + 1], 21, 2240044497),
                p = a(p, h, m, g, v[s + 8], 6, 1873313359),
                g = a(g, p, h, m, v[s + 15], 10, 4264355552),
                m = a(m, g, p, h, v[s + 6], 15, 2734768916),
                h = a(h, m, g, p, v[s + 13], 21, 1309151649),
                p = a(p, h, m, g, v[s + 4], 6, 4149444226),
                g = a(g, p, h, m, v[s + 11], 10, 3174756917),
                m = a(m, g, p, h, v[s + 2], 15, 718787259),
                h = a(h, m, g, p, v[s + 9], 21, 3951481745),
                p = n(p, u),
                h = n(h, c),
                m = n(m, f),
                g = n(g, d);
        return (l(p) + l(h) + l(m) + l(g)).toLowerCase()
    }(token + "&" + time + "&" + l + "&" + params)
    return u
}

sign = get_sign('{"pageNumber":1,"piUrl":"https://2.taobao.com/search?word=%E4%BA%8C%E6%89%8B%E6%89%8B%E6%9C%BA&spm=a2170.xianyu_tbpc_search.0.0"}', "67d4c5674d9fd8a9dcbb977224da25b3", 1746872885266);
console.log(sign)