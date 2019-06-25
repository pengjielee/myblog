### 简单工厂
~~~
var XMLHttpFactory = function() {};

XMLHttpFactory.createXMLHttp = function() {
	var XMLHttp = null;
	if (window.XMLHttpRequest) {
		XMLHttp = new XMLHttpRequest();
	} else if (window.ActiveXObject) {
		XMLHttp = new ActiveXObject("Microsoft.XMLHTTP");
	}
	return XMLHTTP;
}
~~~

### 抽象工厂
~~~
var XMLHttpFactory = function() {};

XMLHttpFactory.prototype = {
	createFactory: function() {　　
		throw new Error('This is an abstract class');　
	}
}
//派生子类
var XHRHandler = function() {　　
	XMLHttpFactory.call(this);
};
XHRHandler.prototype = new XMLHttpFactory();
XHRHandler.prototype.constructor = XHRHandler;
//重新定义createFactory 方法
XHRHandler.prototype.createFactory = function() {
	var XMLHttp = null;
	if (window.XMLHttpRequest) {
		XMLHttp = new XMLHttpRequest()
	}
	elseif(window.ActiveXObject) {
		XMLHttp = new ActiveXObject("Microsoft.XMLHTTP")
	}
	return XMLHttp;
}
~~~
