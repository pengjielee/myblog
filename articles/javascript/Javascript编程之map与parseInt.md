## 题目
```
['1','2','3'].map(parseInt) // [1,NaN,NaN]

// parseInt(string, radix) -> map(parseInt(value,index))
// parseInt('1', 0) // 1
// parseInt('2', 1) // NaN
// parseInt('3', 2) // NaN

['1','2','3'].map(function(item,index){
	return parseInt(item,10);
}) // [1,2,3]

```

## array.map(function(currentValue,index,arr), thisValue)

function(currentValue, index, arr) 必须。函数，数组中的每个元素都会执行这个函数。  
thisValue可选。对象作为该执行回调时使用，传递给函数，用作"this"的值。如果省略了thisValue，"this"的值为"undefined"

```
['1','2','3'].map(function(item,index){
	console.log(item) //'1','2','3'
	console.log(this) //{a: 10}
	return item
},{ "a": 10 })
```


## parseInt()函数可解析一个字符串，并返回一个整数。  

parseInt(string, radix)   

string	必需。要被解析的字符串。   
radix	可选。表示要解析的数字的基数。该值介于 2 ~ 36 之间。    
如果省略该参数或其值为0，则数字将以10为基础来解析。  
如果它以 “0x” 或 “0X” 开头，将以16为基数。  
如果该参数小于2或者大于36，则parseInt()将返回NaN。  

# More
[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)  
[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt)  
[http://www.runoob.com/jsref/jsref-map.html](http://www.runoob.com/jsref/jsref-map.html)       
[http://www.w3school.com.cn/jsref/jsref_parseInt.asp](http://www.w3school.com.cn/jsref/jsref_parseInt.asp)   
