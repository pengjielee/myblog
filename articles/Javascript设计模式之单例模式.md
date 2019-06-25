需求：点击某个按钮的时候需要在页面弹出一个遮罩层。

### 实现1：
~~~

var createMask = function(){
	return document.body.appendChild(document.createElement('div'));
};

$('button').click( function(){
   var mask = createMask();
   mask.show();
});

问题：这个遮罩层是全局唯一的, 那么每次调用createMask都会创建一个
新的div, 虽然可以在隐藏遮罩层的把它remove掉. 但显然这样做不合理.
~~~


### 实现2：在页面的一开始就创建好这个div. 然后用一个变量引用它.
~~~

var mask=document.body.appendChild(document.createElement('div'));

$('button').click( function(){
   mask.show();
});

问题：这样确实在页面只会创建一个遮罩层div, 但是另外一个问题随之而来, 
也许我们永远都不需要这个遮罩层, 那又浪费掉一个div, 对dom节点的任何
操作都应该非常吝啬.

~~~

### 实现3：借助一个变量. 来判断是否已经创建过div

~~~

var mask;
 
var createMask = function(){
	if(!mask){
		mask=document.body.appendChild(document.createElement('div'));
	}
	return mask;
}

$('button').click( function(){
   createMask();
   mask.show();
});

问题：首先这个函数是存在一定副作用的, 函数体内改变了外界变量mask的
引用, 在多人协作的项目中, createMask是个不安全的函数. 另一方面, mask
这个全局变量并不是非需不可. 

~~~

### 实现4：闭包实现

~~~

var createMask = function(){
  var mask;
  return function(){
       return mask || (mask = document.body.appendChild( document.createElement('div')));
  }
}

用了个简单的闭包把变量mask包起来, 至少对于createMask函数来讲, 它是封闭的.
~~~


### 实现5：最终版

~~~

var singleton=function(fn){
	var result;
	return function(){
		return result||(result=fn.apply(this,arguments));
	}
};

var createMask=singleton(function(){
	return document.body.appendChild(document.createElement('div'));
});

用一个变量来保存第一次的返回值, 如果它已经被赋值过, 那么在以后的调用
中优先返回该变量. 而真正创建遮罩层的代码是通过回调函数的方式传人到
singleton包装器中的. 这种方式其实叫桥接模式. 

问题：然而singleton函数也不是完美的, 它始终还是需要一个变量result来
寄存div的引用. 遗憾的是js的函数式特性还不足以完全的消除声明和语句.

~~~




