~~~
var arr = [5,3,4,6,2];

var min;

for(var i = 0; i < arr.length; i++){
	min = i;
	debugger;
	for(var j = i+1; j < arr.length; j++){
		if(arr[min] > arr[j]){
			min = j;
		}
	}

	if(i != min){
		var temp = arr[i];
		arr[i] = arr[min];
		arr[min] = temp;
	}
}
~~~