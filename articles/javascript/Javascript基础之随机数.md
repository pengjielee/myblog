Math.random() 函数返回一个浮点，伪随机数在范围[0,1)。

## 生成[0,9]的随机数
~~~
parseInt(Math.random() * 10, 10);

[0,1) * 10 = [0,10)
~~~

## 生成[0,10]的随机数
~~~
parseInt(Math.random() * (10 + 1), 10);

[0,1) * 11 = [0,11)
~~~

## 生成[0,max]的随机数：
~~~
parseInt(Math.random() * ( max + 1 ),10);
~~~

## 生成[1,max]的随机数：
~~~
parseInt(Math.random() * max,10) + 1;

[0,1) * max + 1 = [1,max+1)
~~~

## 生成[min,max)的随机数：
~~~
parseInt(Math.random() * (max - min) + min,10);
~~~

## 生成[min,max]的随机数：
~~~
parseInt(Math.random() * (max - min + 1) + min,10);
~~~

## 举例说明
~~~
Math.random() 伪随机数范围在[0, 1)。
假如要生成[5,10]，即 min = 5，max = 10，max-min就是5。
[0,1) * (max - min) + min = [0,1) * 5 + 5 = [5,10)
[0,1) * (max - min + 1) + min = [0,1) * 6 + 5 = [5,11)
~~~

## 基础知识
~~~
//向下取整（floor,地板）
Math.floor(4.1) // 4
Math.floor(4.5) // 4
Math.floor(4.9) // 4

//向上取整（ceil,天花板）
Math.ceil(4.1) //5
Math.ceil(4.5) //5 
Math.ceil(4.9) //5

//向下取整 Math.floor()
parseInt(4.1) //4
parseInt(4.5) //4
parseInt(4.9) //4
~~~

## 面试题

编写一个javascript函数 fn，该函数有一个参数 n（数字类型），其返回值是一个数组，该数组内是 n 个随机且不重复的整数，且整数取值范围是 [2, 32]。

~~~
function generate(n){
	if(typeof n === 'undefined'){
		return new Error('please input a number')
	}
	if(!/\d+/.test(n)) {
		return new Error('please input a number')
	}
	var min = 2, max = 32;
	var result = [];

	while(true){
		if(result.length === n){
			break;
		}
		// 生成2-32的随机数
		var number = parseInt(Math.random()*(max-min+1)+min,10);
		if(result.indexOf(number) === -1){
			result.push(number)
		}
	}
	return result;
}
~~~

# More

MDN Math random  
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random 

在js中生成指定范围的随机数？
https://www.zhihu.com/question/43425107/answer/95521759

为什么你的前端工作经验不值钱？  
https://zhuanlan.zhihu.com/p/25595871