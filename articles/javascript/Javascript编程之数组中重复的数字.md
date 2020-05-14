## 题目描述

```
在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 

例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

Input:
{2,3,1,0,2,5,3}

Output:
2

要求：时间复杂度 O(N)，空间复杂度 O(1)。
```

## 代码实现

```
const swap = (arr,i,j) => {
	const temp = arr[i];
	arr[i] = arr[j];
	arr[j] = temp;
}

const duplicate = (arr) => {
	let result = null
	if(arr.length <= 0) {
		return result;
	}

	for(let i = 0; i < arr.length; i++){
		while(arr[i] != i){
			if(arr[i]  === arr[arr[i]]){
				result = arr[i];
				return result;
			}
			swap(arr,i,arr[i])
		}
	}
	return result;
}

var arr = [ 2, 3, 1, 0, 2, 5 ]
var result = duplicate(arr);
console.log(result)

时间复杂度 O(N)，空间复杂度 O(1)。
```

## More

https://github.com/CyC2018/CS-Notes/blob/master/notes/%E5%89%91%E6%8C%87%20Offer%20%E9%A2%98%E8%A7%A3%20-%203~9.md#3-%E6%95%B0%E7%BB%84%E4%B8%AD%E9%87%8D%E5%A4%8D%E7%9A%84%E6%95%B0%E5%AD%97

https://www.cnblogs.com/AndyJee/p/4693099.html