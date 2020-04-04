new 的实现原理:

1. 创建一个空对象，构造函数中的this指向这个空对象
2. 这个新对象被执行 [[原型]] 连接
3. 执行构造函数方法，属性和方法被添加到this引用的对象中
4. 如果构造函数中没有返回其它对象，那么返回this，即创建的这个的新对象，否则，返回构造函数中返回的对象。

```
function _new() {
	let target = {}; //创建的空对象
	let [constructor, ...args] = [...arguments];
	// 执行[[原型]]连接；target 是 constructor 的实例
	target.__proto__ == constructor.prototype;
	// 执行构造函数，将属性或方法添加到创建的空对象上
	let result = constructor.apply(target,args);
	if(result && (typeof result == "object" || typeof result == 'function')){
		// 如果构造函数执行的结构返回的是一个对象，那么返回这个对象
		return result;
	}
	// 如果构造函数执行的结构返回的不是一个对象，返回创建的新对象
	return target;
}
```