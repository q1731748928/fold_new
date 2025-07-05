function main() {
    Java.perform(function () {

    let j = Java.use("com.dianping.nvnetwork.j");
    j["g"].implementation = function () {
        console.log(`j.g is called`);
        let result = this["g"]();
        console.log(`j.g result=${result}`);
        return 3;
    };

    })
}

setImmediate(main)
