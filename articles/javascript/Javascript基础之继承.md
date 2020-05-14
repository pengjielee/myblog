## 父类

```
function Animal(name){
	this.name = name || '001';
	this.colors = ['white','black'];
	this.sleep = function(){
		console.log(this.name + ' is sleeping.');
	}
}
Animal.prototype.eat = function(food) {
	food = food || 'fish';
	console.log(this.name + ' is eating ' + food +'.');
};
```

## 一、原型链继承

核心：将父类的实例作为子类的原型。

构造函数、原型和实例的关系：   
- 每个构造函数都有一个原型对象，  
- 原型对象都包含一个指向构造函数的指针，  
- 而实例都包含一个指向原型对象的内部指针。  

```
function Cat(name){
	this.name = name;
}
Cat.prototype = new Animal();
Cat.prototype.constructor = Cat;
Cat.prototype.drink = function(){
	console.log(this.name + ' is drinking coffee.')
}
var xiaobai = new Cat('xiaobai')
xiaobai.drink(); //xiaobai is drinking coffee.
xiaobai.eat(); //xiaobai is eating fish.
xiaobai.sleep(); //xiaobai is sleeping.
xiaobai.colors.push('red');
console.log(xiaobai.colors) //["white", "black", "red"]

var xiaohei = new Cat('xiaohei')
console.log(xiaohei.colors) //["white", "black", "red"]

//xiaobai -> Cat.prototype -> Animal.prototype

//确定原型和实例的关系
Object.prototype.isPrototypeOf(xiaobai) //true
Animal.prototype.isPrototypeOf(xiaobai) //true
Cat.prototype.isPrototypeOf(xiaobai) //true

//or

console.log(xiaobai instanceof Object) //true
console.log(xiaobai instanceof Animal) //true
console.log(xiaobai instanceof Cat) //true
```

问题：  
1、包含引用类型值的原型属性会被所有实例共享。   
在通过原型来实现继承时，原型实际上会变成另一个类型的实例。于是，原先的实例属性也就顺理成章地变成了现在的原型属性了。   
2、在创建子类型的实例时，不能向超类型的构造函数中传递参数。   

## 二、直接继承prototype:

```
function Cat(name){
	this.name = name;
}
Cat.prototype = Animal.prototype;
Cat.prototype.constructor = Cat;
Cat.prototype.drink = function(){
	console.log(this.name + ' is drinking coffee.')
}

var xiaobai = new Cat('xiaobai')

console.log(Cat.prototype.constructor === Cat) //true
console.log(Animal.prototype.constructor === Cat) //true
```

优点：效率比较高（不用执行和建立Animal的实例了），比较省内存。   
问题：  Cat.prototype和Animal.prototype现在指向了同一个对象，那么任何对Cat.prototype的修改，都会反映到Animal.prototype。

利用空对象作为中介:
```
var F = function(){};
F.prototype = Animal.prototype;
Cat.prototype = new F();
Cat.prototype.constructor = Cat;

// 封装函数：
function extend(Child, Parent) {
	var F = function(){};
	F.prototype = Parent.prototype;
	Child.prototype = new F();
	Child.prototype.constructor = Child;
	Child.uber = Parent.prototype; //为子对象设一个uber属性，这个属性直接指向父对象的prototype属性
}
```

## 三、构造函数继承

核心：在子类型构造函数的内部调用超类型构造函数。使用父类的构造函数来增强子类实例，等于是复制父类的实例属性给子类（没用到原型）

```
function Cat(name){
	Animal.call(this,name)
}

var xiaobai = new Cat('xiaobai')
xiaobai.colors.push('red');
console.log(xiaobai.colors) //["white", "black", "red"]

var xiaohei = new Cat('xiaohei')
console.log(xiaohei.colors) //["white", "black"]
xiaohei.sleep(); //xiaohei is sleeping.
xiaohei.eat(); // error

console.log(xiaobai instanceof Animal) //false
console.log(xiaobai instanceof Cat) //true
```

优点：
可以在子类型构造函数中向超类型构造函数传递参数。

问题：  
1、实例并不是父类的实例，只是子类的实例。   
2、只能继承父类的实例属性和方法，不能继承原型属性/方法。   
3、无法实现函数复用，每个子类都有父类实例函数的副本，影响性能。  

## 四、组合继承

介绍：将原型链和借用构造函数的技术组合到一块，从而发挥二者之长的一种继承模式。

核心：使用原型链实现对原型属性和方法的继承，而通过借用构造函数来实现对实例属性的继承。

```
function Cat(name){
	Animal.call(this,name) //继承属性 //第二次调用Animal()
}
Cat.prototype = new Animal();
Cat.prototype.constructor = Cat;
Cat.prototype.drink = function(){
	console.log(this.name + ' is drinking coffee.')
}
var xiaobai = new Cat('xiaobai') //第一次调用Animal()
xiaobai.eat();
xiaobai.drink();
xiaobai.sleep();
xiaobai.colors.push('red');
console.log(xiaobai.colors)

var xiaohei = new Cat('xiaohei')
console.log(xiaohei.colors)
```

优点：
组合继承避免了原型链和借用构造函数的缺陷，融合了它们的优点，成为 JavaScript 中最常用的继
承模式。而且， instanceof 和 isPrototypeOf()也能够用于识别基于组合继承创建的对象。

问题：  
组合继承最大的问题就是无论什么情况下，都会调用两次超类型构造函数：   
一次是在创建子类型原型的时候，  
另一次是在子类型构造函数内部。  

## 五、寄生组合继承

介绍：通过借用构造函数来继承属性，通过原型链的混成形式来继承方法。

核心：通过寄生方式，砍掉父类的实例属性，这样，在调用两次父类的构造的时候，就不会初始化两次实例方法/属性，避免的组合继承的缺点。

```
function Cat(name){
	Animal.call(this,name)
}
(function(){
	var Super = function(){};
	Super.prototype = Animal.prototype;
	Cat.prototype = new Super();
	Cat.prototype.constructor = Cat;
})();

var xiaobai = new Cat('xiaobai') //第一次调用Animal()
xiaobai.eat();
xiaobai.drink();
xiaobai.sleep();
console.log(xiaobai instanceof Animal)
console.log(xiaobai instanceof Cat)
```

优点：
寄生组合式继承是引用类型最理想的继承范式。


## 六、原型式继承

核心：借助原型可以基于已有的对象创建新对象，同时还不必因此创建自定义类型。  
本质上讲，object()对传入其中的对象执行了一次浅复制

```
function object(o){
	function F(){}
	F.prototype = o;
	return new F();
}

var cat = {
	name: "cat",
	colors: ['white','balck'],
	sleep: function(){
		console.log(this.name + ' is sleeping.')
	}
}

var xiaohei = object(cat);
xiaohei.name = 'xiaohei';
console.log(xiaohei.name); //xiaohei
console.log(xiaohei.colors); //["white", "balck"]
xiaohei.sleep(); //xiaohei is sleeping.

var xiaobai = object(cat)
xiaobai.name = 'xiaobai';
xiaobai.colors.push('red'); 
console.log(xiaobai.name); //xiaobai
console.log(xiaobai.colors); //["white", "balck", "red"]
console.log(xiaohei.colors); //["white", "balck", "red"]
```

问题：  
1、必须有一个对象可以作为另一个对象的基础。     
2、引用类型被所有实例共享。

ECMAScript5通过新增Object.create()方法规范化了原型式继承。

这个方法接收两个参数：   
一个用作新对象原型的对象和（可选的）一个为新对象定义额外属性的对象。  
在传入一个参数的情况下，Object.create()与 object()方法的行为相同。    
第二个参数与Object.defineProperties()方法的第二个参数格式相同：   
每个属性都是通过自己的描述符定义的。以这种方式指定的任何属性都会覆盖原型对象上的同名属性。

支持 Object.create()方法的浏览器有 IE9+、 Firefox 4+、 Safari 5+、 Opera 12+和 Chrome

```
var cat = {
	name: "cat",
	colors: ['white','balck'],
	sleep: function(){
		console.log(this.name + ' is sleeping.')
	}
}

var xiaohei = Object.create(cat);
xiaohei.name = 'xiaohei';
console.log(xiaohei.name); //xiaohei
console.log(xiaohei.colors); //["white", "balck"]
xiaohei.sleep(); //xiaohei is sleeping.

var xiaobai = Object.create(cat,{ 
	name: { value: 'xiaobai' },
	colors:{ value: [ 'blue','green']}
});
xiaobai.colors.push('red'); 
console.log(xiaobai.name); //xiaobai
console.log(xiaobai.colors); //["blue", "green", "red"]
console.log(xiaohei.colors); //["white", "balck"]
```

## 七、寄生式继承

介绍：寄生式继承的思路与寄生构造函数和工厂模式类似，即创建一个仅用于封装继承过程的函数，该函数在内部以某种方式来增强对象，最后再返回对象。

```
function object(o){
	function F(){}
	F.prototype = o;
	return new F();
}
function create(origin){
	var clone = object(origin);
	clone.sayHello = function(){
		console.log('hello world')
	}
	return clone;
}

var cat = {
	name: "cat",
	colors: ['white','balck'],
	sleep: function(){
		console.log(this.name + ' is sleeping.')
	}
}

var xiaohua = create(cat)
xiaohua.sayHello();
xiaohua.sleep();
```

问题：  
使用寄生式继承来为对象添加函数，会由于不能做到函数复用而降低效率；这一点与构造函数模式类似。

## 八、实例继承

核心：为父类实例添加新特性，作为子类实例返回

```
function Cat(name){
  var instance = new Animal();
  instance.name = name || 'Tom';
  return instance;
}

var xiaobai = new Cat('xiaobai')
xiaobai.eat();  //xiaobai is eating fish.
xiaobai.sleep(); //xiaobai is sleeping.
xiaobai.colors.push('red');
console.log(xiaobai.colors); //["white", "black", "red"]
console.log(xiaobai instanceof Animal) //true
console.log(xiaobai instanceof Cat)  //false

var xiaohei = new Cat('xiaohei')
console.log(xiaohei.colors) //["white", "black"]
```

问题：实例是父类的实例，不是子类的实例

## 九、拷贝继承

```
function Cat(name){
  var animal = new Animal();
  for(var p in animal){
    Cat.prototype[p] = animal[p];
  }
  Cat.prototype.name = name || 'Tom';
}


function extend(Child, Parent) {
	var parent = Parent.prototype;
	var child = Child.prototype;
	for (var i in parent) {
		child[i] = parent[i];
	}
	child.uber = parent;
}

//浅拷贝
function copy(parent) {
	var child = {};
	for (var i in parent) { 
		child[i] = parent[i];
	}
	child.uber = parent;
	return child;
}

//深拷贝
function deepCopy(parent,child) {
	var child = child || {};
	for (var i in parent) { 
		if(typeof parent[i] === 'object'){
			child[i] = (parent[i].constructor === Array) ? [] : {};
			deepCopy(parent[i],child[i])
		}else{
			child[i] = parent[i];
		}
	}
	return child;
}
```

问题：  
1、效率较低，内存占用高（因为要拷贝父类的属性）  
2、无法获取父类不可枚举的方法（不可枚举方法，不能使用for in 访问到）  

