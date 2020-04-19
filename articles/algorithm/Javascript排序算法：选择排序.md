选择排序（Selection Sort）

## 概述

选择排序也分已排序区间和未排序区间。
选择排序每次会从未排序区间中找到最小的元素，将其放到已排序区间的末尾。

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
	let min;

	for(let i = 0; i < arr.length; i++){
		min = i;
		for(let j = i + 1; j < arr.length; j++){
			if(arr[j] < arr[min]){
				min = j;
			}
		}

		if(i != min){
			let temp = arr[i];
			arr[i] = arr[min];
			arr[min] = temp;
		}
	}
}

var arr = [5,3,4,6,2];
selectSort(arr);
```