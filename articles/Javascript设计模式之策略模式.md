策略模式：定义一系列的算法，把它们一个个封装起来，并且使它们可以相互替换。

~~~
var strategies = {
	'A': function(salay){
		return salay * 6;
	},
	'B': function(salay){
		return salay * 4;
	},
	'C': function(salay){
		return salay * 3;
	},
	'D': function(salay){
		return salay * 2;
	}
}

var calculateBouns = function(level,salary){
	return strategies[level](salary);
}

console.log(calculateBouns('A',20000))
console.log(calculateBouns('B',20000))
~~~