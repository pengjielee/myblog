## 概述

选择排序分已排序区间和未排序区间。

选择排序每次会从未排序区间中找到最小的元素，将其放到已排序区间的末尾。

## 步骤 

1. 在未排序序列中找到最小（大）元素，存放到排序序列的起始位置；
2. 从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾；
3. 重复第二步，直到所有元素均排序完毕；

## 复杂度

空间复杂度：O(1)。
最好情况时间复杂度：O(n^2)。
最坏情况时间复杂度：O(n^2)。
平均情况时间复杂度：O(n^2)。

原地排序算法。

算法稳定性：不稳定排序算法。

## 实现

```
const selectSort = (arr) => {
	let minIndex;

	for(let i = 0; i < arr.length - 1; i++){
		// 第一个元素为已排序的
		minIndex = i;

		// 从第二个元素开始起，查找最小的
		for(let j = i + 1; j < arr.length; j++){
			if(arr[j] < arr[minIndex]){
				minIndex = j;
			}
		}

		if(i != minIndex){
			let temp = arr[i];
			arr[i] = arr[minIndex];
			arr[minIndex] = temp;
		}
	}

	return arr;
}

var arr = [5,3,4,6,2];
console.log(selectSort(arr));
```

## More 

选择排序
https://www.runoob.com/w3cnote/selection-sort.html 