1、
~~~
const a = {
  i: 1,
  toString: function () {
    return a.i++;
  }
}

console.log(a.toString()) // 1
console.log(a.valueOf())  // 对象本身

if(a == 1 && a == 2 && a == 3) {
  console.log('Hello World!');
}
~~~

2、
~~~
var i = 0;

with({
  get a() {
    return ++i;
  }
}) {
  if (a == 1 && a == 2 && a == 3)
    console.log("wohoo");
}
~~~

3、
~~~
var a = [1,2,3];
a.join = a.shift;
console.log(a == 1 && a == 2 && a == 3);
~~~

4、
~~~
console.log(typeof(null)) //object
console.log(typeof(undefined)) //undefined
console.log(typeof(NaN)) //number

var str = '12345f'
console.log(typeof(str)) //string
console.log(typeof(str++)) //number
~~~

5、
~~~
var x = 1, y = 2, z = 3;
var add = function(x){
  return x = x + 1;
}
x = add(1);  //x=4
function add(x){
  return x = x + 3;
}
y = add(2); //y=5
z = add(3); //z=6
console.log(x+'-'+y+'-'+z) //2-3-4
~~~

6、
~~~
var hello = function(){
  console.log('hello1')
}
function hello(){
  console.log('hello2')
}
hello(); //hello1
~~~

7、
~~~
//first apply
for(var i = 0; i < 3; i++){
  console.log(i)
  setTimeout(function(){
    return function(){
      console.log(i)
    }
  },0)
} // 0 1 2 3 

//second apply
for(var i = 0; i < 3; i++){
  console.log(i)
  setTimeout(function(){
    return function(){
      console.log(i)
    }
  },0)
} // 0 1 2 6

for(var i = 0; i < 3; i++){
  console.log(i)
}// 0 1 2

for(var i = 0; i < 3; ++i){
  console.log(i)
}// 0 1 2
~~~

8、
~~~
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

console.log(object.num);//2
console.log(num); //1
var add = object.add;
add()();//3
object.add()()//4
~~~

参考：
[https://stackoverflow.com/questions/48270127/can-a-1-a-2-a-3-ever-evaluate-to-true](https://stackoverflow.com/questions/48270127/can-a-1-a-2-a-3-ever-evaluate-to-true)