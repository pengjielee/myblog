### 1. 是否有NaN，有的话，则一律返回false
~~~
console.log(1 == NaN) //false
~~~

### 2. null和undefined的比较都返回true
~~~
console.log(undefined == null) //true
~~~

### 3. 是否有boolean值，有的话则将true转化为1，false转化为0
~~~
console.log(true == 1) //true
console.log(false == 0) //true
~~~

### 4. 有一边是字符串
a. 同样是字符串，则直接进行字符串值的比较
~~~
console.log('12' == '12') //true
~~~

b. 是数字，则需要将字符串转化为数字，然后进行比较
~~~
console.log('12' == 12) //true
~~~

c. 有布尔类型，则要将布尔类型转化为0或则1，然后进行比较
~~~
console.log('1' == true) //true
console.log('0' == false) //true
~~~

d. 对象或者数组类型，则需要调用toString()或者valueOf()方法转化成简单类型，然后进行比较
~~~
var a = {
	valueOf: function(){
		return 1;
  }
}
var b = {
	toString: function(){
		return 0;
  }
}
var c = [[2]];
console.log(a.valueOf());  //1
console.log(a.toString()); //[object Object]
console.log(b.valueOf());  //对象本身
console.log(b.toString()); //0
console.log(c.valueOf());  //对象本身
console.log(c.toString()); //2

console.log(true == a) //true
console.log(true == b) //false

console.log(c == '2');
~~~

注释：
对象转化为简单类型时会优先调用valueOf方法，如果可以与简单值进行比较则会直接比较，此时不再调用toString方法。
如果调用valueOf方法后无法与简单值进行比较，则会再调用toString方法，最终得到比对的结果。

注意:
Date对象不满足上述的规则，Date对象的toString和valueOf方法都是重新定义过的

参考：
[https://blog.csdn.net/qq_37530031/article/details/78317823](https://blog.csdn.net/qq_37530031/article/details/78317823)
[https://www.jb51.net/article/103830.htm](https://www.jb51.net/article/103830.htm)
