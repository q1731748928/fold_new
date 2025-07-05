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
function get_x_zse_96(tf) {
    ta = "101_3_3.0"
    tc = null
    td = t6(te)
    tu = "ATCSzTbe1xiPTtvwldcuQDzEc7yQczUbxog=|1719583518"
    // tp = [ta, tf, tu, false && td, tc].filter(Boolean).join("+");
    // tp = [ta, tf, tu, t8(td) && td, tc].filter(Boolean).join("+");
    tp = ta + "+" + tf.replace("https://www.zhihu.com","") + "+" + tu
    // if(tp.endsWith("+")) {
    //     tp = tp.replace("+","")
    // }
    // return tp
    // console.log(tp)
    // return tp
    // return crypto.MD5(tp).toString()
    // console.log(yuan.loader(1514)['ZP'](crypto.MD5(tp).toString()));
    return "2.0_" + yuan.loader(1514)['ZP'](crypto.MD5(tp).toString())

}
//
// console.log(get_x_zse_96("https://www.zhihu.com/api/v4/comment_v5/answers/2840205362/root_comment?order_by=score&limit=20&offset="));
// 'pDsj7Ovq/PMlI80cR7+lDnsT/6beTQWM+JjteAYyi/dsS+1WCbj2Htm4tknUgJhp'

// 101_3_3.0+/api/v4/questions/277135177/concerned_followers?limit=7&offset=0+ATCSzTbe1xiPTtvwldcuQDzEc7yQczUbxog=|1719583518
// 101_3_3.0+/api/v4/comment_v5/answers/3190774612/root_comment?order_by=score&limit=20&offset=+ATCSzTbe1xiPTtvwldcuQDzEc7yQczUbxog=|1719583518"
// get_x_zse_96('https://www.zhihu.com/api/v4/questions/277135177/feeds?cursor=7dbafc43e574bba9b3faa2ab9ccda815&include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Creaction_instruction%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%2A%5D.author.follower_count%2Cvip_info%2Ckvip_info%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=1&order=default&platform=desktop&session_id=1745288135828820257&ws_qiangzhisafe=0+ATCSzTbe1xiPTtvwldcuQDzEc7yQczUbxog%3D%7C1719583518')
