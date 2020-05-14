编写一个javscript函数 fn，该函数有一个参数 n（数字类型），其返回值是一个数组，该数组内是 n 个随机且不重复的整数，且整数取值范围是 [2, 32]。

JS实现1：
```
function fn(n){
	if(typeof n === 'undefined' || typeof n != 'number'){
		return [];
	}

	var min = 2, max = 32;
	var result = [];

	while(result.length != n){
		var number = parseInt(Math.random() * (max - min + 1) + min,10);
		if(result.indexOf(number) === -1){
			result.push(number);
		}
	}

	return result;
}
```

JS实现2：
```
//fn函数
function fn(n) {
  var arr = [];
  for (var i = 0; i < n; i++) {
    var rnd = getRand(2, 32);
    if (arr.includes(rnd)) {
      i--;//减一是因为如果第i次循环的时候如果数组有了改值，就重新走一遍
    } else {
      arr.push(rnd);
    }
  }
  return arr;
}
//生成区间随机数
function getRand(m, n) {
  var random = Math.floor(Math.random() * (n - m + 1) + m);
  return random;
}
//检查是否重复,这里直接用了 arr.includes(e)
function checkInArr(e,arr){
  if(arr.indexOf(e)==-1){
    return false;
  }
    return true;
}
//console.log(fn(5));
```

伪代码：
```
/**
 * 获取指定个数的随机整数，整数范围[2,32]
 * @param  {number}   n 需要的整数个数
 * @return {array}  返回包含n个整数的数组，如果n非法，则返回空数组
 */
function fn(n){
    //将整数取值范围作为变量提取出来
    var min = 2, max = 32;

    //参数校验
    if(!isThere(n)) return [];
    if(!typeOK(n) && !isOKStr(n)) return [];
    n = formatInitNum(n);
    if(!rangeOK(n, min, max)) return [];

    //准备一个容器保存结果
    var arr = [];
    //循环
    for(var i=0; i<n; i++){
        //创建一个随机数
        var rnd = getRand(min, max);
　　　　 //检查是否重复
        if( checkInArr(arr, rnd) ){
            i--;
        }else{
            arr.push(rnd);
        }
    }
    return arr;
}
```

# More

为什么你的前端工作经验不值钱?
https://sq.163yun.com/blog/article/198892655404646400