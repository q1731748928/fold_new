function hookRes(){
    var OkHttpClient = Java.use("okhttp3.OkHttpClient");
OkHttpClient.newCall.overload("okhttp3.Request").implementation = function (request) {
    console.log("HTTP Request -> " + request.url().toString());
    var call = this.newCall(request); // 获取新的 Call 对象
    var response = call.execute(); // 调用新的 Call 对象的 execute 方法
    console.log("HTTP Response -> " + response.body().string());
    // 根据响应  看栈

    return call
}
}

function hookInter(){
    var Builder = Java.use('okhttp3.OkHttpClient$Builder');
    Builder.addInterceptor.implementation = function (a) {
        console.log('a: ' + JSON.stringify(a))
        var res = this.addInterceptor(a);
        return res;
}
}
Java.perform(function () {
    hookRes()
    // hookHeader()
    // hookInter()
})
