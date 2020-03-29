### for  

```
var words = ['a', 'b', 'c']

for (let i = 0; i < words.length; i++) {
	console.log(words[i]) // a b c
}
```

### for... in  

The for... in statement iterates over all non - Symbol,enumerable properties of an object.

```
var people = {
	name: 'tom',
	age: 20,
	sex: 'male'
}

for (var key in people) {
	console.log(key) // name age sex
}
```

[MDN for... in](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in) 

### for...of

The for...of statement creates a loop iterating over iterable objects, including: built - inString, Array, Array - like objects(e.g., arguments or NodeList), TypedArray, Map, Set, and user - defined iterables.

```
// 遍历数组
var names = ['tom', 'jim']
for (let value of names) {
	console.log(value) // tom jim
}

// 遍历字符串
var words = "hello"
for (let value of words) {
	console.log(value) // h e l l o
}

// 遍历类型数组
var unitArr = new Uint8Array([0x00, 0xff]);
for (let value of unitArr) {
	console.log(value) // 0 255
}

// 遍历Map对象
var map = new Map([['a', 1], ['b', 2], ['c', 3]]) 
for (let value of map) {
	console.log(value) // ['a',1] ['b',2] ['c',3]
}

for (let[key, value] of map) {
	console.log(value) // 1 2 3
}

// 遍历Set对象
var set = new Set([1, 1, 2, 2, 3, 3]);
for (let value of set) {
	console.log(value) // 1 2 3
}

// 遍历arguments对象
(function() {
	for (let argument of arguments) {
		console.log(argument) // 1 2 3
	}
})(1, 2, 3)

// 遍历DOM对象
let lines = document.querySelectorAll('p.line')

for (let line of lines) {
	line.classList.add('read')
}
```

[MDN for...of](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of)  

### Array.prototype.forEach()

```
var words = ['a', 'b', 'c']

words.forEach(function(value, index) {
	console.log(value) // a b c
})
```

[MDN Array.prototype.forEach](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)

### $.each

```
var people = {
	name: 'tom',
	age: 20,
	sex: 'male'
}
var words = ['a', 'b', 'c']

$.each(people,
function(key, value) {
	console.log(key) // name age sex
});

$.each(words,
function(index, value) {
	console.log(value) // a b c
})

// $.each实现源码
$.each = function(obj, callback) {
	var length, i = 0;

	if (isArrayLike(obj)) {
		length = obj.length;
		for (; i < length; i++) {
			if (callback.call(obj[i], i, obj[i]) === false) {
				break;
			}
		}
	} else {
		for (i in obj) {
			if (callback.call(obj[i], i, obj[i]) === false) {
				break;
			}
		}
	}
	return obj;
}
```