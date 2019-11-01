迭代器模式是指提供一种方法顺序访问一个聚合对象中的各个元素，而又不需要暴露改对象的内部表示。 

迭代器分为内部迭代器和外部迭代器。  
- 内部迭代器在调用的时候非常方便，外界不用关心迭代器内部的实现，跟迭代器的交互也仅仅是一次初始调用，但也是内部迭代器的缺点。
内部迭代器的迭代规则被提前规定。
- 外部迭代器必须显式地请求迭代下一个元素。
外部迭代器增加了调用的复杂度，但也增加了灵活性，我们可以手工控制迭代的过程或者顺序。

## 内部迭代器
~~~
Javascript each:
Array.prototype.forEach

JQuery each:
$.each();

$.each([2,3,4],function(index,item){ 
	console.log(item)
});

$.each({ id: '1',name: 'jack'},function(key,item){
	console.log(item)
});

myEach: 
function myEach(arr, callback){
	for(var i = 0; i < arr.length; i++){
		callback.call(arr[i],i,arr[i]);
	}
}

myEach([2,3,4],function(index,item){
	console.log(item)
});
~~~

## 外部迭代器
~~~
var Interator = function(obj){
	var current = 0;

	var next = function(){
		current += 1;
	}

	var isDone = function(){
		return current >= obj.length;
	}

	var getCurrItem = function(){
		return obj[current];
	}

	return {
		next : next,
		isDone : isDone,
		getCurrItem: getCurrItem,
		length: obj.length
	}
}
~~~

## 比较两个数组里的元素是否完全相同。

1. 内部迭代器实现：
~~~
var compare = function(arr1,arr2){
	if(arr1.length != arr2.length){
		throw new Error('not equal');
	}
	myEach(arr1, function(index,item){
		if(item !== arr2[index]){
			throw new Error('not equal');
		}
	});
	console.log('equal');
}
~~~

2. 外部迭代器实现：
~~~
var compare = function(interator1,interator2){
	if(interator1.length != interator2.length){
		throw new Error('not equal');
	}
	while(!interator1.isDone() && !interator2.isDone()){
		if(interator1.getCurrItem() !== interator2.getCurrItem()){
			throw new Error('not equal');
		}
		interator1.next();
		interator2.next();
	}
	console.log('equal');
}
~~~

## JQuery $.each()实现代码
~~~
$.each = function(obj,callback){
	var value, isArray = isArrayLike(obj);
	if(isArray){
		for(var i = 0; i < obj.length; i++){
			value = callback.call(obj[i],i,obj[i]);
			if(value === false) { break; }
		}
	}else{
		for(var i in obj){
			value = callback.call(obj[i],i,obj[i]);
			if(value === false) { break; }
		}
	}
	return obj;
}
~~~