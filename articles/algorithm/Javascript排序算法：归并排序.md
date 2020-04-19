归并排序

## 概述

如果要排序一个数组，我们先把数组从中间分成前后两部分，然后对前后两部分分别排序，再将排好序的两部分合并在一起，这样整个数组就有序了。

归并排序使用的是分治思想。

分治，就是分而治之，将一个大问题分解成小的子问题来解决。小的子问题解决了，大问题也就解决了。

分治是一种解决问题的处理思想，递归是一种编程技巧。

## 复杂度

## 实现
```
// Split the array into halves and merge them recursively 
function mergeSort1 (arr) {
  //debugger;
  if (arr.length === 1) {
    // return once we hit an array with a single item
    return arr
  }
  const middle = Math.floor(arr.length / 2) // get the middle item of the array rounded down
  const left = arr.slice(0, middle) // items on the left side
  const right = arr.slice(middle) // items on the right side

  var result = merge1(mergeSort1(left),mergeSort1(right));
  return result;
}

// compare the arrays item by item and return the concatenated result
function merge1 (left, right) {
  let result = []
  let indexLeft = 0
  let indexRight = 0

  while (indexLeft < left.length && indexRight < right.length) {
    if (left[indexLeft] < right[indexRight]) {
      result.push(left[indexLeft])
      indexLeft++
    } else {
      result.push(right[indexRight])
      indexRight++
    }
  }

  result = result.concat(left.slice(indexLeft)).concat(right.slice(indexRight));
  return result;
}

function mergeSort2 (arr) {
  //debugger;
  if (arr.length === 1) {
    // return once we hit an array with a single item
    return arr
  }
  const middle = Math.floor(arr.length / 2) // get the middle item of the array rounded down
  const left = arr.slice(0, middle) // items on the left side
  const right = arr.slice(middle) // items on the right side

  var result = merge2(mergeSort2(left),mergeSort2(right));
  return result;
}

function merge2 (left, right) {
  let result = []
  let indexLeft = 0
  let indexRight = 0
  let current = 0

  while (current < (left.length + right.length)) {
    let isLeftEnd = indexLeft >= left.length;
    let isRightEnd = indexRight >= right.length;

    var flag = !isLeftEnd && (isRightEnd || (left[indexLeft] < right[indexRight]))
    if (flag) {
      result[current] = left[indexLeft];
      indexLeft++
    } else {
      result[current] = right[indexRight];
      indexRight++
    }
    current ++;
  }
  return result;
}

// const arr = [2, 5, 1, 3, 7, 2, 3, 8, 6, 3]
var arr = [ 5,9,8,2,4];
console.log(mergeSort2(arr));
```


merge sort:
https://www.geeksforgeeks.org/merge-sort/

merge sort wiki:
https://en.wikipedia.org/wiki/Merge_sort

图解排序算法(四)之归并排序:
https://blog.csdn.net/qq_41138935/article/details/79754096