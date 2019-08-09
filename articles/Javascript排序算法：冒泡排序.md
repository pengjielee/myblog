冒泡排序（Bubble Sort）  

### 算法概述：  
它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。  

### 冒泡排序有时被称为下沉排序（Sinking Sort）。  
1. 在较大的值可能会被视为更重，因此可以看出，逐步下沉到底层名单。  
2. 所述较小的值可能被认为是轻，因此可以看出，逐步冒泡到顶部列表的。  

### 算法步骤：  
1. 比较相领的元素。如果第一个比第二个大，就交换它们两个。  
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。 
3. 针对所有的元素重复以上的步骤，除了最后一个。  
4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。  

### 复杂度： 
最好时间复杂度：O(n)   
最坏时间复杂度：O(n^2)   
平均时间复杂度：O(n^2)   
空间复杂度： 总共 O(n)，需要辅助空间O(1)   

算法稳定性：稳定排序 

### 算法动画：
![](http://static.pengjielee.cn/uploads/2017/12/bubbleSort.gif)

### 算法实现：
~~~
//冒泡实现1：
function bubbleSort(arr){
  var i = arr.length, j, temp;
  while(i > 0){
    //debugger;
    for(j = 0; j < i-1; j++){
        if(arr[j] > arr[j+1]){
            temp = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = temp;
        }
    }
    i--;
  }
  return arr;
}
console.log(bubbleSort([3,8,10,4,2]))
 
//冒泡实现2：
Array.prototype.bubbleSort = function() {
  var i, j, temp;
  for (i = 0; i < this.length - 1; i++){
    //debugger;
    for (j = 0; j < this.length - 1 - i; j++){
      if (this[j] > this[j + 1]) {
        temp = this[j];
        this[j] = this[j + 1];
        this[j + 1] = temp;
      }
    } 
  } 
  return this;
};
var num = [3,8,10,4,2];
console.log(num.bubbleSort());
~~~

~~~
function BubbleSort1(arr){
  var i, j, temp;

  for(i = 0; i < arr.length - 1; i++){
    for(j = 0; j < arr.length - 1; j++){
      if(arr[j] > arr[j+1]){
        temp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = temp;
      }
      console.log(i+':'+j);
      console.log(arr);
    }
    console.log(i);
    console.log(arr);
    console.log('-------------')
  }
  
  return arr;
}
var arr = [ 5,9,8,2,4]
var result = BubbleSort1(arr); 


function BubbleSort2(arr){
  var i, j, temp;

  for(i = 0; i < arr.length - 1; i++){
    for(j = 0; j < arr.length - i - 1; j++){
      if(arr[j] > arr[j+1]){
        temp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = temp;
      }
      console.log(i+':'+j);
      console.log(arr);
    }
    console.log(i);
    console.log(arr);
    console.log('-------------')
  }
  
  return arr;
}
var arr = [ 5,9,8,2,4]
var result = BubbleSort2(arr);


function BubbleSort3(arr){
  var i, j, temp;

  for(i = arr.length; i > 0; i--){
    for(j = 0; j < i - 1; j++){
      if(arr[j] > arr[j+1]){
        temp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = temp;
      }
      console.log(i+':'+j);
      console.log(arr);
    }
    console.log(i);
    console.log(arr);
    console.log('-------------')
  }
  
  return arr;
}
var arr = [ 5,9,8,2,4]
var result = BubbleSort3(arr);



function BubbleSort4(arr){
  var i, j, temp, flag = true;

  for(i = arr.length; i > 0 && flag; i--){
    flag = false;
    for(j = 0; j < i - 1; j++){
      if(arr[j] > arr[j+1]){
        temp = arr[j];
        arr[j] = arr[j+1];
        arr[j+1] = temp;
        flag = true;
      }
      console.log(i+':'+j);
      console.log(arr);
      console.log(flag)
    }
    console.log(i);
    console.log(arr);
    console.log(flag)
    console.log('-------------')
  }
  
  return arr;
}
var arr = [ 2,1,3,5,6,7,8,9]
var result = BubbleSort4(arr);
~~~

### 参考：
[维基百科中文](https://zh.wikipedia.org/wiki/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F)  
[维基百科英文](https://en.wikipedia.org/wiki/Bubble_sort)   
[js排序算法](https://www.cnblogs.com/beli/p/6297741.html)    