## 用法
```
//apply 
func.apply(thisArg, [argsArray])

//call
fun.call(thisArg, arg1, arg2, ...)

//bind
const newFun = fun.bind(thisArg, arg1, arg2, ...)
newFun()
```

## 手写apply
```
Function.prototype.myApply = function (context, args) {
    //这里默认不传就是给window,也可以用es6给参数设置默认参数
    context = context || window
    args = args ? args : []
    //给context新增一个独一无二的属性以免覆盖原有属性
    const key = Symbol()
    context[key] = this
    //通过隐式绑定的方式调用函数
    const result = context[key](...args)
    //删除添加的属性
    delete context[key]
    //返回函数调用的返回值
    return result
}
```

## 手写call

//实现1：
```
//传递参数从一个数组变成逐个传参了,不用...扩展运算符的也可以用arguments代替
Function.prototype.myCall = function (context, ...args) {
    //这里默认不传就是给window,也可以用es6给参数设置默认参数
    context = context || window
    args = args ? args : []
    //给context新增一个独一无二的属性以免覆盖原有属性
    const key = Symbol()
    context[key] = this
    //通过隐式绑定的方式调用函数
    const result = context[key](...args)
    //删除添加的属性
    delete context[key]
    //返回函数调用的返回值
    return result
}
```

实现2：
```
Function.prototype.mycall = function () {
  if(typeof this !== 'function'){
    throw 'caller must be a function'
  }
  let othis = arguments[0] || window
  othis._fn = this
  let arg = [...arguments].slice(1)
  let res = othis._fn(...arg)
  Reflect.deleteProperty(othis, '_fn') //删除_fn属性
  return res
}
```

## 手写bind

bind和apply的区别在于，bind是返回一个绑定好的函数，apply是直接调用；
其实想一想实现也很简单，就是返回一个函数，里面执行了apply上述的操作而已；
不过有一个需要判断的点，因为返回新的函数，要考虑到使用new去调用，并且new的优先级比较高，所以需要判断new的调用；
还有一个特点就是bind调用的时候可以传参，调用之后生成的新的函数也可以传参，效果是一样的,所以这一块也要做处理。

```
Function.prototype.myBind = function (context, ...args) {
    const fn = this
    args = args ? args : []
    return function newFn(...newFnArgs) {
        if (this instanceof newFn) {
            return new fn(...args, ...newFnArgs)
        }
        return fn.apply(context, [...args,...newFnArgs])
    }
}
```

面试感悟,手写bind,apply,call
https://juejin.im/post/5d2ddd9be51d4556d86c7b79

前端手写代码原理实现
https://juejin.im/post/5e47a19d518825494f7def52

this、apply、call、bind
https://juejin.im/post/59bfe84351882531b730bac2
