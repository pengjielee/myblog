### 作为对象的方法调用

当函数作为对象的方法被调用时，this指向该对象。

~~~
var person = {
	name: "kate",
	sayHi: function(){
		console.log('hello')
	}
}

person.sayHi(); // 'hello'
~~~

### 作为普通函数调用

当函数不作为对象的属性被调用时，也就是普通函数方式，此时的this总是指向全局对象。

~~~
window.color = "red";

var myColor = {
	color: "blue",
	getColor: function(){
		return this.color;
	}
}

console.log(myColor.getColor()) // blue

var getColor = myColor.getColor;
console.log(getColor()) // red
~~~

### 构造函数调用

所谓构造函数，就是通过这个函数生成一个新对象（object）。这时，this就指这个新对象。

~~~
function Animal(name){
	this.name = name || 'kate';
	this.sayHi = function(){
		console.log('hi, i am ' + this.name)
	}
}

var cat = new Animal('cate');
cat.sayHi(); //hi, i am cate
~~~

### apply调用

apply()是函数对象的一个方法，它的作用是改变函数的调用对象，它的第一个参数就表示改变后的调用这个函数的对象。因此，this指的就是这第一个参数。

~~~
var color = 'red';

function getColor(){
	console.log(this.color);
}

var obj = {};
obj.color = 'blue';
obj.getColor = getColor;

obj.getColor(); //blue
obj.getColor.apply(); // red
obj.getColor.apply(obj); // blue
obj.getColor.apply(window); // red
~~~