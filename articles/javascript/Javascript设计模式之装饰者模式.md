装饰者模式可以动态地给某个对象添加一些额外的职责，而不会影响从这个类中派生的其他对象。

```
Function.prototype.before = function(beforeFn){
	var self = this;
	return function(){
		beforeFn.apply(this,arguments);
		return self.apply(this,arguments);
	}
}

Function.prototype.after = function(afterFn){
	var self = this;
	return function(){
		var result = self.apply(this,arguments);
		afterFn.apply(this,arguments);
		return result;
	}
}
```

## 数据统计

```
var login = function(){
	console.log('login')
}

var log = function(){
	console.log('user login')
}

login = login.after(log);

login();
```

## 改变参数

```
var login = function(type,url,param){
	console.log(param)
}

var getToken = function(){
	return 'token'
}

login = login.before(function(type,url,param){
	param.token = getToken();
})

login('get','http://baidu.com',{ name: 'hello' });
```

## 表单验证

```
var submit = function(){
	console.log('submit form')
}

var validate = function(){
	console.log('validate form')
}

submit = submit.before(validate);

submit();
```

