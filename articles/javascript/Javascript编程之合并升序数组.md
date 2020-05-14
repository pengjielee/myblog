将两个升序数组合并成一个升序数组。

## 实现1
```
//O(n) time & O(n) space
function mergeArray1(arr1, arr2){
	var result = [];
	var index1 = 0, index2 = 0, current = 0;

	while(current < (arr1.length + arr2.length)){
		var element1 = arr1[index1];
		var element2 = arr2[index2];

		if(element1 < element2){
			result[current] = element1;
			index1++;
		}else{
			result[current] = element2;
			index2++;
		}
		current++;
	}
	return result;
}

var arr1 = [4, 5, 9], arr2 = [2, 6, 7, 10,12]
var result = mergeArray1(arr1,arr2);
console.log(result) // [2, 4, 5, 6, 7, 9, 10,12]

question:
This works but we have undefined at the end which will always happen since one of our arrays ran out of elements before we finished merging.
```

## 实现2
```
//O(n) time & O(n) space
function mergeArray2(arr1, arr2){
	var result = [];
	var index1 = 0, index2 = 0, current = 0;

	while(current < (arr1.length + arr2.length)){
		var isArr1End = index1 >= arr1.length;
		var isArr2End = index2 >= arr2.length;

		var flag = !isArr1End && (isArr2End || (arr1[index1] < arr2[index2]))
		if(flag){
			result[current] = arr1[index1];
			index1++;
		}else{
			result[current] = arr2[index2];
			index2++;
		}

		current ++;
	}
	return result;
}

var arr1 = [4, 5, 9], arr2 = [2, 6, 7, 10,12]
var result = mergeArray2(arr1,arr2);
console.log(result) // [2, 4, 5, 6, 7, 9, 10,12]
```

## 实现3：
```
function mergeArray3(arr1,arr2){
	var result = arr1.concat(arr2);
	var temp;

	for(var i = 0; i < result.length - 1; i++){
		for(var j = 0; j < result.length - 1 - i;j++){
			if(result[j] > result[j+1]){
				temp = result[j];
				result[j] = result[j+1];
				result[j+1] = temp;
			}
		}
	}
	return result;
}

var arr1 = [4,8,10], arr2 = [5,8,9];
var result = mergeArray3(arr1,arr2); //[4, 5, 8, 8, 9, 10]

function mergeArray4(arr1,arr2){
	var result = arr1.concat(arr2);
	result.sort(function(value1,value2){
		return value1 > value2
	});
	return result;
}

var arr1 = [4,8,10], arr2 = [5,8,9];
var result = mergeArray4(arr1,arr2); //[4, 5, 8, 8, 9, 10]

// O(nlogn) time & O(n) space
function mergeArray5(arr1,arr2){
	let result = [...arr1, ...arr2];
	return result.sort((a,b) => a - b);
}

var arr1 = [4,8,10], arr2 = [5,8,9];
var result = mergeArray5(arr1,arr2); //[4, 5, 8, 8, 9, 10]
```
