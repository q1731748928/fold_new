HTMLAnchorElement = function (){}
HTMLAnchorElement.prototype.host = '';
HTMLAnchorElement.prototype.href = ''

document = {
        createElement: function(val){
            if(val === 'a'){
                return new HTMLAnchorElement("anlan_cE")
            }
        }
    }
_toString = Function.prototype.toString
Function.prototype.toString = function(val){
        debugger;
        if (this.name === 'createElement'){
            return 'function createElement() { [native code] }'
        }
        else if(this.name === ''){
            return 'function () { [native code] }'
        }
        else if(this.name === 'HTMLAnchorElement'){
            return 'function HTMLAnchorElement() { [native code] }'
        }
        else{
            _toString.apply(this, arguments)
        }
    }

// 非箭头函数 和 new的过程中 ， 谁调用指向谁

Object.defineProperty(HTMLAnchorElement.prototype, 'href', {
        set: function(){
            this.host = arguments[0].split('/').at(-1);
            this._HTMLAnchorElement_href = arguments[0];
            // return arguments[0]   // 这里不用return  等号表达式在解析的时候会自动向前赋值的，这里不需要return
        },
        get: function(){
            return this._HTMLAnchorElement_href;
        },
    })
HTMLAnchorElement = function (val) {
    debugger
    if (this instanceof HTMLAnchorElement) {
        if (val === "anlan_cE") {
            "这里写逻辑"
        } else {
            throw TypeError('Illegal constructor')
        }
    } else {
        throw TypeError(`Failed to construct 'HTMLAnchorElement': Please use the 'new' operator, this DOM object constructor cannot be called as a function`)
    }
};


a = document.createElement('a')
a.href = 'https://www.yuanrenxue.com'
console.log(a.host)