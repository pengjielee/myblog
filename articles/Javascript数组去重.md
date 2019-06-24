### 使用ES5中的indexOf进行去重：
~~~
function uniqueArr(){  
  var n = [];  
  for(var i=0;i<arr.length;i++){  
    if(n.indexOf(arr[i]) === -1){  
      n.push(arr[i]);  
    }  
  }  
  return n;  
}
~~~

### 先排序后然后再相邻比较去重 
~~~
function uniqueArr(){  
  arr.sort();  
  var re = [arr[0]];  
  for(var i = 1;i < arr.length;i++){  
    if(arr[i]!==re[re.length-1]){  
      re.push(arr[i]);  
    }  
  }  
  return re;  
}  
~~~

### 使用map去重
~~~
function uniqueArr(arr){  
  var map = {};  
  if(arr && Array.isArray(arr)){  
      for(var i = arr.length;i >= 0; --i){  
          if(arr[i] in map){  
              arr.splice(i,1);  
          }else{  
              map[arr[i]] = true;  
          }  
      }  
  }  
  return arr;  
}  
~~~