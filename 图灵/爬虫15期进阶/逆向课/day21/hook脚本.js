Object.defineProperty(document, "cookie", {
    set: function name(params) {
        if (params.indexOf("acw_tc") != -1) {
            debugger;
        }
    }
})