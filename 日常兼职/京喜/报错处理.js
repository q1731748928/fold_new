Error.prepareStackTrace = function (error, structuredStackTrace) {
    return `${error.name}: ${error.message}\n` + 
        structuredStackTrace
            .filter(callSite => !callSite.getFileName()?.startsWith("node:")) // 过滤掉 node:internal
            .map(callSite => `    at ${callSite.toString()}`)
            .join('\n');
};

// 测试代码
function testError() {
    throw new Error("test err");
}

try {
    testError();
} catch (e) {
    console.log(e.stack);
}