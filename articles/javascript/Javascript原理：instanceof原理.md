## instanceof

The instanceof operator tests whether the prototype property of a constructor appears anywhere in the prototype chain of an object.

The instanceof operator tests the presence of constructor.prototype in object's prototype chain.

```
function Car(make) {
  this.make = make;
}
const auto = new Car('Honda');

console.log(auto instanceof Car);    // true
console.log(auto instanceof Object); // true
```

```
function Cat() {}
function Dog() {}

let cat = new Cat();
console.log(cat instanceof Cat);     // true
console.log(cat instanceof Dog);     // false
console.log(cat instanceof Object);  // true

Cat.prototype = {};
let cat1 = new Cat();
console.log(cat1 instanceof Cat); // true
console.log(cat instanceof Cat);  // false
console.log(cat instanceof Dog);  // false

Dog.prototype = new	Cat();
let dog = new Dog();
console.log(dog instanceof Dog); // true
console.log(dog instanceof Cat); // true
```

## instanceof原理

与instanceof 有关的原型链知识：
- 所有 JavaScript 对象都有 __proto__ 属性，只有 Object.prototype.__proto__ === null ；
- 构造函数的 prototype 属性指向它的原型对象，而构造函数实例的 __proto__ 属性也指向该原型对象；

instanceof 主要的实现原理就是只要右边变量的 prototype 在左边变量的原型链上即可。因此，instanceof 在查找的过程中会遍历左边变量的原型链，直到找到右边变量的 prototype，如果查找失败，则会返回 false。

代码：
```
function instanceof(left, right) { 
  let RP = right.prototype; // 取右表达式的 prototype 值
  while (true) {
  	if (left === null) {
        return false;	
    }
    if (left === RP) {
        return true;	
    }  
    left = left.__proto__; 
  }
}
```

实例：
```
function Person() {}
const p1 = new Person();
p1 instanceof Object;

第一次赋值
left = p1, right = Object, RP = Object.prototype
第一次判断
left !== null && left !== RP, 继续向上寻找left的原型链

第二次赋值
left = p1.__proto__ = Person.prototype
第二次判断
left !== null && left !== RP, 继续向上查找

每三次赋值
left = p1.__proto__.__proto__ = Person.prototype.__proto__
第三次判断
left !== null, 此时 left === RP, 返回true, 执行完毕。
 ```

MDN:
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof

instanceof 的原理是什么
https://blog.csdn.net/sinat_17775997/article/details/89330468