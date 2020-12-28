## 概述 

它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。  

## 冒泡排序（下沉排序，Sinking Sort） 

1. 较大的值被视为是重，逐步下沉到底层列表。  
2. 较小的值被视为是轻，逐步冒泡到顶部列表。  

## 步骤 

1. 比较相邻的元素。如果第一个比第二个大，就交换它们两个。  
2. 对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。 
3. 针对所有的元素重复以上的步骤，除了最后一个。  
4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。  

## 复杂度 

最好时间复杂度：O(n)   
最坏时间复杂度：O(n^2)   
平均时间复杂度：O(n^2)   
空间复杂度： 总共 O(n)，需要辅助空间O(1)   
算法稳定性：稳定排序 

## 代码

1. 
```
function bubbleSort(arr) {
  let temp;
  for (let i = arr.length; i > 0; i--) {
    //console.log('i', i, arr);
    for (let j = 0; j < i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
    //console.log('i', i, arr);
  }
  return arr;
}
var num = [3, 8, 10, 4, 2];
console.log(bubbleSort(num));
```

2. 
```
Array.prototype.bubbleSort = function () {
  let temp;
  for (let i = 0; i < this.length; i++) {
    //console.log('i', i, this);
    for (let j = 0; j < this.length - 1 - i; j++) {
      if (this[j] > this[j + 1]) {
        temp = this[j];
        this[j] = this[j + 1];
        this[j + 1] = temp;
      }
    }
    //console.log('i', i, this);
  }
  return this;
};
var num = [3, 8, 10, 4, 2];
console.log(num.bubbleSort());
```

3. 

```
function bubbleSort(arr) {
  let temp, flag = true;

  for (let i = arr.length; i > 0 && flag; i--) {
    flag = false;
    for (let j = 0; j < i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
        flag = true;
      }
    }
  }

  return arr;
}
var num = [3, 8, 10, 4, 2];
console.log(bubbleSort(num));
```

## More  

维基百科中文  
https://zh.wikipedia.org/wiki/%E5%86%92%E6%B3%A1%E6%8E%92%E5%BA%8F
