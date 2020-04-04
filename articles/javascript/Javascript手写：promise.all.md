在实现 Promise.all 方法之前，我们首先要知道 Promise.all 的功能和特点，因为在清楚了 Promise.all 功能和特点的情况下，我们才能进一步去写实现。

## Promise.all 功能

Promise.all(iterable) 返回一个新的 Promise 实例。此实例在 iterable 参数内所有的 promise 都 fulfilled 或者参数中不包含 promise 时，状态变成 fulfilled；如果参数中 promise 有一个失败 rejected，此实例回调失败，失败原因的是第一个失败 promise 的返回结果。

```
let p = Promise.all([p1, p2, p3]);
```

p的状态由 p1,p2,p3决定，分成以下；两种情况：
（1）只有p1、p2、p3的状态都变成 fulfilled，p的状态才会变成 fulfilled，此时p1、p2、p3的返回值组成一个数组，传递给p的回调函数。
（2）只要p1、p2、p3之中有一个被 rejected，p的状态就变成 rejected，此时第一个被reject的实例的返回值，会传递给p的回调函数。

## Promise.all 的特点

Promise.all 的返回值是一个 promise 实例
- 如果传入的参数为空的可迭代对象， Promise.all 会 同步 返回一个已完成状态的 promise
- 如果传入的参数中不包含任何 promise, Promise.all 会 异步 返回一个已完成状态的 promise
- 其它情况下， Promise.all 返回一个 处理中（pending） 状态的 promise.

## Promise.all 返回的 promise 的状态

- 如果传入的参数中的 promise 都变成完成状态， Promise.all 返回的 promise 异步地变为完成。
- 如果传入的参数中，有一个 promise 失败， Promise.all 异步地将失败的那个结果给失败状态的回调函数，而不管其它 promise 是否完成
- 在任何情况下， Promise.all 返回的 promise 的完成状态的结果都是一个数组

## Promise.all 实现
```
Promise.all = function(promises){
	// promises 是可迭代对象，省略参数合法性检查
	return new Promise((resolve,reject) => {
		// Array.from 将可迭代对象转换成数组
		promises = Array.from(promises);
		if(promises.length === 0){
			resolve([]);
		} else {
			let result = [];
			let index = 0;
			for(let i = 0; i < promises.length; i++){
				// 考虑到i可能是thenable对象也可能是普通值
				Promise.resolve(promises[i]).then(data => {
					result[i] = data;
					if(++index === promises.length) {
						// 所有的promises状态都是fulfilled，promise.all返回的实例才变成fulfilled态
						resolve(result);
					}
				}, err => {
					reject(err);
					return;
				});
			}
		} 
	})
}
```
