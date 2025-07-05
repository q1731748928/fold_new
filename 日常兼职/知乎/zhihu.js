require("./env")
require("./mod")
require("./loader")
var crypto = require("crypto-js")
t6 = function(tt) {
            return null == tt ? "" : "string" == typeof tt ? tt : "undefined" != typeof URLSearchParams && (0,
            tc._)(tt, URLSearchParams) ? tt.toString() : tA()(tt) ? JSON.stringify(tt) : t4(tt) ? String(tt) : ""
        },
te = undefined
t8 = function(tt, te) {
            return void 0 === te && (te = 4096),
            !!tt && t7(tt) <= te
        }
// 测试代码
function get_x_zse_96(tf, _para) {
    ta = "101_3_3.0"
    tc = null
    td = t6(te)
    tu = "ATCSzTbe1xiPTtvwldcuQDzEc7yQczUbxog=|1719583518"
    // tp = [ta, tf, tu, false && td, tc].filter(Boolean).join("+");
    // tp = [ta, tf, tu, t8(td) && td, tc].filter(Boolean).join("+");
    tp = ta + "+" + tf.replace("https://www.zhihu.com","") + "+" + tu + "+" + _para
    // if(tp.endsWith("+")) {
    //     tp = tp.replace("+","")
    // }
    // return tp
    // console.log(tp)
    // return tp
    // return crypto.MD5(tp).toString()
    // console.log(yuan.loader(1514)['ZP'](crypto.MD5('5926537b4439043ff3918bbfebbb32c3').toString()));
    return "2.0_" + yuan.loader(1514)['ZP'](crypto.MD5(tp).toString())

}
//
// console.log(get_x_zse_96("https://www.zhihu.com/api/v4/comment_v5/answers/2840205362/root_comment?order_by=score&limit=20&offset="));
// 'pDsj7Ovq/PMlI80cR7+lDnsT/6beTQWM+JjteAYyi/dsS+1WCbj2Htm4tknUgJhp'

// 101_3_3.0+/api/v4/questions/277135177/concerned_followers?limit=7&offset=0+ATCSzTbe1xiPTtvwldcuQDzEc7yQczUbxog=|1719583518
// 101_3_3.0+/api/v4/comment_v5/answers/3190774612/root_comment?order_by=score&limit=20&offset=+ATCSzTbe1xiPTtvwldcuQDzEc7yQczUbxog=|1719583518"

