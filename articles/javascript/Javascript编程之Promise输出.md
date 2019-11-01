1、  
~~~
const promise = new Promise((resolve, reject) => {
  console.log(1)
  resolve()
  console.log(2)
})
promise.then(() => {
  console.log(3)
})
console.log(4)

运行结果： 
1 
2 
4 
3 

解释：
Promise 构造函数是同步执行的，promise.then 中的函数是异步执行的。
~~~

2、   
~~~
const promise1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('success')
  }, 1000)
})
const promise2 = promise1.then(() => {
  throw new Error('error!!!')
})

console.log('promise1', promise1)
console.log('promise2', promise2)

setTimeout(() => {
  console.log('promise1', promise1)
  console.log('promise2', promise2)
}, 2000)

运行结果： 
promise1 Promise {<pending>}   
promise2 Promise {<pending>} 
Uncaught (in promise) Error: error!!!
    at promise1.then (<anonymous>:7:9)
promise1 Promise {<resolved>: "success"}
promise2 Promise {<rejected>: Error: error!!!
    at promise1.then (<anonymous>:7:9)}

解释： ?
~~~

3、
~~~
const promise = new Promise((resolve, reject) => {
  resolve('success1')
  reject('error')
  resolve('success2')
})

promise
  .then((res) => {
    console.log('then: ', res)
  })
  .catch((err) => {
    console.log('catch: ', err)
  })

运行结果：  
then: success1

解释：  
构造函数中的resolve或reject只有在第1次执行时有效，多次调用没有任何作用，promise状态一旦改变则不能再变。
~~~

4、 
~~~
Promise.resolve(1)
  .then((res) => {
    console.log(res)
    return 2
  })
  .catch((err) => {
    return 3
  })
  .then((res) => {
    console.log(res)
  })

运行结果： 
1
2

解释： 
promise可以链式调用。提起链式调用我们通常会想到通过return this实现，不过Promise并不是这样实现的。promise在每次调用.then或者.catch时都会返回一个新的promise，从而可以实现链式调用。
~~~

5、 
~~~
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    console.log('once')
    resolve('success')
  }, 1000)
})

const start = Date.now()
promise.then((res) => {
  console.log(res, Date.now() - start)
})
promise.then((res) => {
  console.log(res, Date.now() - start)
})

运行结果： 
once
success 1002
success 1002

解释：promise的.then或者.catch可以被调用多次，但这里Promise构造函数只执行一次。或者说，promise内部状态一经改变，并且有了一个值，则后续在每次调用.then或者.catch时都会直接拿到该值。
~~~

6、  
~~~
Promise.resolve()
  .then(() => {
    return new Error('error!!!')
  })
  .then((res) => {
    console.log('then: ', res)
  })
  .catch((err) => {
    console.log('catch: ', err)
  })

运行结果： 
then:  Error: error!!!
    at Promise.resolve.then (<anonymous>:3:12)


解释：.then或者.catch中return一个error对象并不会抛出错误，所以不会被后续的.catch捕获，需要改成如下其中一种：
a. return Promise.reject(new Error('error!!!'))
b. throw new Error('error!!!')

因为返回任意一个非promise的值都会被包裹成promise对象，即return new Error('error!!!') 等价于 return Promise.resolve(new Error('error!!!'))。
~~~


7、 
~~~
const promise = Promise.resolve()
  .then(() => {
    return promise
  })
promise.catch(console.error)

运行结果：  
TypeError: Chaining cycle detected for promise #<Promise>

解释：  
.then或.catch返回的值不能是promise本身，否则会造成死循环。

~~~

8、  
~~~
Promise.resolve(1)
  .then(2)
  .then(Promise.resolve(3))
  .then(console.log)

运行结果：
1

解释：  
.then或者.catch的参数期望是函数，传入非函数则会发生值穿透。
~~~

9、 
~~~
Promise.resolve()
  .then(function success (res) {
    throw new Error('error')
  }, function fail1 (e) {
    console.error('fail1: ', e)
  })
  .catch(function fail2 (e) {
    console.error('fail2: ', e)
  })

运行结果：
fail2:  Error: error
    at success (<anonymous>:3:11)

解释：  
.then可以接收两个参数，第1个是处理成功的函数，第2个是处理错误的函数。
.catch是.then第2个参数的简便写法，但是在用法上有一点需要注意：.then的第2个处理错误的函数（fail1）捕获不了第1个处理成功的函数（success）抛出的错误，而后续的.catch方法（fail2）可以捕获之前的错误。


以下代码也可以： 
Promise.resolve()
  .then(function success1 (res) {
    throw new Error('error')
  }, function fail1 (e) {
    console.error('fail1: ', e)
  })
  .then(function success2 (res) {
  }, function fail2 (e) {
    console.error('fail2: ', e)
  })

运行结果：
fail2:  Error: error
    at success (<anonymous>:3:11)
~~~

10、 
~~~
process.nextTick(() => {
  console.log('nextTick')
})
Promise.resolve()
  .then(() => {
    console.log('then')
  })
setImmediate(() => {
  console.log('setImmediate')
})
console.log('end')

运行结果：  
end
nextTick
then
setImmediate

解释：process.nextTick和promise.then都属于microtask，而setImmediate属于macrotask，在事件循环的check阶段执行。事件循环的每个阶段（macrotask）之间都会执行microtask，以上代码本身（macrotask）在执行完后会执行一次microtask。
~~~

源：  
[https://github.com/nswbmw/node-in-debugging/blob/master/3.1%20Promise.md](https://github.com/nswbmw/node-in-debugging/blob/master/3.1%20Promise.md)  
