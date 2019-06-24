JavaScript有5种简单数据类型：Undefined、Null、Boolean、Number和String。还有1种复杂数据类型：Object。


### 判断数组
~~~
function isArray( value ){
	return Object.prototype.toString.call(value) === '[object Array]'
}

function isArray( value ){
	return Array.isArray(value)
}

isArray([]); //true
isArray(new Array(2)); //true
~~~

### 判断函数
~~~
function isFunction( value ){
	return typeof value === 'function';
}

function isFunction( value ){
	return Object.prototype.toString.call(value) === '[object Function]'
}

isFunction(function(){}); //true
~~~

### 判断对象
~~~
function isObject( value ){
	return value != null && ( typeof value === 'object' || typeof value === 'function' )
}

isObject({}); //true


// 空对象，不包括任何可枚举(自定义)的属性。
function isEmptyObject( value ){
	var name;
	for ( name in value ) {
		return false;
	}
	return true;
}

isEmptyObject({}); //true
isEmptyObject({ 'id': 1 }); //false

isEmptyObject([]); //true
isEmptyObject(123); //true
isEmptyObject('123'); //false
isEmptyObject(function(){console.log('123')}); //true

var animal = { name: 'animal' };
var cat = Object.create(animal);
isEmptyObject(animal); //false
isEmptyObject(cat); //false;

isEmptyObject(undefined); //true
isEmptyObject(null); //true


如果要迭代的对象变量是null 或undefined的话，for-in语句会抛出错误，ECMAScript5更正了这一行为，对这种情况不在抛出错误，而是不执行循环体。
为了保证最大限度的兼容性，建议在使用for-in循环之前，先检测确认该对象的值不是null或undefined.
~~~


### 判断数字
~~~
function isNumber( value ){
	return typeof value === 'number' || Object.prototype.toString.call(value) === '[object Number]';
}

isNumber(12);  //true
isNumber(12.3);//true
isNumber('12');//false

//es6
function isNaN( value ){ 
	return Number.isNaN(value);  
}

//es5
function isNaN( value ){ 
	return value !== value;  
}

isNaN(42);	//fasle
isNaN(NaN); //true


//es6
function isFinite(value) {
   Nuber.isFinite(value);
};

//es5
function isFinite(value) {
    return (typeof value === 'number' && !isNaN(value) && value !== Infinity && value !== -Infinity);
};

isFinite(Infinity); //false;
isFinite(-Infinity); //false;
isFinite(NaN); //false;
isFinite(123); //true;

//es6
function isSafeInteger (value) {
    return Number.isSafeInteger(value);
}

//es5
function isSafeInteger (value) {
    return (
           typeof value === 'number'
        && Math.round(value) === value
        && -(Math.pow(2, 53) - 1) <= value
        && value <= (Math.pow(2, 53) - 1)
    );
}

isSafeInteger(42); //true
isSafeInteger(9007199254740992);//false
~~~

### 判断日期
~~~
function isDate( value ){
	return Object.prototype.toString.call(value) === '[object Date]'
}

isDate(new Date()); //true
~~~

### 判断字符串
~~~
function isString( value ){
	return typeof value === 'string';
}

function isString( value ){
	return Object.prototype.toString.call(value) === '[object String]'
}

isString('12'); //true
isString(12); //false
~~~

### 判断正则
~~~
function isRegExp( value ){
	return Object.prototype.toString.call(value) === '[object RegExp]'
}

isRegExp(/abc/); //true
isRegExp('/abc/'); false
~~~


### typeof
~~~
typeof(a)              // undefined
typeof(true)           // boolean
typeof("1")            // string
typeof(1)              // number
typeof(new Function()) // function
typeof(undefined)      // undefined
typeof(null)           // object
typeof(new Object())   // object
typeof(new RegExp())   // object
typeof(new Date())     // object
typeof(new Array())    // object
typeof([])             // object
~~~

### Object.prototype.toString.call(value)
~~~
Object.prototype.toString.call(a)             // Uncaught ReferenceError: a is not defined
Object.prototype.toString.call(true) 					// '[object Boolean]'
Object.prototype.toString.call('1') 					// '[object String]'
Object.prototype.toString.call(1) 						// '[object Number]'
Object.prototype.toString.call(new Function) 	// '[object Function]'
Object.prototype.toString.call(undefined) 		// '[object Undefined]'
Object.prototype.toString.call(null) 					// '[object Null]'
Object.prototype.toString.call(new Object()) 	// '[object Object]'
Object.prototype.toString.call(new RegExp())  // '[object RegExp]'
Object.prototype.toString.call(new Date())    // '[object Date]'
Object.prototype.toString.call(new Array())   // '[object Array]'
Object.prototype.toString.call([])            // '[object Array]'
~~~
