栈就像生活中的一堆盘子一样，只能在盘子顶放置盘子（入栈），也只能在盘子顶取盘子（出栈）。

栈的特点：
1. 栈顶入栈，栈顶出栈；
2. 后进先出；

栈的操作：
1. 入栈；
2. 出栈；

~~~
function Stack() {
  this.dataStorage = [];
  this.top = 0;
  this.push = push;
  this.pop = pop;
  this.peek = peek;
  this.clear = clear;
  this.length = length;
}

function push(element) {
  this.dataStorage[this.top++] = element;
}

function peek() {
  return this.dataStorage[this.top - 1];
}

function pop() {
  return this.dataStorage[--this.top];
}

function clear() {
  this.top = 0;
}

function length() {
  return this.top;
}

var stack = new Stack();
stack.push(1);
stack.push(2);

console.log(stack.length());
console.log(stack.peek());
console.log(stack.pop());

stack.clear();
console.log(stack.length());
~~~