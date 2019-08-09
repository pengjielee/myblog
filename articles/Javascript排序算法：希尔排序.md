~~~
function ShellSort1(arr){
	function swap(arr,i,j){
		var temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}
	var gap = Math.floor(arr.length / 2);
	// debugger;
	while(gap > 0){
		for(var i = gap; i < arr.length; i++){
			for(var j = i; j >= gap; j -= gap){
				var temp1 = arr[j-gap];
				var temp2 = arr[j];
				if(temp1 > temp2){
					swap(arr,j-gap,j);
				}else{
					break;
				}
				console.log(i+':'+j+':'+gap);
				console.log(arr);
			}
		}
		gap = Math.floor(gap / 2);
		console.log(i+':'+gap);
		console.log(arr);
		console.log('-------------');
	}
	return arr;
}
var arr = [80, 93, 60, 12, 42, 30, 68, 85, 10];
var result = ShellSort1(arr);

function ShellSort2(arr){
	var i, j, tmp;
  var gap = parseInt(arr.length/2);      
  for( ; gap > 0; gap = parseInt(gap/2)){
  	debugger;                        
    for(var i = gap; i < arr.length; i++){    //插入排序法 
      tmp = arr[i];
      for(j = i; j >= gap && tmp < arr[j-gap]; j-=gap){
          arr[j] = arr[j-gap];
      }
      arr[j] = tmp;
      console.log(i+':'+j+':'+gap);
			console.log(arr);
    }
    console.log(i+':'+gap);
		console.log(arr);
		console.log('-------------');
  }
  return arr;
}
var arr = [80, 93, 60, 12, 42, 30, 68, 85, 10];
var result = ShellSort2(arr);

function ShellSort3(arr){
	function swap(arr, i, j){ 
    var tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
	};
	var gap = parseInt(arr.length/2);
  while(gap > 0){
    for(var k = 0; k < gap; k++){
      for(var i = k + gap; i < arr.length; i += gap){
          for(var j = i - gap; j >= k; j -= gap){
            if(arr[j] > arr[j+gap])
              swap( arr, j, j+gap);
            else
              break;
          }
      }
    }
    gap = parseInt(gap / 2);
  }
  return arr;
}
var arr = [80, 93, 60, 12, 42, 30, 68, 85, 10];
var result = ShellSort3(arr);
~~~