## 实现1：
~~~
var Beverage = function(){};
Beverage.prototype.boilWater = function(){
	console.log('boil water');
}
Beverage.prototype.brew = function(){
	console.log('brew Beverage');
}
Beverage.prototype.pourInCup = function(){
	console.log('pour in cup');
}
Beverage.prototype.addCondiments = function(){
	console.log('add condiments');
}
Beverage.prototype.init = function(){
	this.boilWater();
	this.brew();
	this.pourInCup();
	this.addCondiments();
}

// 泡咖啡
var Coffee = function(){};
Coffee.prototype = new Beverage();
Coffee.prototype.boilWater = function(){
	console.log('boil water');
}
Coffee.prototype.brew = function(){
	console.log('brew coffee');
}
Coffee.prototype.pourInCup = function(){
	console.log('pour in cup');
}
Coffee.prototype.addCondiments = function(){
	console.log('add sugar');
}

// 泡茶
var Tea = function(){};
Tea.prototype = new Beverage();
Tea.prototype.boilWater = function(){
	console.log('boil water');
}
Tea.prototype.brew = function(){
	console.log('brew Tea');
}
Tea.prototype.pourInCup = function(){
	console.log('pour in cup');
}
Tea.prototype.addCondiments = function(){
	console.log('add lemon');
}

var coffee = new Coffee();
coffee.init();
var tea = new Tea();
tea.init();
~~~

## 实现2：
~~~
var Beverage = function(param){
	var boilWater = param.boilWater || function(){};
	var brew = param.brew || function(){};
	var pourInCup = param.pourInCup || function(){};
	var addCondiments = param.addCondiments || function(){};

	var F = function(){};
	F.prototype.init = function(){
		boilWater();
		brew();
		pourInCup();
		addCondiments();
	}
	return F;
}

var Coffee = Beverage({
	boilWater: function(){
		console.log('boil water');
	},
	brew: function(){
		console.log('brew Coffee');
	},
	pourInCup: function(){
		console.log('pour in cup');
	},
	addCondiments: function(){
		console.log('add sugar');
	}
})

var Tea = Beverage({
	boilWater: function(){
		console.log('boil water');
	},
	brew: function(){
		console.log('brew Tea');
	},
	pourInCup: function(){
		console.log('pour in cup');
	},
	addCondiments: function(){
		console.log('add lemon');
	}
})

var coffee = new Coffee();
coffee.init();
var tea = new Tea();
tea.init();
~~~