适配器模式用来解决接口之间不兼容的问题。适配器模式不需要改变已有的接口，就能够使接口兼容。

现实中的适配器：
a. 港式插头转换器；
b. 电源适配器；
c. USB转接口；

```
var googleMap = {
	show: function(){
		console.log('render google map')
	}
}

var gaodeMap = {
	show: function(){
		console.log('render gaode map')
	}
}

var baiduMap = {
	display: function(){
		console.log('render baidu map')
	}
}

var baiduMapAdapter = {
	show: function(){
		return baiduMap.display();
	}
}

var renderMap = function(map){
	if(map.show instanceof Function){
		map.show();
	}
}

renderMap(googleMap);
renderMap(gaodeMap);
renderMap(baiduMapAdapter);
```




