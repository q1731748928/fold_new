window = global;
navigator = {
    userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
}

getOwnPropertyDescriptor_ = Object.getOwnPropertyDescriptor
Object.getOwnPropertyDescriptor = function (obj, prop) {
    if (obj === navigator && prop === "webdriver") {
        return undefined
    }
    if (obj === navigator && prop === "userAgent") {
        return undefined
    }
    return getOwnPropertyDescriptor_(obj, prop)
}
