### 1、创建数组

~~~
[code lang = 'js']
var colors = new Array();
console.log(colors); 		//[]
console.log(colors.length); //0

var colors = new Array(20);
console.log(colors); 		//[]
console.log(colors.length); //20

var colors = new Array("red","yellow","green");
console.log(colors); 		//["red", "yellow", "green"]
console.log(colors.length); //3

var colors = Array("red");
console.log(colors); 		//["red"]
console.log(colors.length); //1

var colors = [];
console.log(colors);		//[]
console.log(colors.length);	//0

var colors = ["red","yellow","green"]
console.log(colors); 		//["red", "yellow", "green"]
console.log(colors.length); //3
[/code]
~~~

### 2、数组长度

~~~
[code lang = 'js']
var colors = ["red","yellow","green"];
console.log(colors[0]); //red
console.log(colors[1]);	//yellow
colors[1] = "black";	
console.log(colors[1]);	//black

console.log(colors[2]);	//green
colors.length = 2;		
console.log(colors[2]);	//undefined
[/code]
~~~

### 3、数组极限

~~~
[code lang = 'js']
var max = 4294967295;
var names = new Array(max);
console.log(names.length);	//4 294 967 295

var names = new Array(max+1);
console.log(names.length);	//Uncaught RangeError: Invalid array length(anonymous function)
[/code]
~~~

### 4、检测数组  
(1) instanceof操作符  
a. 对于一个网页，或者一个全局作用域而言，使用instanceof操作符就能得到满意的结果。
b. instanceof操作符的问题在于，它假定只有一个全局执行环境。如果网页中包含多个框架，那实际上就存在两个以上不同的全局执行环境，从而存在两个以上不同版本的Array构造函数。

(2) ECMAScript 5 新增了Array.isArray()方法
c. 为了解决这个问题，ECMAScript 5新增了Array.isArray()方法。这个方法的目的是最终确定某个值到底是不是数组，而不管它是在哪个全局执行环境中创建的。
d. 支持Array.isArray()方法的浏览器有IE9+、Firefox 4+、Safari 5+、Opera 10.5+和Chrome。

~~~
[code lang = 'js']
var names = ["jim","tom"];
//对于一个网页，或者一个全局作用域而言，使用instanceof操作符
console.log(names instanceof Array);	//true

//ECMAScript5新增Array.isArray(),支持该方法的浏览器有IE9+、Firefox 4+、Safari 5+、Opera 10.5+和Chrome。
console.log(Array.isArray(names));		//true

function isArray(value){ 
   return Object.prototype.toString.call(value) == "[object Array]"; 
}
console.log(isArray(names));			//true
[/code]
~~~


### 5、转换方法
(1) toLocaleString()、toString()和valueOf()方法
a. 所有对象都具有toLocaleString()、toString()和valueOf()方法。
b. 调用数组的toString()方法会返回由数组中每个值的字符串形式拼接而成的一个以逗号分隔的字符串。
c. 调用valueOf()返回的还是数组。实际上，为了创建这个字符串会调用数组每一项的toString()方法。
d. toLocaleString()方法经常也会返回与toString()和valueOf()方法相同的值，但也不总是如此。当调用数组的toLocaleString()方法时，它也会创建一个数组值的以逗号分隔的字符串。而与前两个方法唯一的不同之处在于，这一次为了取得每一项的值，调用的是每一项的toLocaleString()方法，而不是toString()方法。
e. 数组继承的toLocaleString()、toString()和valueOf()方法，在默认情况下都会以逗号分隔的字符串的形式返回数组项。
(2) join()方法
a. 使用join()方法，则可以使用不同的分隔符来构建这个字符串。
b. join()方法只接收一个参数，即用作分隔符的字符串，然后返回包含所有数组项的字符串。
c. 如果不给join()方法传入任何值，或者给它传入undefined，则使用逗号作为分隔符。IE7及更早版本会错误的使用字符串"undefined"作为分隔符。

~~~
[code lang = 'js']
var names = ["1","2","3"];
console.log(names.toString());		//1,2,3
console.log(names.valueOf());		//["1","2","3"]
console.log(names.toLocaleString());	//1,2,3

var person1 = {
    toLocaleString: function() {
        return "jim"
    },
    toString: function() {
        return "jim"
    }
};
var person2 = {
    toLocaleString: function() {
        return "tomson"
    },
    toString: function() {
        return "tom"
    }
};
var people = [person1, person2];
console.log(people);
console.log(people.toString());
console.log(people.toLocaleString());
console.log(colors.join(","));
console.log(colors.join("||"));
console.log(colors.join(undefined));
[/code]
~~~

### 6、栈方法
栈是一种LIFO（Last-In-First-Out，后进先出）的数据结构，也就是最新添加的项最早被移除。而栈中项的插入（叫做推入）和移除（叫做弹出），只发生在一个位置——栈的顶部。
(1) push()方法
push()方法可以接收任意数量的参数，把它们逐个添加到数组末尾，并返回修改后数组的长度。
(2) pop()方法
pop()方法则从数组末尾移除最后一项，减少数组的length值，然后返回移除的项。

~~~
[code lang = 'js']
var numbers = [1,2,3];
console.log(numbers);		//[1,2,3]
numbers.push(4);
numbers.push(5);
console.log(numbers);		//[1,2,3,4,5]

var number = numbers.pop();
console.log(numbers);		//[1,2,3,4]
console.log(number);		//5

number = numbers.pop();
console.log(numbers);		//[1,2,3]
console.log(number);		//4
[/code]
~~~

### 7、队列方法
队列数据结构的访问规则是FIFO（First-In-First-Out，先进先出）。队列在列表的末端添加项，从列表的前端移除项。
(1) push()方法
由于push()是向数组末端添加项的方法，因此要模拟队列只需一个从数组前端取得项的方法。
(2) shift()方法
它能够移除数组中的第一个项并返回该项，同时将数组长度减1。
(3) unshift()方法
unshift()与shift()的用途相反：它能在数组前端添加任意个项并返回新数组的长度。
(4) 结合使用
结合使用shift()和push()方法，可以像使用队列一样使用数组。
结合使用unshift()和pop()方法，可以从相反的方向来模拟队列，即在数组的前端添加项，从数组末端移除项。

IE7及更早版本对JavaScript的实现中存在一个偏差，其unshift()方法总是返回undefined而不是数组的新长度。IE8在非兼容模式下会返回正确的长度值。

~~~
[code lang = 'js']
//正向实现队列
var numbers = [1,2,3];
console.log(numbers);		//[1,2,3]
numbers.push(4);
numbers.push(5);
console.log(numbers);		//[1,2,3,4,5]

var number = numbers.shift();
console.log(numbers);		//[2,3,4,5]
console.log(number);		//1

number = numbers.shift();
console.log(numbers);		//[3,4,5]
console.log(number);		//2

//反向实现队列
var numbers = [3,4,5];
console.log(numbers);		//[3,4,5]
numbers.unshift(2);
numbers.unshift(1);
console.log(numbers);		//[1,2,3,4,5]

var number = numbers.pop();
console.log(numbers);		//[1,2,3,4]
console.log(number);		//5

number = numbers.pop();
console.log(numbers);		//[1,2,3]
console.log(number);		//4
[/code]
~~~

### 8、重排序方法
(1) reverse()方法
reverse()方法会反转数组项的顺序。
(2) sort()方法
a. 在默认情况下，sort()方法按升序排列数组项——即最小的值位于最前面，最大的值排在最后面。
b. 为了实现排序，sort()方法会调用每个数组项的toString()转型方法，然后比较得到的字符串，以确定如何排序。即使数组中的每一项都是数值，sort()方法比较的也是字符串。
c. 这种排序方式在很多情况下都不是最佳方案。因此sort()方法可以接收一个比较函数作为参数，以便我们指定哪个值位于哪个值的前面。
d. 比较函数接收两个参数，如果第一个参数应该位于第二个之前则返回一个负数，如果两个参数相等则返回0，如果第一个参数应该位于第二个之后则返回一个正数。
(3) valueOf()方法
对于数值类型或者其valueOf()方法会返回数值类型的对象类型，可以使用一个更简单的比较函数。这个函数只要用第二个值减第一个值即可。

~~~
[code lang = 'js']
var numbers = [1,2,3,10];
console.log(numbers);		//[1,2,3,10]

numbers.reverse();
console.log(numbers);		//[10,3,2,1]

numbers.sort();
console.log(numbers);		//[1,10,2,3]

var compare = function(value1,value2){
	if(value1<value2){
		return -1;
	}else if(value1>value2){
		return 1;
	}else{
		0
	}
}
numbers.sort(compare);
console.log(numbers);		//[1,2,3,10]

function asc(value1, value2) {
    if (value1 < value2) {
        return - 1
    } else {
        if (value1 > value2) {
            return 1
        } else {
            return 0
        }
    }
}
function desc(value1, value2) {
    if (value1 < value2) {
        return 1
    } else {
        if (value1 > value2) {
            return - 1
        } else {
            return 0
        }
    }
}
function compare(value1, value2) {
    return value1 - value2
}
numbers.sort(asc);
console.log(numbers);

numbers.sort(desc);
console.log(numbers);

numbers = [4, 9, 2, 1, 0];
numbers.sort(compare);
[/code]
~~~

### 9、操作方法
(1) concat()方法:
a. concat()方法可以基于当前数组中的所有项创建一个新数组。具体来说，这个方法会先创建当前数组一个副本，然后将接收到的参数
添加到这个副本的末尾，最后返回新构建的数组。
b. 在没有给concat()方法传递参数的情况下，它只是复制当前数组并返回副本。
c. 如果传递给concat()方法的是一或多个数组，则该方法会将这些数组中的每一项都添加到结果数组中。
d. 如果传递的值不是数组，这些值就会被简单地添加到结果数组的末尾。
(2) slice()方法:
a. 它能够基于当前数组中的一或多个项创建一个新数组。
b. slice()方法可以接受一或两个参数，即要返回项的起始和结束位置。
c. 在只有一个参数的情况下，slice()方法返回从该参数指定位置开始到当前数组末尾的所有项。
d. 如果有两个参数，该方法返回起始和结束位置之间的项——但不包括结束位置的项。
e. slice()方法不会影响原始数组。
f. 如果slice()方法的参数中有一个负数，则用数组长度加上该数来确定相应的位置。如果结束位置小于起始位置，则返回空数组。
(3) splice()方法:
a. splice()的主要用途是向数组的中部插入项，但使用这种方法的方式则有如下3种。
a1. 删除：可以删除任意数量的项，只需指定2个参数：要删除的第一项的位置和要删除的项数。
a2. 插入：可以向指定位置插入任意数量的项，只需提供3个参数：起始位置、0（要删除的项数）和要插入的项。如果要插入多个项，可以再传入第四、第五，以至任意多个项。
a3. 替换：可以向指定位置插入任意数量的项，且同时删除任意数量的项，只需指定3个参数：起始位置、要删除的项数和要插入的任意数量的项。插入的项数不必与删除的项数相等。
b. splice()方法始终都会返回一个数组，该数组中包含从原始数组中删除的项（如果没有删除任何项，则返回一个空数组）。

~~~
[code lang = 'js']
var arr = [1, 2, 3];
var newArr = arr.concat();
console.log(newArr);

newArr = arr.concat([4, 5]);
console.log(newArr);

newArr = arr.concat([6, 7], [8, 9]);
console.log(newArr);

newArr = arr.concat(10, 11, [12, 13]);
console.log(newArr);

newArr = arr.concat(14, 15);
console.log(newArr);

var arr1 = [1, 2, 3];
var newArr1 = arr1.slice(1);
console.log(newArr1);

newArr1 = arr1.slice(1, 3);
console.log(newArr1);

newArr1 = arr1.slice( - 2, -1);
console.log(newArr1);

newArr1 = arr1.slice(1, -1);
console.log(newArr1);

var arr3 = [1, 2, 3, 4, 5, 6];
var newArr3 = arr3.splice(0, 1);
console.log(newArr3);

newArr3 = arr3.splice(1, 0, 7, 8);
console.log(newArr3);

newArr3 = arr3.splice(1, 1, 9, 10);
console.log(newArr3);
[/code]
~~~

### 10、位置方法
ECMAScript 5为数组实例添加了两个位置方法：indexOf()和lastIndexOf()。  
a. 这两个方法都接收两个参数：要查找的项和表示查找起点位置的索引（可选的）。其中，indexOf()方法从数组的开头（位置0）开始向后查找，lastIndexOf()方法则从数组的末尾开始向前查找。  
b. 这两个方法都返回要查找的项在数组中的位置，或者在没找到的情况下返回-1。
c. 在比较第一个参数与数组中的每一项时，会使用全等操作符；也就是说，要求查找的项必须严格相等（就像使用===一样）
d. 使用indexOf()和lastIndexOf()方法查找特定项在数组中的位置非常简单，支持它们的浏览器包括IE9+、Firefox 2+、Safari 3+、Opera 9.5+和Chrome。

~~~
[code lang = 'js']
var numbers = [1,2,3,4,5];
console.log(numbers.indexOf(6));		//-1
console.log(numbers.indexOf(1));		//0
console.log(numbers.indexOf(2));		//1
console.log(numbers.lastIndexOf(6));	//-1
console.log(numbers.lastIndexOf(1));	//0
console.log(numbers.lastIndexOf(2));	//1
[/code]
~~~

### 11、迭代方法
ECMAScript 5为数组定义了5个迭代方法。  
a. 每个方法都接收两个参数：要在每一项上运行的函数和（可选的）运行该函数的作用域对象——影响this的值。  
b. 传入这些方法中的函数会接收三个参数：数组项的值、该项在数组中的位置和数组对象本身。  
c. 根据使用的方法不同，这个函数执行后的返回值可能会也可能不会影响方法的返回值。  
f. 以上方法都不会修改数组中的包含的值。  
g. 在这些方法中，最相似的是every()和some()，它们都用于查询数组中的项是否满足某个条件。对every()来说，传入的函数必须对每一项都返回true，这个方法才返回true；否则，它就返回false。而some()方法则是只要传入的函数对数组中的某一项返回true，就会返回true。  
h. 这些数组方法通过执行不同的操作，可以大大方便处理数组的任务。支持这些迭代方法的浏览器有IE9+、Firefox 2+、Safari 3+、Opera 9.5+和Chrome。  
(1) every()：对数组中的每一项运行给定函数，如果该函数对每一项都返回true，则返回true。  
(2) filter()：对数组中的每一项运行给定函数，返回该函数会返回true的项组成的数组。  
(3) forEach()：对数组中的每一项运行给定函数。这个方法没有返回值。  
(4) map()：对数组中的每一项运行给定函数，返回每次函数调用的结果组成的数组。  
(5) some()：对数组中的每一项运行给定函数，如果该函数对任一项返回true，则返回true。  

~~~
[code lang = 'js']
支持这些迭代方法的浏览器有IE9+、Firefox 2+、Safari 3+、Opera 9.5+和Chrome。

var numbers = [1,2,3,4,5];
var everyResult = numbers.every(function(item,index,array){
	return (item>2);
});
console.log(everyResult);	//false

var someResult = numbers.some(function(item,index,array){
	return (item>2);
});
console.log(someResult);	//true

var filterResult = numbers.filter(function(item,index,array){
	return (item>2);
});
console.log(filterResult);	//[3,4,5]


var mapResult = numbers.map(function(item,index,array){
	return (item+1);
});
console.log(mapResult);	//[2,3,4,5,6]


numbers.forEach(function(item,index,array){
	console.log(item);
});
[/code]
~~~

### 12、缩小(归并)方法

ECMAScript 5还新增了两个归并数组的方法：reduce()和reduceRight()。  
a. 这两个方法都会迭代数组的所有项，然后构建一个最终返回的值。其中，reduce()方法从数组的第一项开始，逐个遍历
到最后。而reduceRight()则从数组的最后一项开始，向前遍历到第一项。  
b. 这两个方法都接收两个参数：一个在每一项上调用的函数和（可选的）作为归并基础的初始值。  
c. 给reduce()和reduceRight()的函数接收4个参数：前一个值、当前值、项的索引和数组对象。这个函数返回的任何值都会作为第一个参数自动传给下一项。  
d. 第一次迭代发生在数组的第二项上，因此第一个参数是数组的第一项，第二个参数就是数组的第二项。  
f. 使用reduce()方法可以执行求数组中所有值之和的操作。  
g. 使用reduce()还是reduceRight()，主要取决于要从哪头开始遍历数组。除此之外，它们完全相同。  
h. 支持这两个归并函数的浏览器有IE9+、Firefox 3+、Safari 4+、Opera 10.5和Chrome。

~~~
[code lang = 'js']
//支持这两个归并函数的浏览器有IE9+、Firefox 3+、Safari 4+、Opera 10.5和Chrome。
//reduce()方法从数组的第一项开始，逐个遍历到最后
//reduceRight()则从数组的最后一项开始，向前遍历到第一项。

var numbers = [1,2,3,10];
console.log(numbers);		//[1,2,3,10]

var sum = numbers.reduce(function(prev,cur,index,array){
	//console.log(prev);	//1,3,6,16
	//console.log(cur);	//2,3,10,16
	console.log(index);	//1,2,3,16
	return prev+cur;
});
console.log(sum);	//16

var sum = numbers.reduceRight(function(prev,cur,index,array){
	//console.log(prev);	//10,13,15,16
	//console.log(cur);	//3,2,1,16
	console.log(index);	//2,1,0,16
	return prev+cur;
});
console.log(sum);	//16
[/code]
~~~


原：javascript高级程序设计（第三版）

