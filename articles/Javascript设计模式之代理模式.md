代理模式是为一个对象提供一个代用品或占位符，以便控制对它的访问。


## 虚拟代理实现图片预加载
~~~
var myImage = (function(){
	var imgNode = document.createElement('img');
	document.body.appendChild(imgNode);

	return {
		setSrc: function(src){
			imgNode.src = src;
		}
	}
})();

var proxyImage = (function(src){
	var img = new Image();
	img.onload = function(){
		myImage.setSrc(this.src);
	}

	return {
		setSrc: function(src){
			myImage.setSrc('//loading.gif');
			img.src = src;
		}
	}
})();

proxyImage.setSrc('//real.jpg');
~~~

## 缓存代理计算乘积
~~~

var mult = function(){
	var a = 1;
	for(var i = 0; i < arguments.length; i++){
		a = a * arguments[i];
	}
	return a;
}

var proxyMult = function(){
	var cache = {};
	return function(){
		var args = Array.prototype.join.call(arguments,'',);
		if(args in cache){
			return cache[args];
		}
		return cache[args] = mult.apply(this,arguments)
	}
}

proxyMult(1,2,3,4);
~~~