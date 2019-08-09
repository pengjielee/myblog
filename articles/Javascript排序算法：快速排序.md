快速排序（Quick sort）

### 算法概述
快速排序（Quick sort），又称划分交换排序（partition-exchange sort），一种排序算法，最早由东尼·霍尔提出。  
快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为两个子序列（sub-lists）。

### 算法步骤：
1. 从数列中挑出一个元素，称为”基准”（pivot），
2. 重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（相同的数可以到任何一边）。在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
3. 递归地（recursively）把小于基准值元素的子数列和大于基准值元素的子数列排序。
4. 递归到最底部时，数列的大小是零或一，也就是已经排序好了。这个算法一定会结束，因为在每次的迭代（iteration）中，它至少会把一个元素摆到它最后的位置去。

### 复杂度：
最坏时间复杂度 (n^2)  
最优时间复杂度 (nlog n)  
平均时间复杂度 (nlog n)  
空间复杂度 根据实现的方式不同而不同  

### 算法动画：
![](http://static.pengjielee.cn/uploads/2017/12/quickSort.gif)

### 算法实现：
~~~
实现1：
var QuickSort = function() {
  function swap(array, a, b) {
    var temp = array[a];
    array[a] = array[b];
    array[b] = temp;
  }

  function partition(array, left, right) {
    var pivot = array[Math.floor(left + right) / 2];
    var i = left;
    var j = right;

    while (i <= j) {
      while (compare(array[i], pivot) === -1) {
        i++;
      }
      while (compare(array[j], pivot) === 1) {
        j--;
      }
      if (i <= j) {
        swap(array, i, j);
        i++;
        j--;
      }
    }
    return i;
  }

  function compare(a, b) {
    if (a === b) {
      return 0;
    }
    return a < b ? -1 : 1;
  }

  function sort(array, left, right) {
    let index;
    if (array.length > 1) {
      index = partition(array, left, right);
      if (left < index - 1) {
        quick(array, left, index - 1);
      }
      if (index < right) {
        quick(array, index, right);
      }
    }
    return array;
  }
};


实现2：
function swap(array, a, b) {
  var temp = array[a];
  array[a] = array[b];
  array[b] = temp;
}

function partition(array, low, high) {
  var pivot = low;
  var pivotVal = array[pivot];

  swap(array, pivot, high);

  for (var i = low; i < high; i++) {
    if (array[i] < pivotVal) {
      swap(array, i, pivot);
      pivot++;
    }
  }

  swap(array, high, pivot);
  return pivot;
}

function sort(array, low, high) {
  if (low < high) {
    var pivot = partition(array, low, high);
    sort(array, low, pivot - 1);
    sort(array, pivot + 1, high);
  }
  return array;
}

function QuickSort(array) {
  return sort(array, 0, array.length - 1);
}

var array = [4, 8, 2, 10, 50, 30, 80];
QuickSort(array);


实现3：
function swap(array, a, b) {
  var temp = array[a];
  array[a] = array[b];
  array[b] = temp;
}

function partition(array, low, high) {
  var i = low;
  var j = high;

  var pivot = array[Math.floor((low + high) / 2)];

  while (i <= j) {
    while (array[i] < pivot) {
      i++;
    }
    while (array[j] > pivot) {
      j--;
    }
    if (i <= j) {
      swap(array, i, j);
      i++;
      j--;
    }
  }
  return i;
}

function sort(array, low, high) {
  if (low < high) {
    var pivot = partition(array, low, high);
    sort(array, low, pivot - 1);
    sort(array, pivot, high);
  }
  return array;
}

function QuickSort(array) {
  return sort(array, 0, array.length - 1);
}

var array = [4, 8, 2, 10, 50, 30, 80];
var result = QuickSort(array);
console.log(result);
~~~
