## 使用ES5中的indexOf进行去重

```
function uniqueArr(arr) {
  var results = [];
  for (var i = 0; i < arr.length; i++) {
    if (results.indexOf(arr[i]) === -1) {
      results.push(arr[i]);
    }
  }
  return results;
}
```

## 先排序然后再相邻比较去重

```
function uniqueArr(arr) {
  arr.sort();
  var results = [arr[0]];
  for (var i = 1; i < arr.length; i++) {
    if (arr[i] !== results[results.length - 1]) {
      results.push(arr[i]);
    }
  }
  return results;
}
```

## 使用map去重

```
function uniqueArr(arr) {
  var map = {};
  if (arr && Array.isArray(arr)) {
    for (var i = arr.length - 1; i >= 0; --i) {
      if (arr[i] in map) {
        arr.splice(i, 1);
      } else {
        map[arr[i]] = true;
      }
    }
  }
  return arr;
}
```