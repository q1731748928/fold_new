function main() {
    Java.perform(function () {
        var nvnetwork_g = Java.use("com.dianping.nvnetwork.g");
nvnetwork_g.g.overload().implementation = function(){
    console.log("----------------------------- Hook g()---------------------------");
    return 3;
}
    })
}

Java.perform(function () {
    main()
    // hook()
// hookSign()
    // 主动调用
    // let Utils  = Java.use("com.dodonew.online.util.Utils");
    // var res  =Utils.md5("1")
    // console.log(res )

})