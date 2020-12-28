队列也是一种线性表。

队列就像生活中的排队一样，刚来的人入队（push）要排在队尾(rear)，每次出队(pop)的都是队首(front)的人。

队列的特点：
1. 队尾入队，队头出队。
2. 先进先出（FIFO,first in first out）。

队列的操作：
1. 初始化队列；
2. 判断队列是否为空；
3. 入队（队列的插入操作）；
4. 出队（队列的删除操作）；
5. 求队列中的元素个数；
6. 获取队首元素；

对列的存储结构：
1. 基于数组实现；
2. 基于链表实现；

循环对列：队列头尾相接的顺序存储结构称为循环队列。
链对列；

基于数组的循环队列实现

队列的“假溢出“： 

```
// 实现队列
class Queue {
	constructor(){
		this.list = [];
	}

	// 入队
	enqueue(data){
		this.list.push(data);
	}

	// 出队
	dequeue(){
		if(this.isEmpty()){
			throw new Error('queue is empty')
		}
		return this.list.shift();
	}

	// 返回队头元素
	first(){
		if(this.isEmpty()){
			throw new Error('queue is empty')
		}
		return this.list[0];
	}

	// 返回队尾元素
	last(){
		if(this.isEmpty()){
			throw new Error('queue is empty')
		}
		return this.list[this.list.length - 1];
	}

	// 判断队列是否为空
	isEmpty(){
		return this.list.length === 0;
	}

	// 返回队列长度
	getLength(){
		return this.list.length;
	}

	// 清空队列
	clear(){
		this.list = [];
	}

	// 打印队列
	print(){
		console.log(this.list.join(','))
	}
}

var peopels = new Queue();
peopels.enqueue('jim');
peopels.enqueue('tom');
peopels.enqueue('jack');

peopels.print(); // jim,tom,jack
```

## More 

队列原理
https://blog.csdn.net/zhongguozhichuang/article/details/53196415

队列
https://blog.csdn.net/hjjdehao/article/details/69201276

数据结构
http://blog.jobbole.com/tag/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/

程序员的内功
https://www.cnblogs.com/jingmoxukong/p/4329079.html