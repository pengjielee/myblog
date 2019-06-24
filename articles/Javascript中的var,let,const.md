### 1、var声明
~~~
// demo11: 区域变量覆盖全局变量
var name = 'jim';
function f(){
	console.log(name)
	if(true){
		var name = 'tom'
	}
}
f(); // undefined

// demo12: 循环变量泄漏为全局变量
var str = 'hello';
for(var i=0; i < str.length; i++){
	console.log(str[i]);
}
console.log(i);
~~~


### 2、let/const
~~~
// demo21:
const name = 'hello'

function f(){
	console.log(name);
	if(true){
		const name = 'world'
		console.log(name)
	}
}
f();

output: 
hello 
world

// demo22:
const str = 'hello';
for(let i=0; i < str.length; i++){
	console.log(str[i]);
}
console.log(i); // Uncaught ReferenceError: i is not defined
~~~