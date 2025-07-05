var CryptoJS = require('crypto-js')
const RV = "zxcvbnmlkjhgfdsaqwertyuiop0987654321QWERTYUIOPLKJHGFDSAZXCVBNM"
  , oQe = RV + "-@#$%^&*+!";
function rQe(e, t) {
    switch (arguments.length) {
    case 1:
        return parseInt(Math.random() * e + 1, 10);
    case 2:
        return parseInt(Math.random() * (t - e + 1) + e, 10);
    default:
        return 0
    }
}
function aQe(e) {
    return [...Array(e)].map( () => RV[rQe(0, 61)]).join("")
}
function sQe(e) {
    let t = "";
    return typeof e == "object" ? t = Object.keys(e).map(n => `${n}=${e[n]}`).sort().join("&") : typeof e == "string" && (t = e.split("&").sort().join("&")),
    t
}
function dg(e={}) {
    const {p: t, t: n, n: r, k: o} = e
      , a = sQe(t);
    return CryptoJS.SHA256(r + o + decodeURIComponent(a) + n)
}
u = {
    data: {
        "type": "trading-type",
        "publishStartTime": "",
        "publishEndTime": "",
        "keyword": "",
        "thirdType": 10,
        "siteCode": "44",
        "secondType": "A",
        "projectType": "",
        "dateType": "",
        "searchType": "pf",
        "total": 304,
        "pageNo": 3,
        "pageSize": 10,
        "totals": 304,
        "openConvert": false
    }
}
Aa = function() {
    for (var e = [], t = 0; t < 256; ++t)
        e.push("%" + ((t < 16 ? "0" : "") + t.toString(16)).toUpperCase());
    return e
}()
DAe = function(t, n, r, o, a) {
    if (t.length === 0)
        return t;
    var s = t;
    if (typeof t == "symbol" ? s = Symbol.prototype.toString.call(t) : typeof t != "string" && (s = String(t)),
    r === "iso-8859-1")
        return escape(s).replace(/%u[0-9a-f]{4}/gi, function(c) {
            return "%26%23" + parseInt(c.slice(2), 16) + "%3B"
        });
    for (var i = "", u = 0; u < s.length; ++u) {
        var l = s.charCodeAt(u);
        if (l === 45 || l === 46 || l === 95 || l === 126 || l >= 48 && l <= 57 || l >= 65 && l <= 90 || l >= 97 && l <= 122 || a === AAe.RFC1738 && (l === 40 || l === 41)) {
            i += s.charAt(u);
            continue
        }
        if (l < 128) {
            i = i + Aa[l];
            continue
        }
        if (l < 2048) {
            i = i + (Aa[192 | l >> 6] + Aa[128 | l & 63]);
            continue
        }
        if (l < 55296 || l >= 57344) {
            i = i + (Aa[224 | l >> 12] + Aa[128 | l >> 6 & 63] + Aa[128 | l & 63]);
            continue
        }
        u += 1,
        l = 65536 + ((l & 1023) << 10 | s.charCodeAt(u) & 1023),
        i += Aa[240 | l >> 18] + Aa[128 | l >> 12 & 63] + Aa[128 | l >> 6 & 63] + Aa[128 | l & 63]
    }
    return i
}
oR = function(t, n) {
    for (var r = n && n.plainObjects ? Object.create(null) : {}, o = 0; o < t.length; ++o)
        typeof t[o] < "u" && (r[o] = t[o]);
    return r
}
BAe = function(t, n) {
    return Object.keys(n).reduce(function(r, o) {
        return r[o] = n[o],
        r
    }, t)
}
TAe = function(t, n) {
    return [].concat(t, n)
}
kAe = function(t) {
    for (var n = [{
        obj: {
            o: t
        },
        prop: "o"
    }], r = [], o = 0; o < n.length; ++o)
        for (var a = n[o], s = a.obj[a.prop], i = Object.keys(s), u = 0; u < i.length; ++u) {
            var l = i[u]
              , c = s[l];
            typeof c == "object" && c !== null && r.indexOf(c) === -1 && (n.push({
                obj: s,
                prop: l
            }),
            r.push(c))
        }
    return FAe(n),
    t
}
SAe = function(e, t, n) {
    var r = e.replace(/\+/g, " ");
    if (n === "iso-8859-1")
        return r.replace(/%[0-9a-f]{2}/gi, unescape);
    try {
        return decodeURIComponent(r)
    } catch {
        return r
    }
}
$Ae = function(t) {
    return !t || typeof t != "object" ? !1 : !!(t.constructor && t.constructor.isBuffer && t.constructor.isBuffer(t))
}
xAe = function(t) {
    return Object.prototype.toString.call(t) === "[object RegExp]"
}
OAe = function(t, n) {
    if (tu(t)) {
        for (var r = [], o = 0; o < t.length; o += 1)
            r.push(n(t[o]));
        return r
    }
    return n(t)
}
_Ae = function e(t, n, r) {
    if (!n)
        return t;
    if (typeof n != "object") {
        if (tu(t))
            t.push(n);
        else if (t && typeof t == "object")
            (r && (r.plainObjects || r.allowPrototypes) || !d3.call(Object.prototype, n)) && (t[n] = !0);
        else
            return [t, n];
        return t
    }
    if (!t || typeof t != "object")
        return [t].concat(n);
    var o = t;
    return tu(t) && !tu(n) && (o = oR(t, r)),
    tu(t) && tu(n) ? (n.forEach(function(a, s) {
        if (d3.call(t, s)) {
            var i = t[s];
            i && typeof i == "object" && a && typeof a == "object" ? t[s] = e(i, a, r) : t.push(a)
        } else
            t[s] = a
    }),
    t) : Object.keys(n).reduce(function(a, s) {
        var i = n[s];
        return d3.call(a, s) ? a[s] = e(a[s], i, r) : a[s] = i,
        a
    }, o)
}
aR = {
    arrayToObject: oR,
    assign: BAe,
    combine: TAe,
    compact: kAe,
    decode: SAe,
    encode: DAe,
    isBuffer: $Ae,
    isRegExp: xAe,
    maybeMap: OAe,
    merge: _Ae
}
c3 = {
    RFC1738: "RFC1738",
    RFC3986: "RFC3986"
}
x8 = {
    default: c3.RFC3986,
    formatters: {
        RFC1738: function(e) {
            return wAe.call(e, EAe, "+")
        },
        RFC3986: function(e) {
            return String(e)
        }
    },
    RFC1738: c3.RFC1738,
    RFC3986: c3.RFC3986
}
AAe = x8
af = x8
S = af.default
qS = af.default
Uh = aR
ss = Array.isArray
wr = {
    addQueryPrefix: !1,
    allowDots: !1,
    charset: "utf-8",
    charsetSentinel: !1,
    delimiter: "&",
    encode: !0,
    encoder: Uh.encode,
    encodeValuesOnly: !1,
    format: qS,
    formatter: af.formatters[qS],
    indices: !1,
    serializeDate: function(t) {
        return IAe.call(t)
    },
    skipNulls: !1,
    strictNullHandling: !1
}
RAe = function(t) {
    if (!t)
        return wr;
    if (t.encoder !== null && typeof t.encoder < "u" && typeof t.encoder != "function")
        throw new TypeError("Encoder has to be a function.");
    var n = t.charset || wr.charset;
    if (typeof t.charset < "u" && t.charset !== "utf-8" && t.charset !== "iso-8859-1")
        throw new TypeError("The charset option must be either utf-8, iso-8859-1, or undefined");
    var r = af.default;
    if (typeof t.format < "u") {
        if (!MAe.call(af.formatters, t.format))
            throw new TypeError("Unknown format option provided.");
        r = t.format
    }
    var o = af.formatters[r]
      , a = wr.filter;
    return (typeof t.filter == "function" || ss(t.filter)) && (a = t.filter),
    {
        addQueryPrefix: typeof t.addQueryPrefix == "boolean" ? t.addQueryPrefix : wr.addQueryPrefix,
        allowDots: typeof t.allowDots > "u" ? wr.allowDots : !!t.allowDots,
        charset: n,
        charsetSentinel: typeof t.charsetSentinel == "boolean" ? t.charsetSentinel : wr.charsetSentinel,
        delimiter: typeof t.delimiter > "u" ? wr.delimiter : t.delimiter,
        encode: typeof t.encode == "boolean" ? t.encode : wr.encode,
        encoder: typeof t.encoder == "function" ? t.encoder : wr.encoder,
        encodeValuesOnly: typeof t.encodeValuesOnly == "boolean" ? t.encodeValuesOnly : wr.encodeValuesOnly,
        filter: a,
        format: r,
        formatter: o,
        serializeDate: typeof t.serializeDate == "function" ? t.serializeDate : wr.serializeDate,
        skipNulls: typeof t.skipNulls == "boolean" ? t.skipNulls : wr.skipNulls,
        sort: typeof t.sort == "function" ? t.sort : null,
        strictNullHandling: typeof t.strictNullHandling == "boolean" ? t.strictNullHandling : wr.strictNullHandling
    }
}
YS = {
    brackets: function(t) {
        return t + "[]"
    },
    comma: "comma",
    indices: function(t, n) {
        return t + "[" + n + "]"
    },
    repeat: function(t) {
        return t
    }
}
A8 = Function.prototype.bind
xp = A8
m7e = A8
_7e = xp.call(Function.call, RegExp.prototype.exec)
OS = xp.call(Function.call, String.prototype.replace)
W2 = xp.call(Function.call, String.prototype.slice)
B7e = /[^%.[\]]+|\[(?:(-?\d+(?:\.\d+)?)|(["'])((?:(?!\2)[^\\]|\\.)*?)\2)\]|(?=(?:\.|\[\])(?:\.|\[\]|%$))/g
D7e = function(t) {
    var n = W2(t, 0, 1)
      , r = W2(t, -1);
    if (n === "%" && r !== "%")
        throw new hc("invalid intrinsic syntax, expected closing `%`");
    if (r === "%" && n !== "%")
        throw new hc("invalid intrinsic syntax, expected opening `%`");
    var o = [];
    return OS(t, B7e, function(a, s, i, u) {
        o[o.length] = i ? OS(u, S7e, "$1") : s || a
    }),
    o
}
g7e = m7e.call(Function.call, Object.prototype.hasOwnProperty)
j2 = g7e
TS = {
    "%ArrayBufferPrototype%": ["ArrayBuffer", "prototype"],
    "%ArrayPrototype%": ["Array", "prototype"],
    "%ArrayProto_entries%": ["Array", "prototype", "entries"],
    "%ArrayProto_forEach%": ["Array", "prototype", "forEach"],
    "%ArrayProto_keys%": ["Array", "prototype", "keys"],
    "%ArrayProto_values%": ["Array", "prototype", "values"],
    "%AsyncFunctionPrototype%": ["AsyncFunction", "prototype"],
    "%AsyncGenerator%": ["AsyncGeneratorFunction", "prototype"],
    "%AsyncGeneratorPrototype%": ["AsyncGeneratorFunction", "prototype", "prototype"],
    "%BooleanPrototype%": ["Boolean", "prototype"],
    "%DataViewPrototype%": ["DataView", "prototype"],
    "%DatePrototype%": ["Date", "prototype"],
    "%ErrorPrototype%": ["Error", "prototype"],
    "%EvalErrorPrototype%": ["EvalError", "prototype"],
    "%Float32ArrayPrototype%": ["Float32Array", "prototype"],
    "%Float64ArrayPrototype%": ["Float64Array", "prototype"],
    "%FunctionPrototype%": ["Function", "prototype"],
    "%Generator%": ["GeneratorFunction", "prototype"],
    "%GeneratorPrototype%": ["GeneratorFunction", "prototype", "prototype"],
    "%Int8ArrayPrototype%": ["Int8Array", "prototype"],
    "%Int16ArrayPrototype%": ["Int16Array", "prototype"],
    "%Int32ArrayPrototype%": ["Int32Array", "prototype"],
    "%JSONParse%": ["JSON", "parse"],
    "%JSONStringify%": ["JSON", "stringify"],
    "%MapPrototype%": ["Map", "prototype"],
    "%NumberPrototype%": ["Number", "prototype"],
    "%ObjectPrototype%": ["Object", "prototype"],
    "%ObjProto_toString%": ["Object", "prototype", "toString"],
    "%ObjProto_valueOf%": ["Object", "prototype", "valueOf"],
    "%PromisePrototype%": ["Promise", "prototype"],
    "%PromiseProto_then%": ["Promise", "prototype", "then"],
    "%Promise_all%": ["Promise", "all"],
    "%Promise_reject%": ["Promise", "reject"],
    "%Promise_resolve%": ["Promise", "resolve"],
    "%RangeErrorPrototype%": ["RangeError", "prototype"],
    "%ReferenceErrorPrototype%": ["ReferenceError", "prototype"],
    "%RegExpPrototype%": ["RegExp", "prototype"],
    "%SetPrototype%": ["Set", "prototype"],
    "%SharedArrayBufferPrototype%": ["SharedArrayBuffer", "prototype"],
    "%StringPrototype%": ["String", "prototype"],
    "%SymbolPrototype%": ["Symbol", "prototype"],
    "%SyntaxErrorPrototype%": ["SyntaxError", "prototype"],
    "%TypedArrayPrototype%": ["TypedArray", "prototype"],
    "%TypeErrorPrototype%": ["TypeError", "prototype"],
    "%Uint8ArrayPrototype%": ["Uint8Array", "prototype"],
    "%Uint8ClampedArrayPrototype%": ["Uint8ClampedArray", "prototype"],
    "%Uint16ArrayPrototype%": ["Uint16Array", "prototype"],
    "%Uint32ArrayPrototype%": ["Uint32Array", "prototype"],
    "%URIErrorPrototype%": ["URIError", "prototype"],
    "%WeakMapPrototype%": ["WeakMap", "prototype"],
    "%WeakSetPrototype%": ["WeakSet", "prototype"]
}
u7e = function() {
    return typeof xS != "function" || typeof Symbol != "function" || typeof xS("foo") != "symbol" || typeof Symbol("bar") != "symbol" ? !1 : i7e()
}
ol = u7e()
var dn
Cl = {}
qN = Function
hc = SyntaxError
yu = Object.getOwnPropertyDescriptor;
$S = {
    foo: {}
}
l7e = Object, c7e = function() {
    return {
        __proto__: $S
    }.foo === $S.foo && !({
        __proto__: null
    }instanceof l7e)
}
c7e = function() {
    return {
        __proto__: $S
    }.foo === $S.foo && !({
        __proto__: null
    }instanceof l7e)
}
ir = Object.getPrototypeOf || (b7e ? function(e) {
    return e.__proto__
}
: null)
C7e = typeof Uint8Array > "u" || !ir ? dn : ir(Uint8Array)
y7e = yu ? function() {
    try {
        return arguments.callee,
        a3
    } catch {
        try {
            return yu(arguments, "callee").get
        } catch {
            return a3
        }
    }
}() : a3
  , ol = u7e()
  , b7e = c7e()
  , ir = Object.getPrototypeOf || (b7e ? function(e) {
    return e.__proto__
}
: null)
Hl = TypeError
bu = {
    "%AggregateError%": typeof AggregateError > "u" ? dn : AggregateError,
    "%Array%": Array,
    "%ArrayBuffer%": typeof ArrayBuffer > "u" ? dn : ArrayBuffer,
    "%ArrayIteratorPrototype%": ol && ir ? ir([][Symbol.iterator]()) : dn,
    "%AsyncFromSyncIteratorPrototype%": dn,
    "%AsyncFunction%": Cl,
    "%AsyncGenerator%": Cl,
    "%AsyncGeneratorFunction%": Cl,
    "%AsyncIteratorPrototype%": Cl,
    "%Atomics%": typeof Atomics > "u" ? dn : Atomics,
    "%BigInt%": typeof BigInt > "u" ? dn : BigInt,
    "%BigInt64Array%": typeof BigInt64Array > "u" ? dn : BigInt64Array,
    "%BigUint64Array%": typeof BigUint64Array > "u" ? dn : BigUint64Array,
    "%Boolean%": Boolean,
    "%DataView%": typeof DataView > "u" ? dn : DataView,
    "%Date%": Date,
    "%decodeURI%": decodeURI,
    "%decodeURIComponent%": decodeURIComponent,
    "%encodeURI%": encodeURI,
    "%encodeURIComponent%": encodeURIComponent,
    "%Error%": Error,
    "%eval%": eval,
    "%EvalError%": EvalError,
    "%Float32Array%": typeof Float32Array > "u" ? dn : Float32Array,
    "%Float64Array%": typeof Float64Array > "u" ? dn : Float64Array,
    "%FinalizationRegistry%": typeof FinalizationRegistry > "u" ? dn : FinalizationRegistry,
    "%Function%": qN,
    "%GeneratorFunction%": Cl,
    "%Int8Array%": typeof Int8Array > "u" ? dn : Int8Array,
    "%Int16Array%": typeof Int16Array > "u" ? dn : Int16Array,
    "%Int32Array%": typeof Int32Array > "u" ? dn : Int32Array,
    "%isFinite%": isFinite,
    "%isNaN%": isNaN,
    "%IteratorPrototype%": ol && ir ? ir(ir([][Symbol.iterator]())) : dn,
    "%JSON%": typeof JSON == "object" ? JSON : dn,
    "%Map%": typeof Map > "u" ? dn : Map,
    "%MapIteratorPrototype%": typeof Map > "u" || !ol || !ir ? dn : ir(new Map()[Symbol.iterator]()),
    "%Math%": Math,
    "%Number%": Number,
    "%Object%": Object,
    "%parseFloat%": parseFloat,
    "%parseInt%": parseInt,
    "%Promise%": typeof Promise > "u" ? dn : Promise,
    "%Proxy%": typeof Proxy > "u" ? dn : Proxy,
    "%RangeError%": RangeError,
    "%ReferenceError%": ReferenceError,
    "%Reflect%": typeof Reflect > "u" ? dn : Reflect,
    "%RegExp%": RegExp,
    "%Set%": typeof Set > "u" ? dn : Set,
    "%SetIteratorPrototype%": typeof Set > "u" || !ol || !ir ? dn : ir(new Set()[Symbol.iterator]()),
    "%SharedArrayBuffer%": typeof SharedArrayBuffer > "u" ? dn : SharedArrayBuffer,
    "%String%": String,
    "%StringIteratorPrototype%": ol && ir ? ir(""[Symbol.iterator]()) : dn,
    "%Symbol%": ol ? Symbol : dn,
    "%SyntaxError%": hc,
    "%ThrowTypeError%": y7e,
    "%TypedArray%": C7e,
    "%TypeError%": Hl,
    "%Uint8Array%": typeof Uint8Array > "u" ? dn : Uint8Array,
    "%Uint8ClampedArray%": typeof Uint8ClampedArray > "u" ? dn : Uint8ClampedArray,
    "%Uint16Array%": typeof Uint16Array > "u" ? dn : Uint16Array,
    "%Uint32Array%": typeof Uint32Array > "u" ? dn : Uint32Array,
    "%URIError%": URIError,
    "%WeakMap%": typeof WeakMap > "u" ? dn : WeakMap,
    "%WeakRef%": typeof WeakRef > "u" ? dn : WeakRef,
    "%WeakSet%": typeof WeakSet > "u" ? dn : WeakSet
}
k7e = function(t, n) {
    var r = t, o;
    if (j2(TS, r) && (o = TS[r],
    r = "%" + o[0] + "%"),
    j2(bu, r)) {
        var a = bu[r];
        if (a === Cl && (a = E7e(r)),
        typeof a > "u" && !n)
            throw new Hl("intrinsic " + t + " exists, but is not available. Please file an issue!");
        return {
            alias: o,
            name: r,
            value: a
        }
    }
    throw new hc("intrinsic " + t + " does not exist!")
}
F8 = function(t, n) {
    if (typeof t != "string" || t.length === 0)
        throw new Hl("intrinsic name must be a non-empty string");
    if (arguments.length > 1 && typeof n != "boolean")
        throw new Hl('"allowMissing" argument must be a boolean');
    if (_7e(/^%?[^%]*%?$/, t) === null)
        throw new hc("`%` may not be present anywhere but at the beginning and end of the intrinsic name");
    var r = D7e(t)
      , o = r.length > 0 ? r[0] : ""
      , a = k7e("%" + o + "%", n)
      , s = a.name
      , i = a.value
      , u = !1
      , l = a.alias;
    l && (o = l[0],
    F7e(r, A7e([0, 1], l)));
    for (var c = 1, f = !0; c < r.length; c += 1) {
        var p = r[c]
          , h = W2(p, 0, 1)
          , m = W2(p, -1);
        if ((h === '"' || h === "'" || h === "`" || m === '"' || m === "'" || m === "`") && h !== m)
            throw new hc("property names with quotes must have matching quotes");
        if ((p === "constructor" || !f) && (u = !0),
        o += "." + p,
        s = "%" + o + "%",
        j2(bu, s))
            i = bu[s];
        else if (i != null) {
            if (!(p in i)) {
                if (!n)
                    throw new Hl("base intrinsic for " + t + " exists, but the property is not available.");
                return
            }
            if (yu && c + 1 >= r.length) {
                var v = yu(i, p);
                f = !!v,
                f && "get"in v && !("originalValue"in v.get) ? i = v.get : i = i[p]
            } else
                f = j2(i, p),
                i = i[p];
            f && !u && (bu[s] = i)
        }
    }
    return i
}
D8 = F8
$0 = D8("%WeakMap%", !0)
CAe = function() {
    var t, n, r, o = {
        assert: function(a) {
            if (!o.has(a))
                throw new cAe("Side channel does not contain " + lAe(a))
        },
        get: function(a) {
            if ($0 && a && (typeof a == "object" || typeof a == "function")) {
                if (t)
                    return dAe(t, a)
            } else if (T0) {
                if (n)
                    return hAe(n, a)
            } else if (r)
                return gAe(r, a)
        },
        has: function(a) {
            if ($0 && a && (typeof a == "object" || typeof a == "function")) {
                if (t)
                    return pAe(t, a)
            } else if (T0) {
                if (n)
                    return mAe(n, a)
            } else if (r)
                return bAe(r, a);
            return !1
        },
        set: function(a, s) {
            $0 && a && (typeof a == "object" || typeof a == "function") ? (t || (t = new $0),
            fAe(t, a, s)) : T0 ? (n || (n = new T0),
            vAe(n, a, s)) : (r || (r = {
                key: {},
                next: null
            }),
            yAe(r, a, s))
        }
    };
    return o
}
sR = CAe
PAe = Array.prototype.push
iR = function(e, t) {
    PAe.apply(e, ss(t) ? t : [t])
}
zAe = function(e, t) {
    var n = e, r = RAe(t), o, a;
    typeof r.filter == "function" ? (a = r.filter,
    n = a("", n)) : ss(r.filter) && (a = r.filter,
    o = a);
    var s = [];
    if (typeof n != "object" || n === null)
        return "";
    var i;
    t && t.arrayFormat in YS ? i = t.arrayFormat : t && "indices"in t ? i = t.indices ? "indices" : "repeat" : i = "indices";
    var u = YS[i];
    if (t && "commaRoundTrip"in t && typeof t.commaRoundTrip != "boolean")
        throw new TypeError("`commaRoundTrip` must be a boolean, or absent");
    var l = u === "comma" && t && t.commaRoundTrip;
    o || (o = Object.keys(n)),
    r.sort && o.sort(r.sort);
    for (var c = sR(), f = 0; f < o.length; ++f) {
        var p = o[f];
        r.skipNulls && n[p] === null || iR(s, NAe(n[p], p, u, l, r.strictNullHandling, r.skipNulls, r.encode ? r.encoder : null, r.filter, r.sort, r.allowDots, r.serializeDate, r.format, r.formatter, r.encodeValuesOnly, r.charset, c))
    }
    var h = s.join(r.delimiter)
      , m = r.addQueryPrefix === !0 ? "?" : "";
    return r.charsetSentinel && (r.charset === "iso-8859-1" ? m += "utf8=%26%2310003%3B&" : m += "utf8=%E2%9C%93&"),
    h.length > 0 ? m + h : ""
}
f3 = {}
LAe = function(t) {
    return typeof t == "string" || typeof t == "number" || typeof t == "boolean" || typeof t == "symbol" || typeof t == "bigint"
}
NAe = function e(t, n, r, o, a, s, i, u, l, c, f, p, h, m, v, b) {
    for (var g = t, C = b, y = 0, F = !1; (C = C.get(f3)) !== void 0 && !F; ) {
        var S = C.get(t);
        if (y += 1,
        typeof S < "u") {
            if (S === y)
                throw new RangeError("Cyclic object value");
            F = !0
        }
        typeof C.get(f3) > "u" && (y = 0)
    }
    if (typeof u == "function" ? g = u(n, g) : g instanceof Date ? g = f(g) : r === "comma" && ss(g) && (g = Uh.maybeMap(g, function(K) {
        return K instanceof Date ? f(K) : K
    })),
    g === null) {
        if (a)
            return i && !m ? i(n, wr.encoder, v, "key", p) : n;
        g = ""
    }
    if (LAe(g) || Uh.isBuffer(g)) {
        if (i) {
            var _ = m ? n : i(n, wr.encoder, v, "key", p);
            return [h(_) + "=" + h(i(g, wr.encoder, v, "value", p))]
        }
        return [h(n) + "=" + h(String(g))]
    }
    var E = [];
    if (typeof g > "u")
        return E;
    var T;
    if (r === "comma" && ss(g))
        m && i && (g = Uh.maybeMap(g, i)),
        T = [{
            value: g.length > 0 ? g.join(",") || null : void 0
        }];
    else if (ss(u))
        T = u;
    else {
        var M = Object.keys(g);
        T = l ? M.sort(l) : M
    }
    for (var P = o && ss(g) && g.length === 1 ? n + "[]" : n, H = 0; H < T.length; ++H) {
        var j = T[H]
          , V = typeof j == "object" && typeof j.value < "u" ? j.value : g[j];
        if (!(s && V === null)) {
            var Y = ss(g) ? typeof r == "function" ? r(P, j) : P : P + (c ? "." + j : "[" + j + "]");
            b.set(t, y);
            var Z = sR();
            Z.set(f3, b),
            iR(E, e(V, Y, r, o, a, s, r === "comma" && m && ss(g) ? null : i, u, l, c, f, p, h, m, v, Z))
        }
    }
    return E
}
p = Date.now()
h = aQe(16)
function ts(e=[]) {
    return e.map(t => oQe[t]).join("")
}
u ={
    "transitional": {
        "silentJSONParsing": true,
        "forcedJSONParsing": true,
        "clarifyTimeoutError": false
    },
    "adapter": "xhr",
    "transformRequest": [
        null
    ],
    "transformResponse": [
        null
    ],
    "timeout": 30000,
    "xsrfCookieName": "XSRF-TOKEN",
    "xsrfHeaderName": "X-XSRF-TOKEN",
    "maxContentLength": -1,
    "maxBodyLength": -1,
    "env": {},
    "headers": {
        "Accept": "application/json, text/plain, */*",
        "Vtoken": "8f8ffeb3aae74bd6b8f18766c44f1f01"
    },
    "baseURL": "/ztbjg-portal/center/",
    "paramsSerializer": {},
    "method": "post",
    "url": "notice/search",
    "data": {
        "type": "trading-type",
        "publishStartTime": "",
        "publishEndTime": "",
        "keyword": "中",
        "thirdType": 10,
        "siteCode": "44",
        "secondType": "A",
        "projectType": "",
        "dateType": "",
        "searchType": "pf",
        "total": 3686,
        "pageNo": 2,
        "pageSize": 10,
        "totals": 3686,
        "openConvert": false
    }
}
function get_data(u) {
    p = Date.now()
    h = aQe(16)
    m = ts([59, 11, 31, 37, 9, 65, 33, 42, 15, 41, 12])
    v = {
            [ts([56, 62, 52, 11, 23, 62, 39, 18, 16, 62, 54, 25, 25])]: ts([0, 20, 4, 9, 11, 62, 25, 24, 19, 20, 15, 7]),
            [ts([56, 62, 52, 11, 23, 62, 39, 18, 16, 62, 60, 24, 5, 2, 18])]: h,
            [ts([56, 62, 52, 11, 23, 62, 39, 18, 16, 62, 40, 23, 6, 18, 14, 20, 15, 6, 25])]: p
        };
    const b = dg({
                p: zAe(u.data, {
                    allowDots: !0
                }),
                t: p,
                n: h,
                k: m
            }).toString();
    const s = dg({
            p: "",
            t: p,
            n: h,
            k: m
        }).toString()
            v[[ts([56, 62, 52, 11, 23, 62, 39, 18, 16, 62, 53, 23, 11, 5, 15, 20, 22, 19, 18])]] = b
            v[[ts([56, 62, 52, 11, 23, 62, 39, 18, 16, 62, 53, 23, 11, 5, 15, 20, 22, 19, 18, 14])]] = s
    return v;
}
console.log(get_data(u));
