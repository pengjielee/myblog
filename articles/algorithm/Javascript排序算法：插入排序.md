## 概述

它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。插入排序在实现上，通常采用in-place排序（即只需用到O(1)的额外空间的排序），因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。  

## 步骤  

1. 从第一个元素开始，该元素可以认为已经被排序； 
2. 取出下一个元素，在已经排序的元素序列中从后向前扫描；  
3. 如果该元素（已排序）大于新元素，将该元素移到下一位置；  
4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；  
5. 将新元素插入到该位置后；  
6. 重复步骤2 ~ 5；   

## 复杂度 

最好时间复杂度：O(n)   
最坏时间复杂度：O(n^2)   
平均时间复杂度：O(n^2)   
空间复杂度： 总共 O(n)，需要辅助空间O(1)   

原地排序算法。

稳定性：是稳定排序算法。

## 实现
```
function InsertSort(arr){
	for(var i = 1; i < arr.length; i++){
		for(var j = i; j > 0 && arr[j] < arr[j-1]; j--){
			var temp = arr[j-1];
			arr[j-1] = arr[j];
			arr[j] = temp;
		}
	}
	return arr;
}
var arr = [5,3,4,6,2]
var result = InsertSort(arr);

function InsertSort1(arr){
  for(var i = 1; i < arr.length; i++){
    for(var j = 0; j < i; j++){
      //debugger;
      var tempj = arr[j];
      var tempi = arr[i];
      if(tempj > tempi){
        arr.splice(j,0,arr[i]); //在数组j处添加一个元素arr[i]
        arr.splice(i+1,1); //删除数组从i+1开始的1个元素
      }
      console.log(arr);
    }
  }
  return arr;
}
var arr = [ 5,9,8,2,4]
var result = InsertSort1(arr); 


function InsertSort2(arr){
  for(var i = 0; i < arr.length; i++){
    let value = arr[i];// store the current item value so it can be placed right
    //debugger;
    for(var j = i - 1; j > -1 && arr[j] > value; j--){
      // loop through the items in the sorted array (the items from the current to the beginning)
      // copy each item to the next one
      arr[j+1] = arr[j];
    }
    console.log(arr)
    arr[j+1] = value;// the last item we've reached should now hold the value of the currently sorted item
    console.log('----------')
    console.log(arr);
  }
  return arr;
}
var arr = [ 5,9,8,2,4]
var result = InsertSort2(arr); 
```

## More 

维基百科中文
https://zh.wikipedia.org/zh-hans/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F  
