编写一个javscript函数 fn，该函数有一个参数 n（数字类型），其返回值是一个数组，该数组内是 n 个随机且不重复的整数，且整数取值范围是 [2, 32]。
~~~
function fn(n){
	if(typeof n === 'undefined'){
		return;
	}

	if(typeof n != 'number'){
		return;
	}

	var min = 2, max = 32;
	var result = [];

	if(n <= 0 || n >= max -1){
		return result;
	}

	while(result.length != n){
		var number = parseInt(Math.random()*(max-min+1)+min,10);
		if(result.indexOf(number) === -1){
			result.push(number);
		}
	}

	return arr;
}
~~~

为什么你的前端工作经验不值钱?
https://sq.163yun.com/blog/article/198892655404646400