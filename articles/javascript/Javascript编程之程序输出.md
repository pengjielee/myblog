1、question
```
const a = {
  i: 1,
  toString: function () {
    return a.i++;
  }
}

console.log(a.toString()) // 1
console.log(a.valueOf())  // 对象本身

// 如何打出Hello World！呢？
if(a == 1 && a == 2 && a == 3) {
  console.log('Hello World!');
}
```

2、
```
var i = 0;

with({
  get a() {
    return ++i;
  }
}) {
  if (a == 1 && a == 2 && a == 3)
    console.log("wohoo");
}
```

3、
```
var a = [1,2,3];
a.join = a.shift;
console.log(a == 1 && a == 2 && a == 3);
```

4、
```
console.log(typeof(null)) //object
console.log(typeof(undefined)) //undefined
console.log(typeof(NaN)) //number

var str = '12345f'
console.log(typeof(str)) //string
console.log(typeof(str++)) //number，console.log(str++);//NaN
```

5、
```
var x = 1, y = 2, z = 3;
var add = function(x){
  return x = x + 1;
}
x = add(1);  //x=2
function add(x){  //函数声明提升了
  return x = x + 3;
}
y = add(2); //y=3
z = add(3); //z=4
console.log(x+'-'+y+'-'+z) //2-3-4
```

6、
```
var hello = function(){
  console.log('hello1')
}
function hello(){ //函数声明提升了
  console.log('hello2')
}
hello(); //hello1
```

7、
```
for(var i = 0; i < 3; i++){
  console.log(i)
  setTimeout(function(){
    console.log(i)
  },0)
} // 0 1 2 3 3 3
```

```
for(var i = 0; i < 3; i++){
  console.log(i)
}// 0 1 2

console.log(i); //3
```

8、
```
var num = 1;

var object = {
  num: 2,
  add : function(){
    this.num = 3;
    return function(){
      console.log(this.num);
      this.num = 4;
    }
  }
}

console.log(object.num);//2, object作用域下
console.log(num); //1, window作用域下
var add = object.add;
add()();//3, window作用域下,this是window
object.add()()//4, window作用域下,this是window
```

## More

[https://stackoverflow.com/questions/48270127/can-a-1-a-2-a-3-ever-evaluate-to-true](https://stackoverflow.com/questions/48270127/can-a-1-a-2-a-3-ever-evaluate-to-true)