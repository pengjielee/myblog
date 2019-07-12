职责链模式：使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系，将这些对象连成一条链，并沿着这条链传递该请求，直到有一个对象处理它为止。

~~~
Function.prototype.after = function(fn){
	var self = this;
	return function(){
		var result = self.apply(this,arguments);
		if(result === 'nextSuccessor'){
			return fn.apply(this,arguments);
		}
		return result;
	}
}

var order500 = function(orderType,pay,stock){
	if(orderType === 1 && pay === true){
		console.log('500 order,get 100 coupon');
	}else{
		return 'nextSuccessor'
	}
}

var order200 = function(orderType,pay,stock){
	if(orderType === 2 && pay === true){
		console.log('200 order,get 50 coupon');
	}else{
		return 'nextSuccessor'
	}
}

var orderNormal = function(orderType,pay,stock){
	if(stock){
		console.log('noraml order');
	}else{
		console.log('sold out');
	}
}

var order = order500.after(order200).after(orderNormal);

order(1,true,500);
order(2,true,500);
order(1,false,500);
~~~